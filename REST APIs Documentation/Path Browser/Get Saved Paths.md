

# Path Browser Management API Design

## ***GET*** /V1/CMDB/PathBrowser/Paths
This API is used call to saved paths from Path Browser.
This information can also be viewed from Application Manager in NetBrain.

## Detail Information

> **Title** : Get Saved Paths API<br>

> **Version** : 07/12/2022

> **API Server URL** : http(s):// IP address of your NetBrain Web API Server /ServicesAPI/V1/CMDB/PathBrowser/Paths

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

> No parameters required.

## Parameters(****required***)  
|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|application|string| Name of the application. <br>If this parameter is present, returns the saved path of the specified application. <br>If this parameter is empty, returns all saved path. <br><br> This parameter is optional.|
|skip*|integer|The amount of records to be skipped. <br>The value cannot be negative.|
|limit*|integer|The up limit amount of device records to return per API call. <br>The value cannot be negative. <br>The range is 10 to 100.|
|fullattr*|integer|`0` (default): returns basic path attributes (i.e. applicationName, pathName) <br>`1`: return all path attributes.|


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
|paths.applicationName| string |The application name that the path belongs to.|
|paths.pathName| string |Path name.|
|paths.sourceIP| string |Source IP.|
|paths.destinationIP| string |Destination IP.|
|paths.group| string |Multicast group.|
|paths.protocol| string |Protocol.|
|paths.lastResult| string |Last path execution status.|
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code. |


# Examples

## Example 1: Get Saved Path with all path attributes (`fullattr`=1)
```python
#R12
# Get Saved Paths
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/PathBrowser/Paths"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

application = "Untitled Application"
skip = 0
limit = 10
fullattr = 1

body={
    "application":application,
    "skip":skip,
     "limit":limit,
     "fullattr":fullattr
     }

try:
    response = requests.get(full_url, params=body, headers=headers, verify=False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Failed to Get Saved Paths! - " + str(response.text))
    
except Exception as e:
    print (str(e)) 
```
```
  {'paths': [{'applicationName': 'Untitled Application', 'pathName': 'test', 'sourceIP': '192.168.32.11', 'destinationIP': '192.168.32.12', 'group': '', 'protocol': 'IP', 'lastResult': 'Failed'}, {'applicationName': 'Untitled Application', 'pathName': 'test1', 'sourceIP': '169.254.1.2', 'destinationIP': '169.254.1.3', 'group': '', 'protocol': 'IP', 'lastResult': 'Failed'}], 'statusCode': 790200, 'statusDescription': 'Success.'}
```


## Example 2: Get Saved Path without paramter `application` with their basic path attributes (`fullattr`=1)
```python
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/PathBrowser/Paths"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

skip = 0
limit = 10
fullattr = 0

body={
    "skip":skip,
     "limit":limit,
     "fullattr":fullattr
     }

try:
    response = requests.get(full_url, params=body, headers=headers, verify=False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Failed to Get Saved Path(s)! - " + str(response.text))
    
except Exception as e:
    print (str(e)) 
```
```
  {'paths': [{'applicationName': 'Untitled Application', 'pathName': 'test'}, {'applicationName': 'Untitled Application', 'pathName': 'test1'}], 'statusCode': 790200, 'statusDescription': 'Success.'}
```


# cURL command from Postman
This example is based on Example 2

```python
curl -X GET \
  'https://nextgen-training.netbrain.com/ServicesAPI/API/V1/CMDB/PathBrowser/Paths?skip=0&limit=10&fullattr=0' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: e8341d5e-32e2-4f80-9c35-f0f9a1d13ce4' \
  -H 'cache-control: no-cache'
  ```