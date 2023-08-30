import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

n = ToastNotifier()

url = 'https://www.bbc.com/portuguese'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
site = requests.get(url,headers=headers)
soup = BeautifulSoup(site.content,'html.parser')
#parser é transformar para formato html

artigo1 = soup.find(id="promo-portuguesearticlescx05kwvnyqno-text-1")
artigo2 = soup.find(id="promo-top-stories-portuguesearticlescjl9e0z6py9o-text-1")
artigo3 = soup.find(id="promo-top-stories-portuguesearticlescy0j40d0v3jo-text-4")
artigo1 = str(artigo1)
artigo2 = str(artigo2)
artigo3 = str(artigo3)

inicio = artigo1.find('>')
final = artigo1.find('</')
art1 = artigo1[inicio+1:final]

inicio = artigo2.find('>')
final = artigo2.find('</')
art2 = artigo2[inicio+1:final]

inicio = artigo3.find('>')
final = artigo3.find('</')
art3 = artigo3[inicio+1:final]

fim = 'Veja mais em: ' + url

mensagem = fim

n.show_toast("Notícias", mensagem, duration = 10,threaded=True)