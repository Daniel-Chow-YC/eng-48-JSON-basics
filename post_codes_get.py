import requests
# Get Requests
# They do not have a body (JSON)
# They have a base url, path and arguments

base_url = 'https://postcodes.io/'
path = 'postcodes/'
arguments = 'e146gt'

request_response = requests.get(base_url + path + arguments)
print(request_response)

# Turning a request to dictionary ---> use .json()

dictionary_response = request_response.json()
print(dictionary_response)
print(dictionary_response['result']['postcode'])
