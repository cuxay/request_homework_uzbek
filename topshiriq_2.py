import requests

"""
https://example.com sahifasiga GET so'rov yuboring
va javob matnini (text) konsolga chiqaring.
"""
url = 'https://example.com'
r = requests.get(url)
print(r.text)