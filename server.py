from flask import Flask, request, send_from_directory, render_template_string
import os
import subprocess
from datetime import datetime

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = Flask(__name__)

# Fayl hajmini formatlash
def format_file_size(size):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} TB"

# Fayl ma'lumotlari
def get_file_info(filepath):
    stat = os.stat(filepath)
    size = format_file_size(stat.st_size)
    modified = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M')
    return size, modified

# Asosiy sahifa va yuklash
@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        f = request.files.get("file")
        if f:
            filepath = os.path.join(UPLOAD_DIR, f.filename)
            f.save(filepath)
            message = f"'{f.filename}' muvaffaqiyatli yuklandi!"
        else:
            message = "Fayl topilmadi!"

    files = os.listdir(UPLOAD_DIR)
    file_infos = [(f, *get_file_info(os.path.join(UPLOAD_DIR, f))) for f in files]

    html = '''
    <!DOCTYPE html>
    <html lang="uz">
    <head>
        <meta charset="UTF-8">
        <title>Fayl Server</title>
    </head>
    <body>
        <h1>Fayl Server</h1>
        <p>{{ message }}</p>
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file" required>
            <button type="submit">Yuklash</button>
        </form>
        <h2>Yuklangan fayllar</h2>
        <ul>
        {% for f, size, modified in file_infos %}
            <li>
                {{ f }} ({{ size }}, {{ modified }}) 
                {% if f.endswith('.py') %}
                    - <a href="/run/{{ f }}">Run</a>
                {% endif %}
                - <a href="/files/{{ f }}">Download</a>
            </li>
        {% endfor %}
        </ul>
    </body>
    </html>
    '''
    return render_template_string(html, file_infos=file_infos, message=message)

# Faylni yuklab olish
@app.route("/files/<filename>")
def download_file(filename):
    return send_from_directory(UPLOAD_DIR, filename, as_attachment=True)

# Python faylini ishga tushirish
@app.route("/run/<filename>")
def run_file(filename):
    filepath = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(filepath) or not filename.endswith(".py"):
        return "Fayl topilmadi yoki .py emas!"

    try:
        result = subprocess.run(
            ["python3", filepath],
            capture_output=True,
            text=True,
            timeout=60
        )
        output = result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        output = "Vaqt tugadi: fayl 60 soniyadan ko‘p ishladi."
    except Exception as e:
        output = f"Xato yuz berdi:\n{str(e)}"

    html = f'''
    <h1>{filename} natijasi</h1>
    <pre>{output}</pre>
    <a href="/">Orqaga</a>
    '''
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
