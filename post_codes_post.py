import requests
import json
import time

# Making a POST Request
# We need a path
# We need a json object to send
# Possibly headers, depending on the api

# creating the json
dictionary_post_codes = {
    'postcodes': ['EC2Y5AS', 'e146gt', 'CT12EH']
}

json_body = json.dumps(dictionary_post_codes)

#the url
base_url = 'https://postcodes.io/'
path = 'postcodes/'

# The headers
headers = {'Content-type': 'application/json'}

# making the request
postcodes_post_response = requests.post(base_url + path, data=json_body, headers=headers)
# print(postcodes_post_response.json())


response = postcodes_post_response.json()
# print(response)
results = response['result']

print(results[0]['result'])
print(results[1]['result'])
print(results[2]['result'])

# for request in results:
#     print(request['result']['nhs_ha'])

