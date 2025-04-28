import requests
from bs4 import BeautifulSoup
import pandas as pd

# Tambahan untuk PDF export
from fpdf import FPDF

# URL target
url = 'https://store.steampowered.com/search/?filter=topsellers'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Mengirim HTTP request
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')  # Ubah pakai html.parser kalau mau

# Cari semua elemen game
games = soup.find_all('a', class_='search_result_row')

data = []

for game in games:
    title = game.find('span', class_='title').text.strip()
    price_tag = game.find('div', class_='discount_final_price')
    
    # Kadang tidak ada harga (misal: pre-order atau free to play)
    price = price_tag.text.strip() if price_tag else "N/A"
    
    data.append({
        'Title': title,
        'Price': price
    })

# Buat dataframe
df = pd.DataFrame(data)

# -----------------------------
# Pilihan format export
print("\nPilih format untuk menyimpan hasil scraping:")
print("1. CSV")
print("2. Excel (XLSX)")
print("3. PDF")

choice = input("Masukkan pilihan (1/2/3): ").strip()

if choice == '1':
    df.to_csv('steam_games.csv', index=False)
    print("Data berhasil disimpan di steam_games.csv")
elif choice == '2':
    df.to_excel('steam_games.xlsx', index=False)
    print("Data berhasil disimpan di steam_games.xlsx")
elif choice == '3':
    # Membuat file PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Daftar Game Steam", ln=True, align='C')
    pdf.ln(10)

    for index, row in df.iterrows():
        pdf.cell(0, 10, f"{row['Title']} - {row['Price']}", ln=True)

    pdf.output("steam_games.pdf")
    print("Data berhasil disimpan di steam_games.pdf")
else:
    print("Pilihan tidak valid. Program dihentikan.")
