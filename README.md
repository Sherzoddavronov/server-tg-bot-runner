# server-tg-bot-runner
# Fayl Server / File Server (Flask)

| 🇺🇿 O‘zbekcha | 🇬🇧 English |
|---------------|------------|
| Bu loyiha Python + Flask yordamida ishlaydigan oddiy fayl serverdir. Siz ushbu server orqali fayllarni yuklab, ko‘rib, `.py` fayllarni ishga tushirishingiz mumkin. | This project is a simple file server built with Python + Flask. You can upload files, view uploaded files, and run `.py` files on this server. |

---

## Talablar / Requirements

| 🇺🇿 O‘zbekcha | 🇬🇧 English |
|---------------|------------|
| Python 3.12 yoki undan yuqori | Python 3.12 or higher |
| Flask | Flask |

---

## O‘rnatish / Installation

| 🇺🇿 O‘zbekcha | 🇬🇧 English |
|---------------|------------|
| 1. Loyihani klonlang: <br>`git clone <your-repo-url>`<br>`cd <repo-folder>` | 1. Clone the repository: <br>`git clone <your-repo-url>`<br>`cd <repo-folder>` |
| 2. Virtual muhit yaratish: <br>`python -m venv venv` | 2. Create a virtual environment: <br>`python -m venv venv` |
| 3. Virtual muhitni yoqish: <br>`source venv/bin/activate` (Linux/macOS)<br>`venv\Scripts\activate` (Windows) | 3. Activate the virtual environment: <br>`source venv/bin/activate` (Linux/macOS)<br>`venv\Scripts\activate` (Windows) |
| 4. Zarur paketlarni o‘rnatish: <br>`pip install --upgrade pip`<br>`pip install flask` | 4. Install required packages: <br>`pip install --upgrade pip`<br>`pip install flask` |

---

## Ishga tushirish / Run the server

| 🇺🇿 O‘zbekcha | 🇬🇧 English |
|---------------|------------|
| `python server.py`<br>Brauzerda oching: [http://localhost:8000](http://localhost:8000) | `python server.py`<br>Open in browser: [http://localhost:8000](http://localhost:8000) |

---

## Funksiyalar / Features

| 🇺🇿 O‘zbekcha | 🇬🇧 English |
|---------------|------------|
| Fayl yuklash (`.txt`, `.py`, `.jpg`, va boshqalar) | Upload files (`.txt`, `.py`, `.jpg`, etc.) |
| Yuklangan fayllar ro‘yxati | View uploaded files |
| `.py` fayllarni ishga tushirish va natijani ko‘rish | Run `.py` files and see output |
| Faylni yuklab olish | Download files |

---

## Xavfsizlik Eslatmalari / Security Notes

| 🇺🇿 O‘zbekcha | 🇬🇧 English |
|---------------|------------|
| `.py` fayllarni ishga tushirish xavfli bo‘lishi mumkin. Foydalanuvchi zararli kod yozsa, serverga hujum qilishi mumkin. | Running `.py` files can be dangerous. Malicious code can compromise the server. |
| Real ishlab chiqarishda, izolyatsiya (container / sandbox) ishlatish tavsiya qilinadi. | In production, use containerization / sandboxing for safety. |

---

## Litsenziya / License

| 🇺🇿 O‘zbekcha | 🇬🇧 English |
|---------------|------------|
| MIT Litsenziya | MIT License |
