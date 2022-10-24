
# API Server Management

## ***GET*** /V1/CMDB/APIServers
This API returns all API servers configured in the domain. The user who making this API call need to have domain access along with "Manage Network Settings" Permission. The API will not return API server password and any encrypted content if user configured in extraParams.

## Detail Information

> **Title** : Get All API Server Configured in Domain API<br>

> **Version** : 03/03/2022.

> **API Server URL** : http(s):// IP address of your NetBrain Web API Server /ServicesAPI/API/V1/CMDB/APIServers

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|Bearer Authentication| Parameters | Authentication token | 

 ## Request body(****required***)

>No request body.

 ## Query Parameters(****required***)

>No request body.

 ## Headers

> **Data Format Headers**

|**Name**|**Type**|**Description**|
|------|------|------|
| Content-Type | string  | support "application/json" |
| Accept | string  | support "application/json" |

> **Authorization Headers**

|**Name**|**Type**|**Description**|
|------|------|------|
| token* | string  | Authentication token, get from login API. |

 ## Response

|**Name**|**Type**|**Description**|
|------|------|------|
|apiServers | list of object | A list of all API Servers configured in the domain. |
|id| string | The API Server ID.  |
|serverName| string | The API Server name. |
|desc| string | The API Server description.  |
|apiSourceType| string | The API Adapter name. |
|endpoint| string | The connected third-party service address. |
|username| string | The user name to access the third-party server. |
|frontserverAndGroupName| string | Front Server or Front Server Group name to connect to the third-party API server. |
|fsInfo| string | Front Server detail information. |
|deviceCounts| string | Total number of devices assigned to this API server. |
|password| NULL | NULL. |

> ***Example***

```python
{
    "apiServers": [
        {
            "id": "3cf17c81-8647-4d73-bacd-091557940829",
            "serverName": "NetBrain ServiceNow Lab",
            "desc": "This is NetBrain ServiceNow Lab 1750 environment",
            "apiSourceType": "ServiceNow API Adapter",
            "endpoint": "https://dev01750.service-now.com",
            "username": "admin",
            "frontserverAndGroupName": "WIN-AAVF2I6EUIE",
            "fsInfo": "testFS(192.168.28.123)",
            "deviceCounts": 0,
            "password": null,
            "extraParams": [],
            "frontServerAndGroupId": "testFS"
        }
    ],
    "statusCode": 790200,
    "statusDescription": "Success."
}
```

 ## Full Example : 


```python
# import python modules 
import requests

# Set the request inputs
token = "aaab6acf-caa6-40f9-a5e1-a5fe5d2df18d"
full_url = "http://192.168.28.123/ServicesAPI/API/V1/CMDB/APIServers"

# Set proper headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

try:
    # Do the HTTP request
    response = requests.get(full_url, headers=headers, verify=False)
    # Check for HTTP codes other than 200
    if response.status_code == 200:
        # Decode the JSON response into a dictionary and use the data
        result = response.json()
        print (result)
    else:
        print ("Get API Server failed! - " + str(response.text))

except Exception as e: print (str(e))
```

    {'apiServers': [{'id': '56f17c81-8647-4d73-bacd-091557940829', 'serverName': 'NetBrain ServiceNow Lab', 'desc': 'This is NetBrain ServiceNow Lab 1750 environment', 'apiSourceType': 'ServiceNow API Adapter', 'endpoint': 'https://dev1750.service-now.com', 'username': 'admin', 'frontserverAndGroupName': 'WIN-AAVF2I6EUIE', 'fsInfo': 'testFS(192.168.28.123)', 'deviceCounts': 0, 'password': None, 'extraParams': [], 'frontServerAndGroupId': 'testFS'}], 'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman


```python
curl --location --request GET 'http://192.168.28.123/ServicesAPI/API/V1/CMDB/APIServers' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: aaab6acf-caa6-40f9-a5e1-a5fe5d2df18d'
```
