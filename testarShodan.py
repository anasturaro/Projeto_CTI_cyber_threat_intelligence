from APIs.shodan import verificar_ip_shodan

def main():
    ip = input("Digite um IP: ")
    shodan = verificar_ip_shodan(ip)

    if "error" in shodan:
        print("Erro no Shodan")
    else:
        print("\n--- Shodan ---")
        print(f"Organização: {shodan['org']}")
        print(f"Sistema: {shodan['os']}")
        print(f"Portas: {shodan['ports']}")
        print(f"Vulnerabilidades: {shodan['vulns']}")

if __name__ == "__main__":
    main()
