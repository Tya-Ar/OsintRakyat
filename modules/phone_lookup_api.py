import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NUMVERIFY_API_KEY")

def lookup_number(number):
    if not API_KEY:
        print("[!] API Key NumVerify belum diatur di .env")
        return

    url = f"http://apilayer.net/api/validate?access_key={API_KEY}&number={number}&format=1"
    
    try:
        response = requests.get(url)
        data = response.json()

        if "success" in data and data["success"] is False:
            print(f"[!] Error: {data['error']['info']}")
            return

        print("\n📞 Informasi Nomor Telepon:")
        print("-----------------------------")
        print(f"✅ Valid             : {data.get('valid')}")
        print(f"🌍 Negara           : {data.get('country_name')} ({data.get('country_code')})")
        print(f"📱 Operator         : {data.get('carrier')}")
        print(f"📞 Line Type        : {data.get('line_type')}")
        print(f"🌐 Format Intl      : {data.get('international_format')}")
        print(f"🔢 Format Lokal     : {data.get('local_format')}")
        print(f"📛 Location         : {data.get('location')}")
        print(f"📶 Kode Panggilan   : +{data.get('country_prefix')}")
        print("-----------------------------\n")

    except Exception as e:
        print(f"[!] Terjadi kesalahan: {e}")
