import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("SHODAN_API_KEY")

def verificar_ip_shodan(ip):
    url = f"https://api.shodan.io/shodan/host/{ip}?key={API_KEY}"

    resposta = requests.get(url)

    if resposta.status_code != 200:
        return {"erro": "Ocorreu um erro, status diferente de 200!"}

    data = resposta.json()

    #tratamento de vulns
    vulns_data = data.get("vulns", {})

    if isinstance(vulns_data, dict):
        vulns = list(vulns_data.keys())
    else:
        vulns = []

    return {
        "ip": data.get("ip_str"),
        "org": data.get("org"),
        "os": data.get("os"),
        "ports": data.get("ports", []),
        "hostnames": data.get("hostnames", []),
        "vulns": vulns
    }