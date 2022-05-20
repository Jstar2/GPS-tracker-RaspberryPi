from gps3 import gps3
from ubidots import ApiClient
import time
import requests

gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()

token = ("") # <-------------------------------------------------------------------------------Make sure you add your token Id here....
label = ("RaspberryPi_TrackerData")
variable_1 = ("Position")


for new_data in gps_socket:
    if new_data:        
        #raw data collection
        data_stream.unpack(new_data)
        longitude = (data_stream.TPV['lon'])
        latitude = (data_stream.TPV['lat'])
        payload = {variable_1: {"value": 1, "context": {"lat": latitude, "lng": longitude}}}
        
        #printing data to console
        print (f'\nLongitude : {longitude}W\nLatitude  : {latitude}N')
        
        #request header
        url = ("http://industrial.api.ubidots.com")
        url = "{}/api/v1.6/devices/{}".format(url, label)
        headers = {"X-Auth-Token": token, "Content-Type": "application/json"}
 
        #making request
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code       
        time.sleep(1)   
