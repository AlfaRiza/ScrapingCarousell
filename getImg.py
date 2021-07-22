import bs4
import requests

url = 'https://id.carousell.com/carousell_id'

contents = requests.get(url)

response = bs4.BeautifulSoup(contents.text, 'html.parser')

data = response.find('div', attrs={'class': 'D_apq D_eZ M_gF D_fb M_gH'})


datas = data.findAll('div', attrs={'class': 'D_jg', 'class': 'D_qq', 'class': 'D_qv'})
    # print(datas)
for obj in datas:
    judul = obj.find('p', attrs={'class': "D_bN M_aT D_aP M_aC D_bO M_aU D_bR M_aX D_bT M_aZ D_bW M_bc "
                                          "D_bZ M_bg D_bK"}).text
    image = obj.find('img', attrs={'class': 'D_bl', 'class': 'D_bi', 'class': 'D_tO'})['src']


    with open('images/' + judul + '.jpg', 'wb') as f:
        img = requests.get(image)
        f.write(img.content)