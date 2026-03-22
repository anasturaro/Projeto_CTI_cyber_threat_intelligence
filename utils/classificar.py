def classificar_risco(score):
    if score >= 80:
        return "Malicioso"
    elif score >= 30:
        return "Suspeito"
    else:
        return "Seguro"

def final_risco(abuseipdb_score, vt_malicious, vulns):
    if (abuseipdb_score and abuseipdb_score >= 80) or (vt_malicious and vt_malicious >= 5) or (vulns and len(vulns) > 0):
        return "Alto"
    elif (abuseipdb_score and abuseipdb_score >= 30) or (vt_malicious and vt_malicious >= 2):
        return "Médio"
    else:
        return "Baixo"