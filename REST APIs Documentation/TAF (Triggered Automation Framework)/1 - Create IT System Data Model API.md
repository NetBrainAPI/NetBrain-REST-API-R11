
# Create IT System Data Model API Design

## ***POST*** /V1/TAF/AutoMapping
Use this API to create an IT System Data Model definition in System Management/Integrated IT Systems/Integrated IT Systems.
This API helps to automate the IT System Data Model creation process.

## Detail Information

> **Title** : Create Event Metadata API

> **Version** : 02/24/2022

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/TAF/AutoMapping

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| name | String | Source name. To create a new definition, the name must be a new unique name. Otherwise, the definition will be merged to the existing definition. |
| description | String | Description |
| source | String | The URL Address value of the Integrated IT System Source |
| categories | Array of Objects | IT System Data Model categories |
| categories.name | String | IT System Data Model category name |
| categories.fields | Array of Objects | Category fields |
| categories.fields.name | String | Original field name |
| categories.fields.label | String | NetBrain field name |
| categories.fields.mappings | Array of Objects | Value translation mapping |
| categories.fields.mappings.value | Integer | Field original index value |
| categories.fields.mappings.label | String | Mapped NetBrain display value |


## Query Parameters(****required***)

> **No query parameter**

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
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |


## Example


```python
import json
import requests
import requests.packages.urllib3 as urllib3
 
urllib3.disable_warnings()

def getTokens(endpoint, user,password):
    login_api_url = r"/V1/Session"
    Login_url = endpoint + login_api_url
    data = {
        "username": user,
        "password": password
    }
    token = requests.post(Login_url, data=json.dumps(
        data), headers=headers, verify=False)
    if token.status_code == 200:
#         print(token.json())
        return token.json()["token"]
    else:
        return "error"

def CreateEventMetadata(endpoint, API_Body):
    API_URL = r"/V1/TAF/AutoMapping"
    api_full_url = endpoint + API_URL
    try:
        api_result = requests.post(api_full_url, data=json.dumps(API_Body), headers=headers, verify=False)
        if api_result.status_code == 200:
            return api_result.json()
        else:
            return api_result.json()
    except Exception as e:
        return str(e)
    
nb_endpoint = "https://netbraintech.com/ServicesAPI/API"
nb_username = ""
nb_password = ""

api_body = {
    "name":"API Sample",
    "description":"API Metadata definition sample",
    "source":"https://apisample.com",
    "categories":[
        {
            "name":"incident",       
            "fields":[
                {
                    "name":"description",
                    "label":"description"
                },
                {
                    "name":"state",
                    "label":"state",
                    "mappings":[
                        {
                            "value":0,
                            "label":"active"
                        },
                        {
                            "value":1,
                            "label":"closed"
                        }
                    ]
                }
            ]     
        }
    ]
}

headers = {
    "Accepted":"application/json",
    "Content-Type":"application/json"
}

token = getTokens(nb_endpoint, nb_username, nb_password)
headers["token"] = token

print(CreateEventMetadata(nb_endpoint, api_body))
```

    True
    
