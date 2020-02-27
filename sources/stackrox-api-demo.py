from json import loads
import requests
import sys

# Globals
url = "https://container-security.dev.secops.rpaworker.com/image/container/check"
api_key = "6WN4BgpRfvdUxPZU7DABAfPCXjcaDwsvy6F7YdegNzb96sjmBV3qhY66nEmswQ5j"

def check_image(image_name):
	method = "POST"
	data = '{"imageName": "' + image_name + '","force": true}'

	response = requests.request(
		method = method,
		url = url,
		data = data, 
		headers = {
			"Content-Type": "application/json",
			"X-API-KEY": api_key
		},
		verify = False
	)

	result = loads(response.content.decode('utf-8'))["result"]
	print(result)

	return (len(result["alerts"]) == 0

if __name__ == "__main__":
	#---------------------------------------------------------------
	# Validate with Check API
	#---------------------------------------------------------------
	image_name = "405999462422.dkr.ecr.us-east-1.amazonaws.com/golang:latest"
	
	if not check_image(image_name):
		print("Check Failed!")
		sys.exit(1)

	#---------------------------------------------------------------
	# Continue if Check Passed
	#---------------------------------------------------------------
	print("Check Passed!")
	sys.exit(0)

