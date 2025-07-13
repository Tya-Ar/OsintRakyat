import requests
from colorama import Fore
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key dari file .env

def lookup_number_advanced(phone_number):
    api_key = os.getenv("NUMVERIFY_API_KEY")
    if not api_key:
        print(Fore.RED + "[!] API key tidak ditemukan. Simpan di file .env sebagai NUMVERIFY_API_KEY.")
        return

    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}"

    print(Fore.YELLOW + f"\n📡 Memeriksa nomor dengan NumVerify: {phone_number}")
    
    try:
        response = requests.get(url)
        data = response.json()

        if not data.get("valid"):
            print(Fore.RED + "[✗] Nomor tidak valid.")
            return

        print(Fore.GREEN + "\n✅ Nomor valid dan ditemukan.\n")
        print(Fore.CYAN + "=== DETAIL NOMOR ===")
        print(Fore.GREEN + f"Negara         : {data.get('country_name')}")
        print(Fore.GREEN + f"Kode Negara    : +{data.get('country_code')}")
        print(Fore.GREEN + f"Lokasi         : {data.get('location') or 'Tidak tersedia'}")
        print(Fore.GREEN + f"Provider       : {data.get('carrier') or 'Tidak diketahui'}")
        print(Fore.GREEN + f"Tipe Layanan   : {data.get('line_type')}")
        print(Fore.GREEN + f"Format Lokal   : {data.get('local_format')}")
        print(Fore.GREEN + f"Format Internasional : {data.get('international_format')}")

    except Exception as e:
        print(Fore.RED + f"[!] Gagal mengakses API: {e}")
