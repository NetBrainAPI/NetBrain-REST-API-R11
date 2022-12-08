
# Path API Design

## ***GET*** /V1/CMDB/Path/Calculation/{taskID}/Status	
Call this API to get the status information of a path calculated through the Calculate Path API. 

## Detail Information

> **Title** : Get Path Calulation Status API<br>

> **Version** : 12/08/2022.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Path/Calculation/{taskID}/Status	

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

> No request body.

## Path Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|taskID* | string  | Input the task ID returned by the CalcPath API. |

## Headers

> **Data Format Headers**

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| Content-Type | string  | support "application/json" |
| Accept | string  | support "application/json" |

> **Authorization Headers**

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| token | string  | Authentication token, get from login API. |

## Response

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|result| Object | The status result of path calculation. |
|resultCode| integer | The status code of path calculation. |
|resultDescription| string | The description of resultCode.<br>0 = Initialized<br>1 = Running <br>2 = Succeeded <br>3 = Failed <br>4 = Canceled|
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |

> ***Example***


```python
{
    "result": {
        "resultCode": 2,
        "resultDescription": "Succeeded"
    },
    "statusCode": 790200,
    "statusDescription": "Success."
}
```

# Full Example:


```python
# import python modules 
import requests
import time
import urllib3
import pprint
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
taskID = "064aa4b0-ac78-42f3-b26f-d160fafa35c0"

token = "4976c5f2-176c-4a09-af69-315dcf52e825"
nb_url = "https://integration.netbraintech.com"
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Path/Calculation/" + str(taskID) + "/Status"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

try:
    response = requests.get(full_url, headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        
        print ("Get path calulation code failed! - " + str(response.text))
    
except Exception as e:
    print (str(e))  
```

    {"result": {"resultCode": 2,"resultDescription": "Succeeded"},"statusCode": 790200,"statusDescription": "Success."}
    

# cURL Code from Postman:


```python
curl --location -g --request GET 'https://integration.netbraintech.com/ServicesAPI/API/V1/CMDB/Path/Calculation/{taskID}/status?taskID=064aa4b0-ac78-41f3-b26f-d160fafa35c0' \
--header 'token: 4976c5f2-176c-4a09-af69-315dcf52e825' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json'
```

