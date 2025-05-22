import requests

"""
https://example.com sahifasiga GET so'rov yuboring
va javob holatini (status_code) ekranga chiqaring.
"""
url = 'https://example.com'
r = requests.get(url)
print(r.status_code)