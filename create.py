import requests
endpoint = " http://127.0.0.1:8000/products/"
data = {
    'title': 'H5',
    'price': 45,
    'content': 'content h5'
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())