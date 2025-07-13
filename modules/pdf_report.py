from fpdf import FPDF
from colorama import Fore
import os
from datetime import datetime

def export_pdf():
    print(Fore.YELLOW + "\n📝 Membuat laporan OSINT dalam format PDF...")

    try:
        laporan_folder = "laporan"
        if not os.path.exists(laporan_folder):
            os.makedirs(laporan_folder)

        now = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        filename = f"{laporan_folder}/laporan_osint_{now}.pdf"

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Header
        pdf.set_font("Arial", "B", size=16)
        pdf.cell(200, 10, txt="LAPORAN OSINT CLI RAKYAT PRO", ln=True, align='C')
        pdf.set_font("Arial", size=10)
        pdf.cell(200, 10, txt=f"Generated: {now}", ln=True, align='C')
        pdf.ln(10)

        # Contoh isi (statik untuk versi awal)
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="[Contoh] Username ditemukan: rizal057", ln=True)
        pdf.cell(200, 10, txt="[Contoh] Domain terdaftar: ladangcuan.com", ln=True)
        pdf.cell(200, 10, txt="[Contoh] Lokasi dari foto: -6.2017, 106.8011", ln=True)
        pdf.cell(200, 10, txt="[Contoh] Email bocor: rizal@gmail.com", ln=True)

        pdf.output(filename)
        print(Fore.GREEN + f"✅ Laporan berhasil disimpan: {filename}")

    except Exception as e:
        print(Fore.RED + f"[!] Gagal membuat laporan PDF: {e}")
