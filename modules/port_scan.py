import os

def scan_port(target):
    print(f"\n[🔎] Scan port untuk: {target}")
    os.system(f"nmap -Pn -F {target}")
