import requests
from bs4 import BeautifulSoup


link = 'https://ya.ru/'
responce = requests.get(link).text
# with open('1.html', 'w', encoding='utf-8') as file:
#     file.write(responce)
#     file.close()
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', class="informers3")
print()