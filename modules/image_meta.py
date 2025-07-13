from PIL import Image
from PIL.ExifTags import TAGS

def read_metadata(file_path):
    try:
        image = Image.open(file_path)
        info = image._getexif()
        if info is None:
            print("❌ Metadata tidak tersedia.")
            return
        print("\n[📸] Metadata:")
        for tag, value in info.items():
            tag_name = TAGS.get(tag, tag)
            print(f"{tag_name:25}: {value}")
    except Exception as e:
        print(f"❌ Gagal membaca metadata: {e}")
