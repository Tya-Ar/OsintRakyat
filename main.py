import modules.username_check as uc
import modules.email_check as ec
import modules.domain_check as dc
import modules.port_scan as pc
import modules.image_meta as im

import pyfiglet
import time
import os
from colorama import init, Fore

init(autoreset=True)

def intro_matrix():
    os.system("clear" if os.name == "posix" else "cls")
    banner = pyfiglet.figlet_format("MR057")
    print(Fore.GREEN + banner)
    print(Fore.CYAN + "     ⚡ OSINT CLI RAKYAT v1.0 ⚡")
    print(Fore.YELLOW + "       Created by MR057 [Rizal]")
    print(Fore.MAGENTA + " ──▶ Investigasi Jejak Digital untuk Publik ◀──\n")
    time.sleep(1.5)

def menu():
    print("\n[ OSINT CLI RAKYAT ]")
    print("---------------------------")
    print("1. Cek Username")
    print("2. Cek Email Bocor")
    print("3. Cek Domain/IP")
    print("4. Scan Website (Port)")
    print("5. Metadata Foto (EXIF)")
    print("0. Keluar")
    pilihan = input("Pilih opsi: ")
    if pilihan == "1":
        uc.check_username(input("Username: "))
    elif pilihan == "2":
        ec.check_email(input("Email: "))
    elif pilihan == "3":
        dc.check_domain(input("Domain/IP: "))
    elif pilihan == "4":
        pc.scan_port(input("Domain/IP: "))
    elif pilihan == "5":
        im.read_metadata(input("Path ke foto: "))
    elif pilihan == "0":
        print("Selesai.")
        exit()
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    intro_matrix()
    while True:
        menu()
        input("\nTekan Enter untuk kembali ke menu…")
