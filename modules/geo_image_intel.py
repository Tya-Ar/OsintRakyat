from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from colorama import Fore
import os

def get_exif_data(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if not exif_data:
            return {}

        exif_dict = {}
        for tag, value in exif_data.items():
            decoded = TAGS.get(tag, tag)
            exif_dict[decoded] = value
        return exif_dict
    except Exception as e:
        print(Fore.RED + f"[!] Gagal membaca EXIF: {e}")
        return {}

def get_geolocation(exif_data):
    gps_info = exif_data.get("GPSInfo", None)
    if not gps_info:
        return None

    def convert_to_degrees(value):
        d = value[0][0] / value[0][1]
        m = value[1][0] / value[1][1]
        s = value[2][0] / value[2][1]
        return d + (m / 60.0) + (s / 3600.0)

    try:
        lat = convert_to_degrees(gps_info[2])
        if gps_info[1] == 'S':
            lat = -lat

        lon = convert_to_degrees(gps_info[4])
        if gps_info[3] == 'W':
            lon = -lon

        return (lat, lon)
    except:
        return None

def analyze_image(image_path):
    print(Fore.YELLOW + f"\n📸 Menganalisis metadata dari file: {image_path}")

    if not os.path.exists(image_path):
        print(Fore.RED + "[!] File tidak ditemukan.")
        return

    exif = get_exif_data(image_path)
    if not exif:
        print(Fore.RED + "[!] Tidak ada data EXIF.")
        return

    print(Fore.CYAN + "\n=== Informasi EXIF ===")
    for tag in ['DateTime', 'Model', 'Make', 'Software']:
        value = exif.get(tag, None)
        if value:
            print(Fore.GREEN + f"{tag:<12}: {value}")

    geo = get_geolocation(exif)
    if geo:
        lat, lon = geo
        print(Fore.CYAN + "\n=== Lokasi Ditemukan ===")
        print(Fore.GREEN + f"Latitude      : {lat}")
        print(Fore.GREEN + f"Longitude     : {lon}")
        print(Fore.BLUE  + f"[🗺️ Google Maps] https://maps.google.com/?q={lat},{lon}")
    else:
        print(Fore.YELLOW + "[!] Lokasi tidak ditemukan dalam EXIF.")
