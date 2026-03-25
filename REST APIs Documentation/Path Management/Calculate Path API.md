
# Path API Design

## ***POST*** /V1/CMDB/Path/Calculation
Call this API to calculate the path from endpoint A (source) to endpoint B (destination). <br> 
It returns the result of the calculated path in the form of a path ID (a string), which can be used as the input parameter to get each hop information of the path via [Get Path Calculation Result API](https://github.com/NetBrainAPI/NetBrain-REST-API-R12.3/blob/main/REST%20APIs%20Documentation/Path%20Management/Get%20Path%20Calculation%20Result%20API.md) or [Get Path Calculation Overview API](https://github.com/NetBrainAPI/NetBrain-REST-API-R12.3/blob/main/REST%20APIs%20Documentation/Path%20Management/Get%20Path%20Calculation%20Overview%20API.md).

## Detail Information

> **Title** : Calculate Path API<br>

> **Version** : 05/09/2023.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Path/Calculation

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|sourceIP* | string  | Input the IP address of the source device.  |
|sourcePort | integer  | Specify the source protocol port If TCP/UDP is selected such as 23 for telnet. This parameter can be null.  |
|sourceGateway* | Object  | Source gateway resolve result, end user **MUST** use gateway resolve result.  |
|sourceGateway.type* | string | Result relies on Step 1, can be disregarded for customer.|
|sourceGateway.gatewayName* | string  | The name of the gateway. Result from Step 1.  |
|gatewayList.payload*| dict | Internal data structure, can be disregarded for customer.  |
|destIP* | string  | Input IP address of the destination device.  |
|destPort* | integer  | Specify the destination protocol port If TCP/UDP is selected, such as 23 for telnet. This parameter can be null.  |
|protocol* | integer  | Specify the application protocol. see list_of_ip_protocol_numbers, such as 4 for IPv4.  |
|isLive* | bool  | ▪ `False` - Use data From current Baseline<br>▪ `True` - Use data via live access |
|advanced |object |advance setting.|
|advanced.debugMode | bool	|The debug mode of trigger API.|
|advanced.calcWhenDeniedByACL| bool | Whether to keep calculate when the process been denied by ACL.|
|advanced.calcWhenDeniedByPolicy |bool |Whether to keep calculate when the process been denied by policy.|
|advanced.calcL3ActivePath| bool |Whether to calculate L3 active path.|
|advanced.useCommandsWithArguments| bool |Whether to use the commands with arguments inside.|
|advanced.enablePathFixup |bool |Whether to enable the path fixup feature.|
|routingScheme |integer |Scheme for routing process and with two values 0 and 1 can be selected. 0 - `UNICAST`, 1 - `MULTICAST`.|
|group |string |Group name for Unicast calculation. (The group must have value when the routing scheme is 0).|

## Parameters(****required***)

>No parameters required.

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
| token | string  | Authentication token, retrieved from Login API. |

## Response

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|taskID| string | The task ID of the calculated path. <br> Use this as `taskID` input parameter in Get Path Calculation Result API or Get Path Calculation Overview API to get the hop information of the path. |
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |

> ***Example***
```python
{
    'taskID': 'b0bae173-af8c-418b-8dc4-1ffdb0e897fa',
    'statusCode': 790200,
    'statusDescription': 'Success.'
}
```

# Full Example:
```python
Calculate_Path_url = nb_url + "/ServicesAPI/API/V1/CMDB/Path/Calculation"

gwName = source_gateway["gatewayList"][0]["gatewayName"]
gwType = source_gateway["gatewayList"][0]["type"]
gw = source_gateway["gatewayList"][0]["payload"]

sourceIP = source_device
sourcePort = None #can be 8080
destIP = destination_device
destPort = 0
pathAnalysisSet = 2
protocol = 4
isLive = True

body = {
    "sourceIP" : sourceIP,                # IP address of the source device.
    "sourcePort" : sourcePort,
    "sourceGateway" : {
        "type" : gwType,
        "gatewayName" : gwName,
        "payload" : gw
    },    
    "destIP" : destIP,                    # IP address of the destination device.
    "destPort" : destPort,
    "protocol" : protocol,                # Specify the application protocol, check online help, such as 4 for IPv4.
    "isLive" : isLive                     # False: Current Baseline; True: Live access
} 


def calculate_path(Calculate_Path_url, body, headers, token):
    headers["Token"] = token
    
    try:
        response = requests.post(Calculate_Path_url, data = json.dumps(body), headers = headers, verify = False)
        if response.status_code == 200:
            result = response.json()
            return (result)
        else:
            return ("Failed to Calculate Path! - " + str(response.text))

    except Exception as e:
        return (str(e)) 

res = calculate_path(Calculate_Path_url, body, headers, token)
res
```
```python
    {'taskID': 'dcf25655-81a9-4cfe-82ca-aef80a698971',
     'statusCode': 790200,
     'statusDescription': 'Success.'}
```

# cURL Code from Postman
```python
curl -X POST \
  http://192.168.28.173/ServicesAPI/API/V1/CMDB/Path/Calculation \
  -H 'Accept: */*' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Host: 192.168.28.173' \
  -H 'Postman-Token: 8e0bc75f-58c8-48fe-869a-0535f6385590,b98e9443-bf6d-4b12-be03-bf580231fa38' \
  -H 'User-Agent: PostmanRuntime/7.13.0' \
  -H 'accept-encoding: gzip, deflate' \
  -H 'cache-control: no-cache' \
  -H 'content-length: 581' \
  -H 'token: 76f95ffa-fc1b-4eb6-a503-75760185f2a5' \
  -d '{
"sourceIP": "172.24.33.10",
 "sourcePort": None,
 "sourceGateway": {
 	"type": "Device Interface",
    "gatewayName": "BJ_L2_test_1.Vlan10(172.24.33.10)",
    "payload": "{"ip": "172.24.33.10", "endPointInfo": {"deviceId": "101deae6-8d11-47d2-b87f-b69cbe7ba2ce", "interfaceId": "9a40c2e8-12ba-4556-bb2f-9545f776afb7"}, "device": "BJ_L2_test_1", "deviceId": "101deae6-8d11-47d2-b87f-b69cbe7ba2ce", "interface": "Vlan10", "interfaceId": "9a40c2e8-12ba-4556-bb2f-9545f776afb7", "prefixLen": 26}"},
 "destIP": "172.24.33.135",
 "destPort": 0,
 "protocol": 4,
 "isLive": True	
}'
```
