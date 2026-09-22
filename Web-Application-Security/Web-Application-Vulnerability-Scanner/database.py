import sqlite3,json
from datetime import datetime
DB="scanner.db"
def connect():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c
def init_db():
    c=connect(); c.execute("CREATE TABLE IF NOT EXISTS scans (id INTEGER PRIMARY KEY AUTOINCREMENT,target TEXT NOT NULL,created_at TEXT NOT NULL,result_json TEXT NOT NULL)"); c.commit(); c.close()
def save_scan(target,result):
    c=connect(); cur=c.execute("INSERT INTO scans(target,created_at,result_json) VALUES(?,?,?)",(target,datetime.now().isoformat(timespec="seconds"),json.dumps(result))); c.commit(); sid=cur.lastrowid; c.close(); return sid
def get_scans():
    c=connect(); rows=c.execute("SELECT id,target,created_at FROM scans ORDER BY id DESC").fetchall(); c.close(); return [dict(r) for r in rows]
def get_scan(sid):
    c=connect(); r=c.execute("SELECT id,target,created_at,result_json FROM scans WHERE id=?",(sid,)).fetchone(); c.close()
    if not r:return None
    d=dict(r); d["result"]=json.loads(d.pop("result_json")); return d
