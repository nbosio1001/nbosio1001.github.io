#!/usr/bin/bash
set -v

set -x
# Connect to Memcached server and retrieve value for 'mykey'
result=$(echo -e "get client_id\r\n" | telnet localhost | grep VALUE | awk '{print $NF}')
set +x
# Print the result
echo "Result: $result"



#firefox https://auth.tesla.com/oauth2/v3/authorize?&client_id=$CLIENT_ID&locale=en-US&prompt=login&redirect_uri=$REDIRECT_URI&response_type=code&scope=openid%20vehicle_device_data%20offline_access&state=$STATE

