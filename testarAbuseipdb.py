from APIs.abuseipdb import verificar_ip
from utils.classificar import classificar_risco

def main():
    ip = input("Digite um IP: ")

    result = verificar_ip(ip)

    if "error" in result:
        print("Erro ao consultar API")
        return

    risco = classificar_risco(result["score"])

    print("\n--- Resultado ---")
    print(f"IP: {result['ip']}")
    print(f"Pontuação: {result['score']}")
    print(f"País: {result['country']}")
    print(f"ISP: {result['isp']}")
    print(f"Reportado: {result['total_reports']}")
    print(f"Classificação: {risco}")

if __name__ == "__main__":
    main()