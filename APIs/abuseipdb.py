import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ABUSEIPDB_API_KEY")

def verificar_ip(ip):
    url = "https://api.abuseipdb.com/api/v2/check"

    #headers p/autenticação
    headers = {
        "Accept": "application/json",
        "Key": API_KEY
    }

    #requests
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    resposta = requests.get(url, headers=headers, params=params)

    #verificar se houve erro
    if resposta.status_code != 200:
        return {"erro": "Ocorreu um erro, status diferente de 200!"}

    #json
    data = resposta.json()["data"]

    return {
        "ip": data["ipAddress"],
        "score": data["abuseConfidenceScore"],
        "country": data["countryCode"],
        "isp": data["isp"],
        "total_reports": data["totalReports"]
    }
