import requests
from bs4 import BeautifulSoup


link = 'https://browser-info.ru/'
responce = requests.get(link).text
# with open('1.html', 'w', encoding='utf-8') as file:
#     file.write(responce)
#     file.close()
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', id='tool_padding')
check_js = block.find('div', id='javascript_check')
result_js = check_js.find_all('span')[1].text
print('JS {}'.format(result_js))