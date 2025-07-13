import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from colorama import Fore

def lookup_number(number):
    print(Fore.YELLOW + f"\n📱 Menganalisis nomor: {number}")
    try:
        parsed_number = phonenumbers.parse(number)

        # Validasi
        if not phonenumbers.is_possible_number(parsed_number):
            print(Fore.RED + "[!] Format nomor tidak valid.")
            return

        # Informasi dasar
        negara = geocoder.description_for_number(parsed_number, "id")
        operator = carrier.name_for_number(parsed_number, "id")
        zona = timezone.time_zones_for_number(parsed_number)

        print(Fore.CYAN + "\n=== INFO NOMOR ===")
        print(Fore.GREEN + f"Negara        : {negara}")
        print(Fore.GREEN + f"Operator      : {operator}")
        print(Fore.GREEN + f"Zona Waktu    : {', '.join(zona)}")

    except Exception as e:
        print(Fore.RED + f"[!] Gagal memproses nomor: {e}")
