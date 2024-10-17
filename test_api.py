import requests

posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
assert len(posts) == 100