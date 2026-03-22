import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

def vericar_ip_virustotal(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"

    headers = {
        "x-apikey": API_KEY
    }

    resposta = requests.get(url, headers=headers)

    #verifica erro
    if resposta.status_code != 200:
        return {"erro": "Ocorreu um erro, status diferente de 200!"}

    data = resposta.json()

    stats = data["data"]["attributes"]["last_analysis_stats"]

    return {
        "malicious": stats["malicious"],
        "suspicious": stats["suspicious"],
        "harmless": stats["harmless"],
        "undetected": stats["undetected"]
    }