from APIs.abuseipdb import verificar_ip
from APIs.virustotal import vericar_ip_virustotal
from APIs.shodan import verificar_ip_shodan

def analizar_ip(ip):
    abuseipdb = verificar_ip(ip)
    virustotal = vericar_ip_virustotal(ip)
    shodan = verificar_ip_shodan(ip)

    if "error" in abuseipdb:
        abuseipdb = {}
    if "error" in virustotal:
        virustotal = {}
    if "error" in shodan:
        shodan = {}

    return {
        "ip": ip,
        "abuseipdb_score": abuseipdb.get("score"),
        "country": abuseipdb.get("country"),
        "isp": abuseipdb.get("isp"),
        "vt_malicious": virustotal.get("malicious"),
        "vt_suspicious": virustotal.get("suspicious"),
        "ports": shodan.get("ports"),
        "org": shodan.get("org"),
        "vulns": shodan.get("vulns", [])
    }