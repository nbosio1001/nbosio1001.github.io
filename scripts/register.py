import os
import http.client
import json

ENV_TESLA_API_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1GUWpMaVF4OEZEeEdka2l1VDhuOW5RRGNRNCJ9.eyJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJzdWIiOiI4ZGExMWMwYTVkYjEtNDhkNy1iMWZlLWVjZGFhMWU1NTVlNSIsImlzcyI6Imh0dHBzOi8vYXV0aC50ZXNsYS5jb20vb2F1dGgyL3YzL250cyIsImF6cCI6IjhkYTExYzBhNWRiMS00OGQ3LWIxZmUtZWNkYWExZTU1NWU1IiwiYXVkIjpbImh0dHBzOi8vYXV0aC50ZXNsYS5jb20vb2F1dGgyL3YzL2NsaWVudGluZm8iLCJodHRwczovL2ZsZWV0LWFwaS5wcmQubmEudm4uY2xvdWQudGVzbGEuY29tIl0sImV4cCI6MTY5OTI1Njk2NCwiaWF0IjoxNjk5MjI4MTY0LCJzY3AiOlsidmVoaWNsZV9kZXZpY2VfZGF0YSIsInZlaGljbGVfY21kcyIsInZlaGljbGVfY2hhcmdpbmdfY21kcyIsIm9wZW5pZCJdfQ.khmK-qt4UTEKE6LL2R4sVG0SLCgdraDeQp0GOQ-zU231zgl42jsOqRkrav4NHVTC4TfaHlSuuWelNspJrgMm-3Ke4dE-h00o_nX7_rJ0d2I9sy06ck-m1Ps8BLdd-3-DQczMS-pL48HrkarI93ZZpb0tV-aytq47YVMknlGPdx0g-GflIcTmP0h_o1_Kh8GCD7col_Rx1LzOLAYsj1yZvQECozlTX68_GLJl4_kHtrJg-FX_R7R1CYG4Giatv6fPOQQoqjykUqm5fJHp4ZmtEjIdRrtGmGGrjEBojU2OLw3kt8XmWLKdJcgcwS2av6bDUY_RTmoho4EaTnIXAjvNBA'

conn = http.client.HTTPSConnection("fleet-api.prd.na.vn.cloud.tesla.com")
payload = json.dumps({
    "domain": "nbosio1001.github.io"
       })
headers = {
           'Content-Type': 'application/json',
              'Authorization': f'Bearer {ENV_TESLA_API_TOKEN}'
              }
conn.request("POST", "/api/1/partner_accounts", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

