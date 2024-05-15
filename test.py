import requests

url = 'http://192.168.31.102:8090/api/qrcode/generate'

data = {
    'data': 'test'
}

response = requests.post(url=url, json=data)

print(response.content)

