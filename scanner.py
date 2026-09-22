from urllib.parse import urljoin,urlparse,parse_qsl,urlencode,urlunparse
import requests
from bs4 import BeautifulSoup

TIMEOUT=8
MAX_PAGES=20
UA="Authorized-Web-Security-Scanner/1.0"

HEADERS={
"Content-Security-Policy":"Helps reduce XSS impact.",
"X-Content-Type-Options":"Helps prevent MIME sniffing.",
"X-Frame-Options":"Helps reduce clickjacking.",
"Referrer-Policy":"Controls referrer information.",
"Strict-Transport-Security":"Helps enforce HTTPS."
}

def req(s,method,url,**kw):
    kw.setdefault("timeout",TIMEOUT); kw.setdefault("allow_redirects",True)
    return s.request(method,url,**kw)

def norm(url):
    p=urlparse(url)
    return urlunparse((p.scheme,p.netloc,p.path or "/","",p.query,""))

def same_origin(a,b):
    x,y=urlparse(a),urlparse(b)
    return (x.scheme,x.netloc)==(y.scheme,y.netloc)

def crawl(s,target):
    queue=[norm(target)]; seen=set(); pages=[]
    while queue and len(pages)<MAX_PAGES:
        url=queue.pop(0)
        if url in seen: continue
        seen.add(url)
        try: r=req(s,"GET",url)
        except requests.RequestException: continue
        page={"url":url,"status":r.status_code,"content_type":r.headers.get("Content-Type",""),"length":len(r.content),"forms":[]}
        pages.append(page)
        if "text/html" not in page["content_type"].lower(): continue
        soup=BeautifulSoup(r.text,"html.parser")
        for form in soup.find_all("form"):
            inputs=[{"name":i.get("name"),"type":i.get("type","text")} for i in form.find_all(["input","textarea","select"]) if i.get("name")]
            page["forms"].append({"action":urljoin(url,form.get("action") or url),"method":(form.get("method") or "GET").upper(),"inputs":inputs})
        for a in soup.find_all("a",href=True):
            link=norm(urljoin(url,a["href"]))
            if same_origin(target,link) and link not in seen: queue.append(link)
    return pages

def header_checks(r):
    out=[]
    for name,desc in HEADERS.items():
        if name=="Strict-Transport-Security" and urlparse(r.url).scheme!="https": continue
        if name not in r.headers:
            out.append({"title":f"Missing security header: {name}","severity":"Low","category":"Security Misconfiguration","evidence":f"{name} was not present.","recommendation":desc})
    return out

def cookie_checks(r):
    out=[]
    raw=r.headers.get("Set-Cookie","")
    if raw and "httponly" not in raw.lower():
        out.append({"title":"Cookie without HttpOnly attribute","severity":"Medium","category":"Session Management","evidence":raw[:180],"recommendation":"Use HttpOnly on session cookies where appropriate."})
    if raw and "samesite" not in raw.lower():
        out.append({"title":"Cookie without SameSite attribute","severity":"Low","category":"Session Management","evidence":raw[:180],"recommendation":"Configure an appropriate SameSite policy."})
    return out

def reflection_check(s,url):
    p=urlparse(url); params=dict(parse_qsl(p.query,keep_blank_values=True)); out=[]
    marker="SECURITY_SCANNER_REFLECTION_TEST_9f31"
    for key in list(params)[:5]:
        q=params.copy(); q[key]=marker
        test=urlunparse((p.scheme,p.netloc,p.path or "/","",urlencode(q),""))
        try:r=req(s,"GET",test)
        except requests.RequestException:continue
        if marker in r.text:
            out.append({"title":f"User input reflected: {key}","severity":"Informational","category":"Input Handling","evidence":f"Inert marker reflected for '{key}'.","recommendation":"Review contextual output encoding; reflection alone does not prove XSS."})
    return out

def rank(x): return {"Critical":4,"High":3,"Medium":2,"Low":1,"Informational":0}.get(x,0)

def scan_target(target):
    s=requests.Session(); s.headers["User-Agent"]=UA
    try:first=req(s,"GET",target)
    except requests.RequestException as e:
        return {"target":target,"pages":[],"findings":[],"summary":{"total":0,"critical":0,"high":0,"medium":0,"low":0},"errors":[str(e)]}
    findings=header_checks(first)+cookie_checks(first)
    pages=crawl(s,target); errors=[]
    for page in pages:
        try:
            req(s,"GET",page["url"])
            findings += reflection_check(s,page["url"])
        except requests.RequestException as e: errors.append(f"{page['url']}: {e}")
    unique={(x["title"],x["evidence"]):x for x in findings}
    findings=sorted(unique.values(),key=lambda x:rank(x["severity"]),reverse=True)
    summary={"total":len(findings),"critical":sum(x["severity"]=="Critical" for x in findings),"high":sum(x["severity"]=="High" for x in findings),"medium":sum(x["severity"]=="Medium" for x in findings),"low":sum(x["severity"]=="Low" for x in findings)}
    return {"target":target,"pages":pages,"findings":findings,"summary":summary,"errors":errors}
