#Can wrap main in decorator that starts memcached before 
#Hook into
from pymemcache.client.base import Client
import os
import subprocess
import json

def checkMemoryCache():
#   createTable()
    try:
        client = Client(("localhost",11211))
#       client = Client(("localhost",11211),serde=(python_memcache_serializer))
    except ConnectionRefusedError as e:
        print("Try systemctl start memcached")
#   print(client)
    if client.get("access_token") is None:
        command = bashScripts()

        dictObj = bash_output_to_dictionary(command.executeCommand())
        client.set_many(dictObj, expire=dictObj['expires_in'])
    print(client.get_many(['access_token']))
    ENV_TESLA_API_TOKEN = client.get_many(['access_token'])
    ENV_TESLA_API_TOKEN = ENV_TESLA_API_TOKEN['access_token'].decode('UTF-8')

# Register partner account before using general API
#   register
#   vehicle_device_data(ENV_TESLA_API_TOKEN)
    REDIRECT_URI = os.getenv("REDIRECT_URI")
    CLIENT_ID = os.getenv("CLIENT_ID")
    STATE=os.getenv("STATE")
    return ENV_TESLA_API_TOKEN, REDIRECT_URI, CLIENT_ID, STATE
#   print(REDIRECT_URI,CLIENT_ID,STATE)
#   app(CLIENT_ID,REDIRECT_URI,STATE,AUTH_URL)
#   print(getRequest(CLIENT_ID,REDIRECT_URI,STATE))
#   print(register_user(ENV_TESLA_API_TOKEN))
    
def main0(client, dictObj):
    dictObj['expires_in'] = str(dictObj['expires_in'])
    serialized_data = {key: json.dumps(value) for key, value in dictObj.items()}
    client.set_many(serialized_data,expire=int(dictObj["expires_in"]))
#   client.set("ENV_TESLA_API_TOKEN",dictObj["access_token"])
#   ENV_TESLA_API_TOKEN = database.get_tesla_access_token()
#   client.set("ENV_TESLA_API_TOKEN",ENV_TESLA_API_TOKEN)
#   bashCommand(TESLA_API_TOKEN)
#   print(dictObj["access_token"])
    retrieved_data = {key: json.dumps(value) for key, value in client.get_many()}
    print(retrieved_data)

def generateCustomerToken():
    CLIENT_ID = os.getenv("CLIENT_ID")
    REDIRECT_URI = 'https://nbosio1001.github.io/redirectPage'
    STATE = 'CA'

    url = f
def main1():
    string_output = register_user(dictObj["access_token"])
    registration_output = bash_output_to_dictionary(string_output)
#   print(registration_output)
    client.set('public_key',registration_output['response']['public_key'])
    client.set('client_id',registration_output['response']["client_id"])
#   executeCommand(command)
#   bashCommand(TESLA_API_TOKEN)
#https://auth.tesla.com/oauth2/v3/authorize?&client_id=$CLIENT_ID&locale=en-US&prompt=login&redirect_uri=$REDIRECT_URI&response_type=code&scope=openid%20vehicle_device_data%20offline_access&state=$STATE

