import os

def check_domain(domain):
    print(f"\n[🌐] WHOIS & DNS untuk: {domain}")
    os.system(f"whois {domain}")
    os.system(f"nslookup {domain}")
