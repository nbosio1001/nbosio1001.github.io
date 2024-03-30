efresh token request
REFRESH_TOKEN=<extract from authorization code token request>
curl --request POST \
	 --header 'Content-Type: application/x-www-form-urlencoded' \
	 --data-urlencode 'grant_type=refresh_token' \
	--data-urlencode "client_id=$CLIENT_ID" \
		    --data-urlencode "refresh_token=$REFRESH_TOKEN" \
			  'https://auth.tesla.com/oauth2/v3/token'

