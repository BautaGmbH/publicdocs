import requests
import argparse
import json
import time

def fetch_json_from_endpoint(url,params):
    try:
        headers = {'Accept' : 'application/json','Content-Type': 'application/json'}
        response = requests.get(url, headers=headers,params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        json_data = response.json()
        return json_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


def getandsetcurrent(IPaddress,newThresh):
    endpoint_url = "http://"+IPaddress+":8080/getsettings"
    json_response = fetch_json_from_endpoint(endpoint_url,None)
    if json_response:
        print("RAW JSON Response: ",json_response)
        endpoint_url = "http://"+IPaddress+":8080/setsettings"
        json_response['detector-threshold']=newThresh
        param_string = json.dumps(json_response)
        params = {'params' : param_string}
        response = fetch_json_from_endpoint(endpoint_url,params)
        print("Response: ",response)
        endpoint_url = "http://"+IPaddress+":8080/getsettings"
        new_response = fetch_json_from_endpoint(endpoint_url,None)
        print("NEW Settings: ",new_response)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get and set current settings")
    parser.add_argument('--ipAddress', type=str, default='', required=True, help='IP Address of compute unit')
    parser.add_argument('--detthreshold', type=str, default='0.3', help='Set a new detector threshold')
    args = parser.parse_args() 
    getandsetcurrent(args.ipAddress,args.detthreshold)