class bashScripts:
    def __init__(self):
        self.command = ['/usr/bin/bash', '/home/nbosio1001/Documents/tesla/teslacommand/src/scripts/partnerAuthorizationToken.sh']

    def executeCommand(self):
        # Run the command
        try:
                result = subprocess.run(self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
                string_output = result.stdout.decode()
    #           print("Output:", string_output)
        except subprocess.CalledProcessError as e:
                print("Error executing command")
                print("Error:", e.stderr.decode())
        return string_output


def createTable():
    columns_dict = {
            'access_token': 'TEXT',
            'expires_in': 'INT',
            'token_type': 'CHAR(100)',
            'expiration_time': 'INT'
            }
    database.create_table_from_dict(user='nbosio1001',database='teslaData',table_name='authentication',columns_dict=columns_dict)
#   if partner_authorization not in the database or current_time(int(time.time()) is NOT greater than expiration_time:



def bash_output_to_dictionary(string_output):
    output_json = string_output.strip()
    return json.loads(output_json) 


#   print(partnerAuthentication)
def main1():
    # modifyEnvVariables()
    env_tesla_api_token = {'ENV_TESLA_API_TOKEN':None}     
    url = 'https://auth.tesla.com/oauth2/v3/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    # response = AuthorizationRequest(url)
    # env_variables = convertToENVFormat(response.get_request_text())
    # appendEnvFile(env_variables)
    if checkAccessToken() is False:
        partnerObj = PartnerAuthorization(url, headers)
        json_data = partnerObj.post_request(url,headers) 
        



        env_variables = convertToENVFormat(json_data) 

        appendEnvFile(env_variables)
    env_tesla_api_token['ENV_TESLA_API_TOKEN']=os.getenv('access_token')
    REDIRECT_URI="nbosio1001.github.io/redirectPage"
    CLIENT_ID="8da11c0a5db1-48d7-b1fe-ecdaa1e555e5"
    # registered_users_json_data = register_user(env_tesla_api_token['ENV_TESLA_API_TOKEN']) # '{"response":{"domain":"nbosio1001.github.io","name":"teslaCustomizationApp","description":"To be determined","client_id":"8da11c0a5db1-48d7-b1fe-ecdaa1e555e5","ca":null,"created_at":"2023-11-02T00:13:42.719Z","updated_at":"2023-11-17T23:03:12.635Z","enterprise_tier":"free","public_key":"040ebec32e7369403fdbe3761f7a97b53eab71f0e5be1044deaee3d92e8ea20c5c3121ad826da655d33227c36c4631d02073bbab672037931e61dbd7328457a88e"}}'
    # users_data = convertToENVFormat(registered_users_json_data) # "response={'domain': 'nbosio1001.github.io', 'name': 'teslaCustomizationApp', 'description': 'To be determined', 'client_id': '8da11c0a5db1-48d7-b1fe-ecdaa1e555e5', 'ca': None, 'created_at': '2023-11-02T00:13:42.719Z', 'updated_at': '2023-11-17T23:03:12.635Z', 'enterprise_tier': 'free', 'public_key': '040ebec32e7369403fdbe3761f7a97b53eab71f0e5be1044deaee3d92e8ea20c5c3121ad826da655d33227c36c4631d02073bbab672037931e61dbd7328457a88e'}"

#   os.environ["CLIENT_ID"] = ans
#   os.environ["REDIRECT_URI"] = "nbosio1001.github.io/redirectPage"
#    vehicle_device_data(obj.ENV_TESLA_API_TOKEN)

#    obj.get_request_data
#    obj.print_response
#    if checkAccessToken() is False:
#        pass
        #setAccessKeyEnvVariable()
#       partner_authentication_data = HTTPClient("auth.tesla.com/oauth2/v3/token")
#       partner_authentication_data = HTTPClient("https://auth.tesla.com/oauth2/v3/token")
#       getPartnerAuthTokenWithCurlCommand() 


def checkAccessToken():
    if 'access_token' not in dotenv.dotenv_values():
       return False

#   json_data = json.dump(token_stdout)
#   env_data = [f"{key}={value}" for key, value in json_data.items()]

def convertToENVFormat(json_data):
    data = json.loads(json_data)
    env_data = "\n".join(f'{key}={value}' for key, value in data.items())
    return env_data


def setAccessKeyEnvVariable(curl_command):
    try:
        json_data = json.loads(curl_command,index=2)
    except Exception as e:
        with open('error.txt','w') as file:
            output_string = f"{curl_command}\ntype: {type(curl_command)}"
            file.write(output_string)
    # output = subprocess.check_output(curl_command,shell=True,text=True)

    # json_data = json.loads(output)

#   for key,value in json_data.items():
#       os.environ[key] = str(value)
####    dotenv.set_key(dotenv_path="../,env",key=key,value=value)





if __name__=="__main__":
    checkMemoryCache()
