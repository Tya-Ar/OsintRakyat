import os
import time
import pyfiglet
from colorama import Fore, init

# Import modul OSINT
from modules import (
    username_hunter,
    email_breach_advanced,
    domain_deep_lookup,
    geo_image_intel,
    phone_lookup,
    pdf_report
)

init(autoreset=True)

def show_banner():
    os.system("clear" if os.name == "posix" else "cls")
    banner = pyfiglet.figlet_format("OSINT CLI")
    print(Fore.GREEN + banner)
    print(Fore.CYAN + "        RAKYAT PRO v1.0")
    print(Fore.YELLOW + "      Created by MR057 (Rizal)\n")
    time.sleep(1)

def menu():
    print(Fore.BLUE + "[ Menu OSINT CLI Rakyat PRO ]")
    print("1. Cari Username")
    print("2. Cek Email Bocor")
    print("3. Analisa Domain")
    print("4. Metadata Foto & Lokasi")
    print("5. Cek Nomor HP")
    print("6. Export Laporan PDF")
    print("0. Keluar")
    choice = input("\nPilih opsi: ")

    if choice == "1":
        username = input("Masukkan username: ")
        username_hunter.search_username(username)
    elif choice == "2":
        email = input("Masukkan email: ")
        email_breach_advanced.check_email_breach(email)
    elif choice == "3":
        domain = input("Masukkan domain/IP: ")
        domain_deep_lookup.analyze_domain(domain)
    elif choice == "4":
        path = input("Masukkan path foto: ")
        geo_image_intel.analyze_image(path)
    elif choice == "5":
        number = input("Masukkan nomor HP (dengan kode negara): ")
        phone_lookup.lookup_number(number)
    elif choice == "6":
        pdf_report.export_pdf()
    elif choice == "0":
        print("Keluar...")
        exit()
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    show_banner()
    while True:
        menu()
        input(Fore.MAGENTA + "\nTekan Enter untuk kembali ke menu...")
