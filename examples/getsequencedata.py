import requests
import argparse
import json
import time
from PIL import Image

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


def getseqdata(IPaddress, getsnapshot, numsecs):
    if getsnapshot:
        endpoint_url = "http://"+IPaddress+":8080/getsnapshot"
        response = requests.get(endpoint_url)
        response.raise_for_status()
        if 'image/jpeg' in response.headers.get('content-type',''):
           with open('image.jpg','wb') as f:
              f.write(response.content)
        else:
           # need to wait because we can not hammer for snapshots
           time.sleep(30)
           response = requests.get(endpoint_url)
           response.raise_for_status()
           if 'image/jpeg' in response.headers.get('content-type',''):
              with open('image.jpg','wb') as f:
                 f.write(response.content)

    endpoint_url = "http://"+IPaddress+":8080/getlastnseconds?secs="+str(numsecs)
    json_response = fetch_json_from_endpoint(endpoint_url)
    if json_response:
        print("RAW JSON Response: ",json_response)
        print("Number of people in sequence: ",json_response['total'])
        if (json_response['total'] > 0):
           print("Listing data for each person")
           for n in range(len(json_response['people'])):
              person = json_response['people'][n]
              # put your real data parsing code here here for now
              # we just going to print out the json structure
              print(person)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get sequence data of numsecs length")
    parser.add_argument('--ipAddress', type=str, default='', required=True, help='IP Address of compute unit')
    parser.add_argument('--getsnapshot' ,type=bool, default=False, help='Should it get a snapshot first?')
    parser.add_argument('--numsecs', type=int, default=10, help='Length of sequence in seconds')
    args = parser.parse_args() 
    getseqdata(args.ipAddress,args.getsnapshot,args.numsecs)

