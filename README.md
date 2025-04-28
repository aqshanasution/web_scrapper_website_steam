# 🎮 Steam Web Scraper

Project ini adalah sebuah **web scraper** sederhana yang mengambil data **judul** dan **harga** game dari website **Steam Store**!  
Setelah scraping, kamu bisa **memilih** format penyimpanan data: CSV 📄, Excel 📊, atau PDF 📜.

---

## 📦 Fitur

- 🔍 Scraping daftar game dari Steam (Top Sellers).
- 📄 Menyimpan hasil dalam format CSV.
- 📊 Menyimpan hasil dalam format Excel (.xlsx).
- 📜 Menyimpan hasil dalam format PDF.
- 🧩 Pilihan format output saat menjalankan program.

---

## 🚀 Cara Menjalankan

1. **Clone repository ini**:
    ```bash
    git clone https://github.com/username/repo-name.git
    cd repo-name
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Jalankan program**:
    ```bash
    python steam_scraper.py
    ```

4. **Pilih format penyimpanan** yang kamu inginkan:
    ```
    1. CSV
    2. Excel
    3. PDF
    ```

---

## 🛠️ Requirements

- `requests`
- `beautifulsoup4`
- `pandas`
- `fpdf` (hanya untuk output PDF)
- `openpyxl` (hanya untuk output Excel)

Kamu bisa install semua requirements sekaligus dengan:

```bash
pip install -r requirements.txt
