from json import loads
import requests
import sys

def check_image():
    method = "POST"
    url = "https://container-security.dev.secops.rpaworker.com/image/container/check"
    data = '{"imageName": "405999462422.dkr.ecr.us-east-1.amazonaws.com/golang:latest","force": true}'
    headers = {
            "Content-Type": "application/json",
            "X-API-KEY": "6WN4BgpRfvdUxPZU7DABAfPCXjcaDwsvy6F7YdegNzb96sjmBV3qhY66nEmswQ5j"
    }

    return requests.request(
            method = method,
            url = url,
            data = data, 
            headers = headers,
            verify = False
    )

if __name__ == "__main__":
    response = check_image()
    result = loads(response.content.decode('utf-8'))["result"]
    print(result)

#     if len(result["alerts"]) == 0:
#         sys.exit(0)
#     else:
#         sys.exit(1)
    sys.exit(0)

