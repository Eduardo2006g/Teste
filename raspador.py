import requests
from bs4 import BeautifulSoup

'Cria link pro site que eu quero raspar'
link = "https://www.google.com/search?q=cotacao+dolar"
requisicao = requests.get(link)
print(requisicao)
#print(requisicao.text)
site = BeautifulSoup(requisicao.text, "html.parser")
print(site.prettify())

titulo = site.find("title")
print (titulo)

pesquisa = site.find_all("input")
print (pesquisa[2])
