import os
from dotenv import load_dotenv
import random
import string


load_dotenv()
valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')
no_valid_email = os.getenv('1mailo4@mail.ru')
no_valid_password = os.getenv('1daorliar')



def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))