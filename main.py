import bs4
import requests
from bs4 import BeautifulSoup

url = 'https://id.carousell.com/carousell_id'

contents = requests.get(url)

response = bs4.BeautifulSoup(contents.text, 'html.parser')

data = response.findAll('div', attrs={'class': 'D_apq D_eZ M_gF D_fb M_gH'})

for item in data:
    datas = item.findAll('div', attrs={'class': 'D_jg', 'class': 'D_qq', 'class': 'D_qv'})
    print(datas)
    for obj in datas:
        print('Title: ', obj.find('p', attrs={'class': "D_bN M_aT D_aP M_aC D_bO M_aU D_bR M_aX D_bT M_aZ D_bW M_bc "
                                                       "D_bZ M_bg D_bK"}).text)
        print('Harga: ', obj.find('p', attrs={'class': 'D_bN M_aT D_aP M_aC D_bO M_aU D_bR M_aX D_bT M_aZ D_bW M_bc '
                                                       'D_bY M_bf D_bJ'}).text)
        descs = obj.findAll('p', attrs={'class': 'D_bN M_aT D_aP M_aC D_bO M_aU D_bR M_aX D_bT M_aZ D_bW '
                                                           'M_bc D_bY M_bf D_bK'})
        for desc in descs:
            print('Deskripsi: ', desc.text)
        # print('Keterangan: ', obj.find('p', attrs={'class': 'D_bN M_aT D_aP M_aC D_bO M_aU D_bR M_aX D_bT M_aZ D_bW '
        #                                                     'M_bc D_bY M_bf D_bK'}).text)
        print('likes: ', obj.find('span', attrs={'class': 'D_bN M_aT D_aP M_aC D_bO M_aU D_bR M_aX D_bU M_ba D_bW '
                                                          'M_bc D_bY M_bf D_bK'}).text)
        print('\n')

