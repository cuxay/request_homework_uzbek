import requests

"""
3-topshiriqdagi JSON javobdan "title" maydonini
ajratib olib konsolga chiqaring.
"""
url ='https://jsonplaceholder.typicode.com/todos/1'
r = requests.get(url)
d = r.json()


print(d['title'])