import phonenumbers
from phonenumbers import carrier, geocoder, timezone, number_type
from phonenumbers.phonenumberutil import NumberType
from colorama import Fore

def lookup_number(number):
    print(Fore.YELLOW + f"\n📱 Menganalisis nomor: {number}")

    try:
        parsed = phonenumbers.parse(number)

        # Validasi
        if not phonenumbers.is_valid_number(parsed):
            print(Fore.RED + "[!] Nomor tidak valid secara internasional.")
        else:
            print(Fore.GREEN + "✅ Nomor valid secara global.")

        # Zona waktu
        zones = timezone.time_zones_for_number(parsed)
        # Negara asal
        country = geocoder.description_for_number(parsed, "id")
        # Operator seluler
        provider = carrier.name_for_number(parsed, "id")
        # Tipe nomor
        type_of_number = number_type(parsed)
        tipe_map = {
            NumberType.MOBILE: "Mobile",
            NumberType.FIXED_LINE: "Telepon Rumah",
            NumberType.FIXED_LINE_OR_MOBILE: "Telp Rumah / Mobile",
            NumberType.VOIP: "VoIP (Online)",
            NumberType.TOLL_FREE: "Bebas Pulsa",
            NumberType.PREMIUM_RATE: "Premium Rate",
            NumberType.UNKNOWN: "Tidak diketahui"
        }

        print(Fore.CYAN + "\n=== DETAIL NOMOR ===")
        print(Fore.GREEN + f"Negara        : {country}")
        print(Fore.GREEN + f"Operator      : {provider or 'Tidak diketahui'}")
        print(Fore.GREEN + f"Zona Waktu    : {', '.join(zones)}")
        print(Fore.GREEN + f"Tipe Nomor    : {tipe_map.get(type_of_number, 'Tidak diketahui')}")
        print(Fore.GREEN + f"Internasional : {phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")

    except Exception as e:
        print(Fore.RED + f"[!] Gagal memproses nomor: {e}")
