import requests
from bs4 import BeautifulSoup


link = 'https://ya.ru/'
responce = requests.get(link).text
# with open('1.html', 'w', encoding='utf-8') as file:
#     file.write(responce)
#     file.close()
soup = BeautifulSoup(responce, 'lxml')
# block = soup.find('div', id='tool_padding')
# check_js = block.find('div', id='javascript_check')
# result_js = check_js.find_all('span')[1].text
blcok = soup.find('div', 'aria-label')
print(blcok)