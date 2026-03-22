from flask import Flask, render_template, request, redirect, url_for
from APIs.full import analizar_ip
from utils.classificar import final_risco
from DB.DB import create_db, salvar_analise, buscar_analise, buscar_por_id
import requests

def get_geo(ip):
    url = f"http://ip-api.com/json/{ip}"
    return requests.get(url).json()

app = Flask(__name__)

create_db()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    status = checar_status_api()

    if request.method == "POST":
        ip = request.form.get("ip")

        data = analizar_ip(ip)

        if data:
            risco = final_risco(
                data.get("abuseipdb_score"),
                data.get("vt_malicious"),
                data.get("vulns", [])
            )

            id_salvo = salvar_analise(data, risco)

            return redirect(url_for("detalhes", id=id_salvo))

    return render_template("index.html", result=result, status=status)

@app.route("/historico")
def historico():
    data = buscar_analise()
    return render_template("historico.html", data=data)

@app.route("/detalhes/<int:id>")
def detalhes(id):
    data = buscar_por_id(id)
    geo = get_geo(data["ip"])
    return render_template("detalhes.html", data=data, geo=geo)

import os

def checar_status_api():
    status = {}

    # Shodan
    shodan_data = checar_shodan()
    status["shodan"] = shodan_data

    # AbuseIPDB
    try:
        r = requests.get(... )
        status["abuseipdb"] = {
            "status": r.status_code == 200
        }
    except:
        status["abuseipdb"] = {"status": False}

    # VirusTotal
    try:
        r = requests.get(... )
        status["vt"] = {
            "status": r.status_code == 200
        }
    except:
        status["vt"] = {"status": False}

    return status

def checar_shodan():
    try:
        r = requests.get(
            f"https://api.shodan.io/api-info?key={os.getenv('SHODAN_API_KEY')}"
        )
        data = r.json()

        return {
            "status": True,
            "query_credits": data.get("query_credits"),
            "scan_credits": data.get("scan_credits")
        }
    except:
        return {"status": False}

if __name__ == "__main__":
    app.run(debug=True)