import requests
import json
base_url = 'https://postcodes.io/'
path = 'postcodes/'
headers = {'Content-type': 'application/json'}


def find_nhs_location(list_of_postcodes):
    dict_post_codes = {
        'postcodes': list_of_postcodes
    }
    json_body = json.dumps(dict_post_codes)
    postcodes_post_response = requests.post(base_url + path, data=json_body, headers=headers)
    results = postcodes_post_response.json()['result']
    counter = 1
    for request in results:
        print(f"{counter} - Postcode: {request['result']['postcode']}, with NHS location at: {request['result']['nhs_ha']}")
        counter += 1

def find_long_and_lat(list_of_postcodes):
    dict_post_codes = {
        'postcodes': list_of_postcodes
    }
    json_body = json.dumps(dict_post_codes)
    postcodes_post_response = requests.post(base_url + path, data=json_body, headers=headers)
    results = postcodes_post_response.json()['result']
    counter = 1
    for request in results:
        print(f"{counter} - Postcode: {request['result']['postcode']}, with longitude: {request['result']['longitude']} and "
              f"latitude: {request['result']['latitude']} ")
        counter += 1


find_nhs_location(['ec2y5as', 'w139qu', 'gu2 8ut'])
# find_long_and_lat(['ec2y5as', 'w13 9qu'])