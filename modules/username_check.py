import requests

def check_username(username):
    platforms = {
        "GitHub": f"https://github.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "TikTok": f"https://tiktok.com/@{username}",
    }
    print(f"\n[🔍] Username: {username}")
    for name, url in platforms.items():
        try:
            r = requests.get(url, timeout=5)
            status = "✅ Found" if r.status_code == 200 else "❌ Not found"
            print(f"{name:<10}: {status} → {url}")
        except Exception as e:
            print(f"{name:<10}: ⚠️ Error ({e})")
