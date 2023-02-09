from external.Inventory import Inventory
import requests
import json


def Order(obj):
	headers = {'Content-Type':'application/json'}
	ip = "http://localhost:"
	port = "### this should be changed ###"
	target = "/inventories"
	address = ip+port+target
	data = json.dumps(obj.__dict__)
	response = requests.post(address,data=data, headers=headers)
	response = response.content.decode('utf8').replace("'", '"')
	'''
    LOGIC GOES HERE
    '''

	return response


