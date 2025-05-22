import requests

"""
https://jsonplaceholder.typicode.com/todos/1 sahifasiga so'rov yuboring
va JSON javobini chiqarib bering.
"""
url = 'https://jsonplaceholder.typicode.com/todos/1'
r = requests.get(url)
print(r.json())