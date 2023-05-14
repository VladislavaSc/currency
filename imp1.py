import requests

response = requests.get('https://api.github.com')
print(response)
print(response.status_code)
print(dir(response))
print(response.content)

print(response.text)
print(response.content)

print(response.json())
