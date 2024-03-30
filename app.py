from flask import Flask, redirect, url_for, request
from main import checkMemoryCache


app = Flask(__name__)

ENV_TESLA_API_TOKEN, REDIRECT_URI, CLIENT_ID, STATE = checkMemoryCache()



# Endpoint for initiating the authorization process
@app.route("/start_auth", methods=["GET"])
def start_auth(CLIENT_ID=CLIENT_ID,REDIRECT_URI=REDIRECT_URI,STATE=STATE):#,AUTH_URL):
    # Base URL for the authorization endpoint
    auth_endpoint = "https://auth.tesla.com/oauth2/v3/authorize"

    # Client ID provided by Tesla
    client_id = CLIENT_ID

    # Redirect URI registered with Tesla
    redirect_uri = REDIRECT_URI

    # Scopes requested by the client application
    scopes = "openid vehicle_device_data offline_access"

    # State parameter (optional, used for CSRF protection)
    state = STATE

    # Construct the authorization URL with required parameters
    auth_url = f"{auth_endpoint}?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scopes}&state={state}"

    # Redirect the user's browser to the authorization URL
    return redirect(auth_url)

# Callback endpoint to handle the authorization response
@app.route("/callback", methods=["GET"])
def callback():
    # Retrieve the authorization code from the callback URL
    code = request.args.get("code")
    print(code)
    # Process the authorization code (e.g., exchange it for an access token)
    # Your code to handle the authorization code goes here

    # For demonstration purposes, simply display the authorization code
    return f"Authorization Code: {code}"

if __name__ == "__main__":
    app.run(debug=True)
