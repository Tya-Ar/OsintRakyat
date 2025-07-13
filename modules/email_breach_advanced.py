import requests
from colorama import Fore

def check_email_breach(email):
    print(Fore.YELLOW + f"\n🔐 Mengecek kebocoran email: {email}")

    headers = {
        "User-Agent": "OSINT-CLI-Rakyat/1.0",
    }

    try:
        url = f"https://haveibeenpwned.com/unifiedsearch/{email}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200 and "Breach" in response.text:
            print(Fore.RED + "\n⚠️ Email ditemukan dalam kebocoran publik!")
            # Data lengkap hanya untuk API berbayar, jadi tampilkan sederhana
            print(Fore.CYAN + "Gunakan API resmi HaveIBeenPwned untuk data lebih rinci.")
        elif response.status_code == 404:
            print(Fore.GREEN + "✅ Email ini tidak ditemukan dalam kebocoran.")
        else:
            print(Fore.YELLOW + f"⚠️ Status tidak dikenali: {response.status_code}")
    except Exception as e:
        print(Fore.RED + f"❌ Gagal mengakses API: {e}")
