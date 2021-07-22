import bs4
import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/hasil-scraping')
def scraping():
    url = 'https://id.carousell.com/carousell_id'

    contents = requests.get(url)

    response = bs4.BeautifulSoup(contents.text, 'html.parser')

    data = response.find('div', attrs={'class': 'D_apq D_eZ M_gF D_fb M_gH'})

    datas = data.findAll('div', attrs={'class': 'D_jg', 'class': 'D_qq', 'class': 'D_qv'})

    return render_template('index.html', datas=datas)

if __name__ == '__main__':
    app.run(debug=True)
