import json 
import requests 
from itertools import count 
email = "kornbot380@hotmail.com" # Getting the email account data of the user to checking the data of the user payload 
#Loading the data from the path of the token 
for i in count(0):
        #Step 0 checking the email account of the user to get the status payload 
        #Step 1 post request into the broker to run checking status 
        #Step 2 after detect status ON then running the json file input from the payload 
        #Step 3 after running the payload finish then change the status of the json input to status off 
        res = requests.get("https://roboreactor.com/Config_status") # Getting the remote config of the data 
        data_check = res.json() # Step 0 checking the email 
        status = data_check.get(email) # Getting the status payload for step 1 and step 2 
        try:
           if status != {}:
                if status.get("status") == "ON": # Checking the status 
                             # Sending the post request
                             res_config = requests.post("https://roboreactor.com/remote_config",json={email:{"status":"OFF","payload":status.get('payload')}})
                             print(res_config.json())
                             print("Writing the payload code",status.get("payload")) # Writing the payload  
                              
                if status.get("status") == "OFF":
                               print("Status off waiting for next remote config") # Waiting for the new remote config                                                                
        except:
            print("Data is not json type")       

                      
