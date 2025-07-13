# 🕵️ OSINT CLI Rakyat v1.0

Tool investigasi OSINT berbasis CLI (Command Line Interface) untuk pengguna Termux, Linux, dan edukasi publik.

## 🎯 Fitur Utama
- 🔍 Cek username di GitHub, IG, TikTok, Twitter
- 🔐 Cek email yang bocor via HaveIBeenPwned
- 🌐 Cek WHOIS dan DNS suatu domain
- 📡 Scan port dasar dari target website/IP
- 🖼️ Baca metadata (EXIF) dari foto

## 🚀 Instalasi di Termux
```bash
pkg install python git nmap whois dnsutils
pip install -r requirements.txt
python main.py
