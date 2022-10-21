import requests
import json
import httpcore
BASE_URL = 'https://blockchain.info/ticker'
response = httpcore.request("GET", BASE_URL)

print(response)
print(response.status)

print(response.headers)

print(type(response.content))
# if response.content is "TWD":
#     print(response.content)

# response = requests.get(BASE_URL)#, params={'base:'})

# print(response.json())

# {
#   "base": USD,
#   "date": "2018-02-13",
#   "rates": {
#      "CAD": 1.260046,
#      "CHF": 0.933058,
#      "EUR": 0.806942,
#      "GBP": 0.719154,
#      [170 world currencies]
#   }
# }