import os 
import jwt 
import json 
import requests 
from itertools import count 
email = "kornbot380@hotmail.com" # Getting the email account data of the user to checking the data of the user payload 
path_token = "/home/"+os.listdir("/home/")[0]+"/RoboreactorGenFlow" # Getting the path token data 
try:
   Load_json = open(path_token+"data_token_secret.json",'r') # Load the json data in local computer this file need to be export from the website 
   OAuth  = json.loads(Load_json.read())  # Load json data of the persal OAuth downloaded from the web and put into the local file 
   Account_data = OAuth.get('Account')
   Token_data = OAuth.get('Token')
   Secret_data = OAuth.get('Secret') 
   Project_data = OAuth.get('project_name') # getting the project name  
except:
     pass 

class Authentication_function(object): 
        def request_authentication_API(self,Email,token,secret,Project):
                Authentication_data = {'Email':Email,'project_name':Project}
                res = requests.post('https://roboreactor.com/API/endpoint_request', json=Authentication_data)
                #return logic to the authentication to check the status of the hardware connection 
                q_res = res.json().get(Authentication_data.get('Email'))
                token_data = str(q_res[0])+'.'+str(token)
                decode_Data = jwt.decode(q_res[0]+'.'+str(token),str(q_res[1]) ,algorithm=["HS512"])
                return decode_Data 

def Authentication_system(Email,token,secret,Project): 
      authen = Authentication_function() 
      data_out = authen.request_authentication_API(Email,token,secret,Project)
      return data_out

try:
     Data = Authentication_system(Account_data,Token_data,Secret_data,Project_data)  # Getting the project data to verify the project data to post request sendback the data 
     print(Data) # Getting the email to verfy the data to send back to request the project and send back data to the user profile information  
except: 
     pass 

#Loading the data from the path of the token 
for i in count(0):
        #Step 0 checking the email account of the user to get the status payload 
        #Step 1 post request into the broker to run checking status 
        #Step 2 after detect status ON then running the json file input from the payload 
        #Step 3 after running the payload finish then change the status of the json input to status off 
        print(Data)
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

                      
