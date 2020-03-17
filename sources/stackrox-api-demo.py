from json import loads
import requests
import sys

# Globals
url = "https://container-security.dev.secops.rpaworker.com/image/container/check"
api_key = "6WN4BgpRfvdUxPZU7DABAfPCXjcaDwsvy6F7YdegNzb96sjmBV3qhY66nEmswQ5j"

def check_image(image_name):
	#---------------------------------------------------------------
	# Call Check API
	#---------------------------------------------------------------
	method = "POST"
	data = '{"imageName": "' + image_name + '"}'

	response = requests.request(
		method = method,
		url = url,
 		data = data, 
 		headers = {
 			"Content-Type": "application/json",
 			"X-API-KEY": api_key
 		}
	)
	
	#---------------------------------------------------------------
	# Grab "result" from the response
	#---------------------------------------------------------------
	result = loads(response.content.decode('utf-8'))["result"]

	#---------------------------------------------------------------
	# If check_status is PASS, return True (PASS); Else, return False (FAIL)
	#---------------------------------------------------------------
	return result["check_status"] == "PASS"


if __name__ == "__main__":
	#---------------------------------------------------------------
	# Validate with Check API
	#---------------------------------------------------------------
	image_name = "405999462422.dkr.ecr.us-east-1.amazonaws.com/golang:latest"
	
	#---------------------------------------------------------------
	# If the check_image NOT PASSed, exit with code 1 
	#---------------------------------------------------------------
	if not check_image(image_name):
		print("FAIL")
		sys.exit(1)

	#---------------------------------------------------------------
	# Continue if Check PASSed
	#---------------------------------------------------------------
	print("PASS")
	sys.exit(0)
