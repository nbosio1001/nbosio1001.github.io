import os
import http.client
import json

conn = http.client.HTTPSConnection("fleet-api.prd.na.vn.cloud.tesla.com")
payload = json.dumps({
   "domain": "string"
})
headers = {
   'Content-Type': 'application/json',
   'Authorization': 'Bearer ENV_TESLA_API_TOKEN'
}
conn.request("POST", "/api/1/partner_accounts", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

