from APIs.full import analizar_ip
from utils.classificar import final_risco

def main():
    ip = input("Digite um IP: ")

    data = analizar_ip(ip)

    risco = final_risco(
        data["abuseipdb_score"],
        data["vt_malicious"],
        data["vulns"]
    )

    print("\n--- Análise Completa ---")
    print(f"IP: {data['ip']}")
    print(f"Abuseipdb Score: {data['abuseipdb_score']}")
    print(f"Virus Total Malicious: {data['vt_malicious']}")
    print(f"Portas: {data['ports']}")
    print(f"Vulnerabilidades: {data['vulns']}")
    print(f"Risco Final: {risco}")


if __name__ == "__main__":
    main()
