from selenium import webdriver

# Here chrome webdriver is used
driver = webdriver.Chrome()

# URL of the website
url = "https://spb.rt.ru/"

# Opening the URL
driver.get(url)

# Getting current URL
get_url = driver.current_url

# Printing the URL
print(get_url)