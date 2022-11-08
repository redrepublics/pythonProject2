import os
from dotenv import load_dotenv
from api import PetFriends

load_dotenv()
valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')
pf = PetFriends()
