import requests
import argparse
import json

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


def getstatus(IPaddress):
    endpoint_url = "http://"+IPaddress+":8080/getstatus"
    json_response = fetch_json_from_endpoint(endpoint_url)
    if json_response:
        print("RAW JSON Response: ",json_response)
        if (json_response["SystemRunning"]):
           print("System Running: YES")
           print("Temperatures: Sensor-Temp:",json_response["SensorTemp"],
                 " OnPremiseUnit: CPU ",json_response["SystemCPUTemp"]," GPU ",json_response["SystemGPUTemp"])
        else:
           print("System Running: NO")

    endpoint_url = "http://"+IPaddress+":8080/getversion"
    json_response = fetch_json_from_endpoint(endpoint_url)
    if json_response:
        print("RAW JSON Response: ",json_response)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hello Blindsensor connect to the Blindsensor compute unit and get its status")
    parser.add_argument('--ipAddress', type=str, default='', required=True, help='IP Address of compute unit')
    args = parser.parse_args() 
    getstatus(args.ipAddress)

