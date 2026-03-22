import sqlite3
import json

def create_db():
    conn = sqlite3.connect("cti.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analise (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        abuseipdb_score INTEGER,
        vt_malicious INTEGER,
        ports TEXT,
        vulns TEXT,
        risco TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

def salvar_analise(data, risco):
    conn = sqlite3.connect("cti.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO analise (ip, abuseipdb_score, vt_malicious, ports, vulns, risco)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["ip"],
        data["abuseipdb_score"],
        data["vt_malicious"],
        json.dumps(data["ports"]),
        json.dumps(data["vulns"]),
        risco
    ))

    conn.commit()
    last_id = cursor.lastrowid
    conn.close()

    return last_id

def buscar_analise():
    conn = sqlite3.connect("cti.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM analise ORDER BY created_at DESC")
    rows = cursor.fetchall()

    conn.close()
    return rows

def buscar_por_id(id):
    conn = sqlite3.connect("cti.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM analise WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            "id": row[0],
            "ip": row[1],
            "abuseipdb_score": row[2],
            "vt_malicious": row[3],
            "ports": json.loads(row[4]) if row[4] else [],
            "vulns": json.loads(row[5]) if row[5] else [],
            "risco": row[6],
            "created_at": row[7]
        }
    return None