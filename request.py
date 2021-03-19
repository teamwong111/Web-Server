  
import requests
parameters = {'q' : 'Python', 'client' : 'Firefox'}
response = requests.get('http://www.google.com/search', params=parameters)
print('actual URL:', response.url)


response = requests.get("http://aosabook.org/en/posa/introduction.html")
print('status code:', response.status_code)
print('content length:', response.headers['content-length'])
print(response.text)