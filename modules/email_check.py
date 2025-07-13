import requests

def check_email(email):
    print(f"\n[🔐] Mengecek email bocor untuk: {email}")
    try:
        url = f"https://haveibeenpwned.com/unifiedsearch/{email}"
        res = requests.get(url, headers={"User-Agent": "osint-cli"})
        if "Breach" in res.text:
            print("⚠️ Email ini ditemukan dalam kebocoran data!")
        else:
            print("✅ Email ini aman atau tidak ditemukan dalam breach publik.")
    except Exception as e:
        print(f"⚠️ Gagal mengakses HaveIBeenPwned: {e}")
