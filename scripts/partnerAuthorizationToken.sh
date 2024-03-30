#!/bin/bash

CLIENT_ID='8da11c0a5db1-48d7-b1fe-ecdaa1e555e5'
CLIENT_SECRET='ta-secret.F_rYBl8!4PTn5V$s'
AUDIENCE="https://fleet-api.prd.na.vn.cloud.tesla.com"
# Partner authentication token request
curl --request POST \
	--header 'Content-Type: application/x-www-form-urlencoded' \
	--data-urlencode 'grant_type=client_credentials' \
	--data-urlencode "client_id=$CLIENT_ID" \
	--data-urlencode "client_secret=$CLIENT_SECRET" \
	--data-urlencode 'scope=openid vehicle_device_data vehicle_cmds vehicle_charging_cmds' \
	--data-urlencode "audience=$AUDIENCE" \
	'https://auth.tesla.com/oauth2/v3/token'

