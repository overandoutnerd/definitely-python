import sqlite3
try:
    conn = sqlite3.connect("career_management.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS placement(id INTEGER PRIMARY KEY,company TEXT,package REAL,status TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS training(id INTEGER PRIMARY KEY,name TEXT,participants INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS alumni(id INTEGER PRIMARY KEY,name TEXT,company TEXT)")
    cur.execute("INSERT OR IGNORE INTO placement VALUES(1,'ABC Technologies',8.5,'Placed')")
    cur.execute("INSERT OR IGNORE INTO training VALUES(1,'Python & AI Training',120)")
    cur.execute("INSERT OR IGNORE INTO alumni VALUES(1,'Rahul','XYZ Ltd')")
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM placement WHERE status='Placed'")
    placed = cur.fetchone()[0]
    cur.execute("SELECT SUM(participants) FROM training")
    trained = cur.fetchone()[0] or 0
    cur.execute("SELECT COUNT(*) FROM alumni")
    alumni = cur.fetchone()[0]
    cur.execute("SELECT MAX(package) FROM placement")
    highest = cur.fetchone()[0] or 0

    print("\n================================================")
    print("       PLACEMENT, TRAINING & ALUMNI")
    print("                 DASHBOARD")
    print("================================================")
    print("Students Placed:",placed)
    print("Students Trained:",trained)
    print("Registered Alumni:",alumni)
    print("Highest Package: ₹",highest,"LPA")
    print("================================================")

except sqlite3.Error as e:
    if "conn" in locals():
        conn.rollback()
    print("Database Error:",e)
finally:
    if "conn" in locals():
        conn.close()