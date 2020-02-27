from json import loads
import requests
import sys

# Globals
url = "JUNK"
api_key = "JUNK"

def check_image(image_name):
	#---------------------------------------------------------------
	# Call Check API
	#---------------------------------------------------------------
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

	#---------------------------------------------------------------
	# Grab "result" from the response
	#---------------------------------------------------------------
	result = loads(response.content.decode('utf-8'))["result"]
	print(result)

	#---------------------------------------------------------------
	# If NO alerts, return True (PASS); Else, return False (FAIL)
	#---------------------------------------------------------------
	return len(result["alerts"]) == 0

if __name__ == "__main__":
	#---------------------------------------------------------------
	# Validate with Check API
	#---------------------------------------------------------------
	# image_name = "405999462422.dkr.ecr.us-east-1.amazonaws.com/golang:latest"
	
	#---------------------------------------------------------------
	# If NOT no alerts (Failed), exit with code 1
	#---------------------------------------------------------------
	if not check_image(image_name):
		print("Check Failed!")
		sys.exit(1)

	#---------------------------------------------------------------
	# Continue if Check Passed
	#---------------------------------------------------------------
	print("Check Passed!")
	sys.exit(0)
