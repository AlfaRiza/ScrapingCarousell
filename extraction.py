import bs4
import requests
import csv

url = 'https://id.carousell.com/carousell_id'

contents = requests.get(url)

response = bs4.BeautifulSoup(contents.text, 'html.parser')

data = response.find('div', attrs={'class': 'D_apq D_eZ M_gF D_fb M_gH'})


datas = data.findAll('div', attrs={'class': 'D_jg', 'class': 'D_qq', 'class': 'D_qv'})
    # print(datas)

file = open('hasil.csv', 'w', newline='')
writer = csv.writer(file)
headers = ['Judul', 'Harga', 'Likes']
writer.writerow(headers)
for obj in datas:
    judul = obj.find('p', attrs={'class': "D_bN M_aT D_aP M_aC D_bO M_aU D_bR M_aX D_bT M_aZ D_bW M_bc "
                                                       "D_bZ M_bg D_bK"}).text
    harga = obj.find('p', attrs={'class': 'D_bN M_aT D_aP M_aC D_bO M_aU D_bR M_aX D_bT M_aZ D_bW M_bc '
                                                       'D_bY M_bf D_bJ'}).text
    like = obj.find('span', attrs={'class': 'D_bN M_aT D_aP M_aC D_bO M_aU D_bR M_aX D_bU M_ba D_bW '
                                                      'M_bc D_bY M_bf D_bK'}).text
    file = open('hasil.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow([judul, harga, like])
    file.close()

