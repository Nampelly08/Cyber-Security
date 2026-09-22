from flask import Flask, render_template, request, jsonify, redirect, url_for
from scanner import scan_target
from database import init_db, save_scan, get_scans, get_scan
from urllib.parse import urlparse

app=Flask(__name__)
init_db()

@app.route("/")
def index():
    return render_template("index.html", scans=get_scans())

@app.route("/scan", methods=["POST"])
def start_scan():
    target=request.form.get("target","").strip()
    p=urlparse(target)
    if p.scheme not in ("http","https") or not p.netloc:
        return render_template("index.html", error="Enter a valid http:// or https:// URL.", scans=get_scans())
    result=scan_target(target)
    sid=save_scan(target,result)
    return redirect(url_for("scan_result",scan_id=sid))

@app.route("/scan/<int:scan_id>")
def scan_result(scan_id):
    scan=get_scan(scan_id)
    return render_template("result.html",scan=scan) if scan else ("Scan not found",404)

@app.route("/api/scan",methods=["POST"])
def api_scan():
    data=request.get_json(silent=True) or {}
    target=(data.get("target") or "").strip()
    p=urlparse(target)
    if p.scheme not in ("http","https") or not p.netloc:
        return jsonify({"error":"Valid http/https target required."}),400
    result=scan_target(target)
    sid=save_scan(target,result)
    return jsonify({"scan_id":sid,"result":result})

if __name__=="__main__":
    app.run(debug=True)
