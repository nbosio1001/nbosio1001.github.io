from flask import Flask, redirect, url_for, request
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Endpoint for initiating the authorization process
@app.route("/")
def start_auth():
    # Base URL for the authorization endpoint
    auth_endpoint = "https://auth.tesla.com/oauth2/v3/authorize"

    # Client ID provided by Tesla
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    audience = os.getenv("AUDIENCE")

    # Redirect URI registered with Tesla
    redirect_uri = "https://your_redirect_uri.com/callback"

    # Scopes requested by the client application
    scopes = "openid vehicle_device_data offline_access"

    # State parameter (optional, used for CSRF protection)
    state = "CA"

    # Construct the authorization URL with required parameters
    auth_url = f"{auth_endpoint}?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scopes}&state={state}"

    # Redirect the user's browser to the authorization URL
    return redirect(auth_url)

# Callback endpoint to handle the authorization response
@app.route("/callback", methods=["GET"])
def callback():
    # Retrieve the authorization code from the callback URL
    code = request.args.get("code")

    # Process the authorization code (e.g., exchange it for an access token)
    # Your code to handle the authorization code goes here

    # For demonstration purposes, simply display the authorization code
    return f"Authorization Code: {code}"

if __name__ == "__main__":
    app.run(debug=True)
