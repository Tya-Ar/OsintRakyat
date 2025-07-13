import whois
import socket
from ipwhois import IPWhois
from colorama import Fore

def analyze_domain(domain):
    print(Fore.YELLOW + f"\n🌐 Analisis WHOIS dan IP untuk: {domain}\n")

    # WHOIS Info
    try:
        w = whois.whois(domain)
        print(Fore.CYAN + "=== WHOIS DATA ===")
        print(Fore.GREEN + f"Domain Name   : {w.domain_name}")
        print(Fore.GREEN + f"Registrar     : {w.registrar}")
        print(Fore.GREEN + f"Created       : {w.creation_date}")
        print(Fore.GREEN + f"Expires       : {w.expiration_date}")
        print(Fore.GREEN + f"Name Servers  : {w.name_servers}")
        print(Fore.GREEN + f"Emails        : {w.emails}")
    except Exception as e:
        print(Fore.RED + f"[!] Gagal ambil WHOIS: {e}")

    # IP Resolve & GeoIP
    try:
        ip = socket.gethostbyname(domain)
        print(Fore.CYAN + f"\n=== DNS RESOLVE ===")
        print(Fore.GREEN + f"IP Address    : {ip}")

        obj = IPWhois(ip)
        results = obj.lookup_rdap()
        print(Fore.CYAN + f"\n=== GEOIP / ASN INFO ===")
        print(Fore.GREEN + f"ASN           : {results['asn']}")
        print(Fore.GREEN + f"ASN Desc      : {results['asn_description']}")
        print(Fore.GREEN + f"Country       : {results['asn_country_code']}")
        print(Fore.GREEN + f"Org           : {results['network']['name']}")
        print(Fore.GREEN + f"CIDR          : {results['network']['cidr']}")
    except Exception as e:
        print(Fore.RED + f"[!] Gagal ambil info IP: {e}")
