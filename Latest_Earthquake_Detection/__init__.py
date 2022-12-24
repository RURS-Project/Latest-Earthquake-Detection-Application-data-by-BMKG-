import requests
from bs4 import BeautifulSoup


# Modul Python yang akan dibaca pertama kali saat membaca Packages
def extraction_data():
    """
    Tanggal : 22 Desember 2022, 04:18:28 WIB
    Magnitudo : 3.8
    Kedalaman : 5 km
    Lokasi : LS = 6.99 LS - BT = 108.48
    Pusat gempa : Pusat gempa berada di darat 1 km BaratDaya Kab. Kuningan
    Dirasakan : Dirasakan (Skala MMI): III Kuningan, II - III Cirebon, II - III Majalengka
    """
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        print(content.text)
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('span', {'class': 'waktu'})
        re
        waktu = result.text.split(', ')[1]
        tanggal = result.text.split(', ')[0]


        hasil = dict()
        hasil['tanggal'] = tanggal  #'22 Desember 2022,
        hasil['waktu'] = waktu # 04:18:28 WIB'
        hasil['Magnitudo'] = '3.8'
        hasil['Kedalaman'] = '5 km'
        hasil['Lokasi'] = {'ls' : 6.99, 'bt' : 108.48}
        hasil['Pusat'] = 'Pusat gempa berada di darat 1 km BaratDaya Kab. Kuningan'
        hasil['Dirasakan'] = 'Dirasakan (Skala MMI): III Kuningan, II - III Cirebon, II - III Majalengka'
        return hasil
    else:
        return None

def show_data(result):
    if result is None:
        print("Couldn't find the latest earthquake data")
        return
    print('Latest Earthquake by BMKG')
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['Magnitudo']}")
    print(f"Lokasi : LS= {result['Lokasi']['ls']}, BT= {result['Lokasi']['bt']}")
    print(f"Pusat : {result['Pusat']}")
    print(f"Dirasakan : {result['Dirasakan']}")
