import os
from dotenv import load_dotenv

load_dotenv()
valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')
no_valid_email = os.getenv('1mailo4@mail.ru')
no_valid_password = os.getenv('1daorliar')
