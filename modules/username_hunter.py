import requests
from colorama import Fore

def search_username(username):
    print(Fore.YELLOW + f"\n🔍 Mencari username: {username}...\n")

    platforms = {
        "GitHub": f"https://github.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "TikTok": f"https://tiktok.com/@{username}",
        "Reddit": f"https://reddit.com/u/{username}",
        "Pinterest": f"https://pinterest.com/{username}",
        "Medium": f"https://medium.com/@{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Spotify": f"https://open.spotify.com/user/{username}",
        "Flickr": f"https://www.flickr.com/people/{username}",
        "GitLab": f"https://gitlab.com/{username}",
    }

    for platform, url in platforms.items():
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                print(Fore.GREEN + f"[✓] {platform:<12} → {url}")
            elif r.status_code == 404:
                print(Fore.RED + f"[✗] {platform:<12} → Tidak ditemukan")
            else:
                print(Fore.YELLOW + f"[!] {platform:<12} → Status: {r.status_code}")
        except Exception as e:
            print(Fore.RED + f"[!] {platform:<12} → Error: {e}")
