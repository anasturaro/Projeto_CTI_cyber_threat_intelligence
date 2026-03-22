from APIs.virustotal import vericar_ip_virustotal

def main():
    ip = input("Digite um IP: ")
    vt_result = vericar_ip_virustotal(ip)
    if "error" in vt_result:
        print("Erro no VirusTotal")
    else:
        print("\n--- VirusTotal ---")
        print(f"Malicioso: {vt_result['malicious']}")
        print(f"Suspeito: {vt_result['suspicious']}")
        print(f"Seguro: {vt_result['harmless']}")

if __name__ == "__main__":
    main()