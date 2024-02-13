import requests
import argparse
import json
import time

def fetch_json_from_endpoint(url):
    try:
        headers = {'Accept' : 'application/json','Content-Type': 'application/json'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        json_data = response.json()
        return json_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


def restartdetector(IPaddress):
    endpoint_url = "http://"+IPaddress+":8080/restartdetector"
    json_response = fetch_json_from_endpoint(endpoint_url)
# wait a bit before checking status again needs sometime to restart
    time.sleep(6)
    endpoint_url = "http://"+IPaddress+":8080/getstatus"
    json_response = fetch_json_from_endpoint(endpoint_url)
    if (json_response["SystemRunning"]):
       print("System Running: YES")
    else:
       print("System Running: NO")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Restart the detection on the compute unit and return its new status")
    parser.add_argument('--ipAddress', type=str, default='', required=True, help='IP Address of compute unit')
    args = parser.parse_args() 
    restartdetector(args.ipAddress)

