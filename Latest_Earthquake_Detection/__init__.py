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
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None
        for res in result:
            print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['Magnitudo'] = magnitudo
        hasil['Kedalaman'] = kedalaman
        hasil['Koordinat'] = {'ls' : ls, 'bt' : bt}
        hasil['Lokasi'] = lokasi
        hasil['Dirasakan'] = dirasakan
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
    print(f"Kedalaman : {result['Kedalaman']}")
    print(f"Koordinat : {result['Koordinat']['ls']}, {result['Koordinat']['bt']}")
    print(f"Lokasi : {result['Lokasi']}")
    print(f"Dirasakan : {result['Dirasakan']}")
