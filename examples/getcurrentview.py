import requests
import argparse
import json
import time
from PIL import Image,ImageDraw

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


def getcurrent(IPaddress, getsnapshot):
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

    endpoint_url = "http://"+IPaddress+":8080/getcurrent"
    json_response = fetch_json_from_endpoint(endpoint_url)
    if json_response:
        print("RAW JSON Response: ",json_response)
        if (json_response['data'] != None): 
           print("Got data")
           for n in range(len(json_response['data'])):
               print("Box: ",json_response['data'][n]['x1']," ",json_response['data'][n]['y1'],
                     " ",json_response['data'][n]['x2']," ",json_response['data'][n]['y2'])
               print("Propability: ",json_response['data'][n]['prob'])

           if getsnapshot:
              img = Image.open("image.jpg")
              draw = ImageDraw.Draw(img)
              for n in range(len(json_response['data'])):
                 x1 = int(float(json_response['data'][n]['x1']))
                 y1 = int(float(json_response['data'][n]['y1']))
                 x2 = int(float(json_response['data'][n]['x2']))
                 y2 = int(float(json_response['data'][n]['y2']))
                 shape =[x1,y1,x2,y2]
                 draw.rectangle(shape,outline="#ff00ff",width=4)
              img.save("image.jpg")
        else:
           print("Got no data")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get current detection")
    parser.add_argument('--ipAddress', type=str, default='', required=True, help='IP Address of compute unit')
    parser.add_argument('--getsnapshot' ,type=bool, default=False, help='Should it get a snapshot first?')
    args = parser.parse_args() 
    getcurrent(args.ipAddress,args.getsnapshot)

