
# Path Calculation Design

***Note:*** It is mandatory to follow the below sequence of steps to successfully call Path Calculation APIs.

# Step 1 - Resolve device gateway

## ***GET*** /V1/CMDB/Path/Gateways
Call this API to retrieve the gateways for a device used as path source.

## Detail Information

> **Title** : Resolve Device Gateway API<br>

> **Version** : 06/27/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Path/Gateways

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

> No request body.

## Query Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| ipOrHost* | string  | Device mgmIp or hostname, used as the source in path calculation. |

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
|gatewayList| List of Object | Gateway list.  |
|gatewayList.gatewayName| string | The name of gateway.  |
|gatewayList.type| string | The type of gateway.  |
|gatewayList.payload| dict | Internal data structure, customer don't need to considered.  |
|transip| string | Ip address of gateway.  |
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |


```python
{
    "gatewayList": [
        {
            "gatewayName": "BJ_L2_test_1.Vlan10(172.24.33.10)",
            "type": "Device Interface",
            "payload": "{\"ip\": \"172.24.33.10\", \"endPointInfo\": {\"deviceId\": \"101deae6-8d11-47d2-b87f-b69cbe7ba2ce\", \"interfaceId\": \"9a40c2e8-12ba-4556-bb2f-9545f776afb7\"}, \"device\": \"BJ_L2_test_1\", \"deviceId\": \"101deae6-8d11-47d2-b87f-b69cbe7ba2ce\", \"interface\": \"Vlan10\", \"interfaceId\": \"9a40c2e8-12ba-4556-bb2f-9545f776afb7\", \"prefixLen\": 26}"
        }
    ],
    "transip": "172.24.33.10",
    "statusCode": 790200,
    "statusDescription": "Success."
}
```

## Full Example
```python
# import python modules 
import requests
import time
import urllib3
import pprint
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json

nb_url = "http://192.168.28.173"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'} 
token = "76f95ffa-fc1b-4eb6-a503-75760185f2a5"
source_device = "172.24.33.10"
destination_device = "172.24.33.135"
```


```python
Resolve_Device_Gateway_url = nb_url + "/ServicesAPI/API/V1/CMDB/Path/Gateways"

def resolve_device_gateway(Resolve_Device_Gateway_url, token, ipOrHost, headers):
    headers["Token"] = token
    data = {"ipOrHost":ipOrHost}
    try:
        response = requests.get(Resolve_Device_Gateway_url, params = data, headers = headers, verify = False)
        if response.status_code == 200:
            result = response.json()
            return (result)
        else:
            return ("Create module attribute failed! - " + str(response.text))

    except Exception as e:
        print (str(e))

source_gateway = resolve_device_gateway(Resolve_Device_Gateway_url, token, source_device, headers)
source_gateway
```
    {'gatewayList': [{'gatewayName': 'BJ_L2_test_1.Vlan10(172.24.33.10)',
       'type': 'Device Interface',
       'payload': '{"ip": "172.24.33.10", "endPointInfo": {"deviceId": "101deae6-8d11-47d2-b87f-b69cbe7ba2ce", "interfaceId": "9a40c2e8-12ba-4556-bb2f-9545f776afb7"}, "device": "BJ_L2_test_1", "deviceId": "101deae6-8d11-47d2-b87f-b69cbe7ba2ce", "interface": "Vlan10", "interfaceId": "9a40c2e8-12ba-4556-bb2f-9545f776afb7", "prefixLen": 26}'}],
     'transip': '172.24.33.10',
     'statusCode': 790200,
     'statusDescription': 'Success.'}


## cURL Code from Postman
```python
curl -X GET \
  'http://192.168.28.173/ServicesAPI/API/V1/CMDB/Path/Gateways?ipOrHost=172.24.33.10' \
  -H 'Accept: */*' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Host: 192.168.28.173' \
  -H 'Postman-Token: e03fba73-b667-49d4-badb-7c166ef88a94,a062a3f7-6186-4ef4-98ca-2afae1c17f7f' \
  -H 'User-Agent: PostmanRuntime/7.13.0' \
  -H 'accept-encoding: gzip, deflate' \
  -H 'cache-control: no-cache' \
  -H 'token: 76f95ffa-fc1b-4eb6-a503-75760185f2a5'
```

# Step 2 - Path Calculation

## ***POST*** /V1/CMDB/Path/Calculation
Call this API to calculate the path from endpoint A (source) to endpoint B (destination). <br> 
It returns the result of the calculated path in the form of a path ID (a string), which can be used as the input parameter to get each hop information of the path via [Get Path Calculation Result API](https://github.com/NetBrainAPI/NetBrain-REST-API-R11/blob/main/REST%20APIs%20Documentation/Path%20Management/Get%20Path%20Calculation%20Result%20API.md) or [Get Path Calculation Overview API](https://github.com/NetBrainAPI/NetBrain-REST-API-R11/blob/main/REST%20APIs%20Documentation/Path%20Management/Get%20Path%20Calculation%20Overview.md).


## Detail Information

> **Title** : Calculate Path API<br>

> **Version** : 06/27/2019.

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
|advanced |object	|advance setting.|
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
    'taskID': 'dcf25655-81a9-4cfe-82ca-aef80a698971',
    'statusCode': 790200,
    'statusDescription': 'Success.'
}
```

## Full Example:
```python
# call calculate_path API

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



## cURL Code from Postman
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

# Step 3 - Get Path Calculation OverView

## ***GET*** /V1/CMDB/Path/Calculation/{taskID}/OverView
Call this API to get the hop information of the calculated path achieved through [Calculate Path API](https://github.com/NetBrainAPI/NetBrain-REST-API-R12/blob/main/REST%20APIs%20Documentation/Path%20Management/Calculate%20Path%20API.md). 

If the [Calculation Path](https://github.com/NetBrainAPI/NetBrain-REST-API-R12/blob/main/REST%20APIs%20Documentation/Path%20Management/Calculate%20Path%20API.md) task is not yet finished or failed, the API will prompt an error with message accordingly. 

All directed links in the result consists of a directed path graph, which contains all possible reachable paths from the original source to the destination specified in path calculation.

## Detail Information

> **Title** : Get Path Calculation Overview API<br>

> **Version** : 01/30/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Path/Calculation/{taskID}/OverView	

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
|taskID* | string  | Input the task ID returned by the Calculate Path API. |

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
The below table mainly includes the fields meant for customer's use. <br>
To view all the generated fields, please refer to the examples below.
|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| path_overview | list of Object | A list of path_list.|
| path_list | list of Object | A list of path.|
| branch_list | list of Object | A list of branch.|
| hop_detail_list | list of Object | A list of hop with hop detail information.|
| fromDev | Object | Detail information of source device. |
| devId | string | ID of source device. |
| devName | string | Hostname of source device. |
| devType | integer | Type of source device. |
| fromIntf | Object | The detailed information of source device interface. |
| hopId | string | The ID of current hop. |
| isP2P | boolean | `True` - P2P <br> `False` - not P2P |
| mediaInfo | Object | The detailed information of media. |
| failure_reason | string | Explanation of the failure path. |
| description | string | Path description. |
| status | string | Status of the path calculation. |
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |

> ***Example***
```python
{
  "path_overview": [
    {
      "path_list": [
        {
          "branch_list": [
            {
              "hop_detail_list": [
                {
                  "fromDev": {
                    "devId": "02ef8cd1-27be-414f-bd86-dc62c660b881",
                    "devName": "192.168.0.197",
                    "devType": 1005,
                    "domainId": ""
                  },
                  "fromIntf": {
                    "intfKeyObj": {
                      "schema": "intfs._id",
                      "value": "5da2f88e-3560-485b-bfaf-04b328117d49"
                    },
                    "intfDisplaySchemaObj": {
                      "schema": "intfs.name",
                      "value": "Ethernet0"
                    },
                    "PhysicalInftName": "Ethernet0",
                    "ipLoc": ""
                  },
                  "hopId": "e38cc13f-147a-44d6-962f-535b734f92b3",
                  "isComplete": false,
                  "isP2P": false,
                  "mediaId": "fa8111b9-60d5-4925-9607-b88d4eced2ef",
                  "mediaInfo": {
                    "mediaName": "192.168.0.0/22\r\nVRRP: 0(192.168.0.64)",
                    "mediaType": "Lan",
                    "neat": false,
                    "topoType": "L3_Topo_Type"
                  },
                  "preHopId": "00000000-0000-0000-0000-000000000000",
                  "sequnce": 0,
                  "toIntf": {
                    "intfKeyObj": {
                      "schema": "ipIntfs._id",
                      "value": "d6c271e0-f647-4cf3-bc78-8fe40bc28abb"
                    },
                    "intfDisplaySchemaObj": {
                      "schema": "ipIntfs.name",
                      "value": "Mgmt 192.168.0.62/22"
                    },
                    "PhysicalInftName": "Mgmt",
                    "ipLoc": "192.168.0.62/22"
                  },
                  "toDev": {
                    "devId": "17f64621-642a-42f1-a7bd-aae287ceecf2",
                    "devName": "CP_HA2",
                    "devType": 30080,
                    "domainId": ""
                  },
                  "topoType": "L3_Topo_Type",
                  "trafficState": {
                    "acl": "",
                    "alg": -1,
                    "dev_name": "192.168.0.197",
                    "dev_type": 1005,
                    "in_intf": "Ethernet0",
                    "in_intf_schema": "intfs",
                    "in_intf_topo_type": "L3_Topo_Type",
                    "next_dev_in_intf": "Mgmt 192.168.0.62/22",
                    "next_dev_in_intf_schema": "ipIntfs",
                    "next_dev_in_intf_topo_type": "L3_Topo_Type",
                    "next_dev_name": "CP_HA2",
                    "next_dev_type": 30080,
                    "next_hop_ip": "192.168.0.62",
                    "next_hop_mac": "",
                    "out_intf": "Ethernet0",
                    "out_intf_schema": "intfs",
                    "out_intf_topo_type": "L3_Topo_Type",
                    "pbr": "",
                    "vrf": ""
                  },
                  "parentHopId": "",
                  "isGateway": false,
                  "techs": []
                },
                {
                  "fromDev": {
                    "devId": "17f64621-642a-42f1-a7bd-aae287ceecf2",
                    "devName": "CP_HA2",
                    "devType": 30080,
                    "domainId": ""
                  },
                  "fromIntf": {
                    "intfKeyObj": {
                      "schema": "",
                      "value": ""
                    },
                    "intfDisplaySchemaObj": {
                      "schema": "",
                      "value": ""
                    },
                    "PhysicalInftName": "",
                    "ipLoc": ""
                  },
                  "hopId": "193c9332-dabe-49ea-be40-59fdac9a8fb4",
                  "isComplete": false,
                  "isP2P": false,
                  "mediaId": "",
                  "mediaInfo": {
                    "mediaName": "",
                    "mediaType": "",
                    "neat": false,
                    "topoType": ""
                  },
                  "preHopId": "e38cc13f-147a-44d6-962f-535b734f92b3",
                  "sequnce": 1,
                  "toIntf": {
                    "intfKeyObj": {
                      "schema": "",
                      "value": ""
                    },
                    "intfDisplaySchemaObj": {
                      "schema": "",
                      "value": ""
                    },
                    "PhysicalInftName": "",
                    "ipLoc": ""
                  },
                  "toDev": {
                    "devId": "",
                    "devName": "",
                    "devType": 0,
                    "domainId": ""
                  },
                  "topoType": "",
                  "trafficState": {
                    "acl": "",
                    "alg": -1,
                    "dev_name": "CP_HA2",
                    "dev_type": 30080,
                    "in_intf": "Mgmt 192.168.0.62/22",
                    "in_intf_schema": "ipIntfs",
                    "in_intf_topo_type": "L3_Topo_Type",
                    "next_dev_in_intf": "",
                    "next_dev_in_intf_schema": "",
                    "next_dev_in_intf_topo_type": "L3_Topo_Type",
                    "next_dev_name": "",
                    "next_dev_type": 0,
                    "next_hop_ip": "",
                    "next_hop_mac": "",
                    "out_intf": "",
                    "out_intf_schema": "",
                    "out_intf_topo_type": "L3_Topo_Type",
                    "pbr": "",
                    "vrf": ""
                  },
                  "parentHopId": "",
                  "isGateway": false,
                  "techs": []
                }
              ],
              "failure_reason": "Neither the next hop IP address nor the output interface has been discovered by NetBrain.",
              "status": "Failed",
              "category": "Lack of related information",
              "error_code": 423,
              "priority": 2
            }
          ],
          "failure_reasons": [],
          "path_name": "L3 Path",
          "description": "192.168.0.197 -> 192.168.0.61",
          "status": "Success"
        }
      ],
      "failure_reasons": [],
      "status": "Success"
    }
  ],
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
taskID = "498c10a7-0011-4a59-a4cd-0258af3edd19"

token = "c4edcb21-8d27-42a3-be0c-7e3b53b608c7"
nb_url = "http://192.168.28.79"
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Path/Calculation/" + str(taskID) + "/Result"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

try:
    response = requests.get(full_url, headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        
        print ("Failed to Get Path Calculation Overview! - " + str(response.text))
    
except Exception as e:
    print (str(e)) 
```
```python
{"path_overview":[{"path_list":[{"branch_list":[{"hop_detail_list":[{"fromDev":{"devId":"02ef8cd1-27be-414f-bd86-dc62c660b881","devName":"192.168.0.197","devType":1005,"domainId":""},"fromIntf":{"intfKeyObj":{"schema":"intfs._id","value":"5da2f88e-3560-485b-bfaf-04b328117d49"},"intfDisplaySchemaObj":{"schema":"intfs.name","value":"Ethernet0"},"PhysicalInftName":"Ethernet0","ipLoc":""},"hopId":"208cb446-e1c9-4f07-a31a-d47f46fdca5b","isComplete":false,"isP2P":false,"mediaId":"fa8111b9-60d5-4925-9607-b88d4eced2ef","mediaInfo":{"mediaName":"192.168.0.0/22\r\nVRRP: 0(192.168.0.64)","mediaType":"Lan","neat":false,"topoType":"L3_Topo_Type"},"preHopId":"00000000-0000-0000-0000-000000000000","sequnce":0,"toIntf":{"intfKeyObj":{"schema":"ipIntfs._id","value":"8aa76b0a-e05a-4dda-9002-aba19d3bdecf"},"intfDisplaySchemaObj":{"schema":"ipIntfs.name","value":"Mgmt 192.168.0.61/22"},"PhysicalInftName":"Mgmt","ipLoc":"192.168.0.61/22"},"toDev":{"devId":"02630588-1871-4f66-b229-50d0a2f20449","devName":"CP_HA1","devType":30080,"domainId":""},"topoType":"L3_Topo_Type","trafficState":{"acl":"","alg":-1,"dev_name":"192.168.0.197","dev_type":1005,"in_intf":"Ethernet0","in_intf_schema":"intfs","in_intf_topo_type":"L3_Topo_Type","next_dev_in_intf":"Mgmt 192.168.0.61/22","next_dev_in_intf_schema":"ipIntfs","next_dev_in_intf_topo_type":"L3_Topo_Type","next_dev_name":"CP_HA1","next_dev_type":30080,"next_hop_ip":"192.168.0.61","next_hop_mac":"","out_intf":"Ethernet0","out_intf_schema":"intfs","out_intf_topo_type":"L3_Topo_Type","pbr":"","vrf":""},"parentHopId":"","isGateway":false,"techs":[]},{"fromDev":{"devId":"02630588-1871-4f66-b229-50d0a2f20449","devName":"CP_HA1","devType":30080,"domainId":""},"fromIntf":{"intfKeyObj":{"schema":"","value":""},"intfDisplaySchemaObj":{"schema":"","value":""},"PhysicalInftName":"","ipLoc":""},"hopId":"a457dbfa-66fd-4608-b881-bf13e6dd56af","isComplete":false,"isP2P":false,"mediaId":"","mediaInfo":{"mediaName":"","mediaType":"","neat":false,"topoType":""},"preHopId":"208cb446-e1c9-4f07-a31a-d47f46fdca5b","sequnce":1,"toIntf":{"intfKeyObj":{"schema":"","value":""},"intfDisplaySchemaObj":{"schema":"","value":""},"PhysicalInftName":"","ipLoc":""},"toDev":{"devId":"","devName":"","devType":0,"domainId":""},"topoType":"","trafficState":{"acl":"","alg":-1,"dev_name":"CP_HA1","dev_type":30080,"in_intf":"Mgmt 192.168.0.61/22","in_intf_schema":"ipIntfs","in_intf_topo_type":"L3_Topo_Type","next_dev_in_intf":"","next_dev_in_intf_schema":"","next_dev_in_intf_topo_type":"","next_dev_name":"","next_dev_type":0,"next_hop_ip":"","next_hop_mac":"","out_intf":"","out_intf_schema":"","out_intf_topo_type":"","pbr":"","vrf":""},"parentHopId":"","isGateway":false,"techs":[]}],"failure_reason":"","status":"Success","category":"","error_code":-1,"priority":0},{"hop_detail_list":[{"fromDev":{"devId":"02ef8cd1-27be-414f-bd86-dc62c660b881","devName":"192.168.0.197","devType":1005,"domainId":""},"fromIntf":{"intfKeyObj":{"schema":"intfs._id","value":"5da2f88e-3560-485b-bfaf-04b328117d49"},"intfDisplaySchemaObj":{"schema":"intfs.name","value":"Ethernet0"},"PhysicalInftName":"Ethernet0","ipLoc":""},"hopId":"e38cc13f-147a-44d6-962f-535b734f92b3","isComplete":false,"isP2P":false,"mediaId":"fa8111b9-60d5-4925-9607-b88d4eced2ef","mediaInfo":{"mediaName":"192.168.0.0/22\r\nVRRP: 0(192.168.0.64)","mediaType":"Lan","neat":false,"topoType":"L3_Topo_Type"},"preHopId":"00000000-0000-0000-0000-000000000000","sequnce":0,"toIntf":{"intfKeyObj":{"schema":"ipIntfs._id","value":"d6c271e0-f647-4cf3-bc78-8fe40bc28abb"},"intfDisplaySchemaObj":{"schema":"ipIntfs.name","value":"Mgmt 192.168.0.62/22"},"PhysicalInftName":"Mgmt","ipLoc":"192.168.0.62/22"},"toDev":{"devId":"17f64621-642a-42f1-a7bd-aae287ceecf2","devName":"CP_HA2","devType":30080,"domainId":""},"topoType":"L3_Topo_Type","trafficState":{"acl":"","alg":-1,"dev_name":"192.168.0.197","dev_type":1005,"in_intf":"Ethernet0","in_intf_schema":"intfs","in_intf_topo_type":"L3_Topo_Type","next_dev_in_intf":"Mgmt 192.168.0.62/22","next_dev_in_intf_schema":"ipIntfs","next_dev_in_intf_topo_type":"L3_Topo_Type","next_dev_name":"CP_HA2","next_dev_type":30080,"next_hop_ip":"192.168.0.62","next_hop_mac":"","out_intf":"Ethernet0","out_intf_schema":"intfs","out_intf_topo_type":"L3_Topo_Type","pbr":"","vrf":""},"parentHopId":"","isGateway":false,"techs":[]},{"fromDev":{"devId":"17f64621-642a-42f1-a7bd-aae287ceecf2","devName":"CP_HA2","devType":30080,"domainId":""},"fromIntf":{"intfKeyObj":{"schema":"","value":""},"intfDisplaySchemaObj":{"schema":"","value":""},"PhysicalInftName":"","ipLoc":""},"hopId":"193c9332-dabe-49ea-be40-59fdac9a8fb4","isComplete":false,"isP2P":false,"mediaId":"","mediaInfo":{"mediaName":"","mediaType":"","neat":false,"topoType":""},"preHopId":"e38cc13f-147a-44d6-962f-535b734f92b3","sequnce":1,"toIntf":{"intfKeyObj":{"schema":"","value":""},"intfDisplaySchemaObj":{"schema":"","value":""},"PhysicalInftName":"","ipLoc":""},"toDev":{"devId":"","devName":"","devType":0,"domainId":""},"topoType":"","trafficState":{"acl":"","alg":-1,"dev_name":"CP_HA2","dev_type":30080,"in_intf":"Mgmt 192.168.0.62/22","in_intf_schema":"ipIntfs","in_intf_topo_type":"L3_Topo_Type","next_dev_in_intf":"","next_dev_in_intf_schema":"","next_dev_in_intf_topo_type":"L3_Topo_Type","next_dev_name":"","next_dev_type":0,"next_hop_ip":"","next_hop_mac":"","out_intf":"","out_intf_schema":"","out_intf_topo_type":"L3_Topo_Type","pbr":"","vrf":""},"parentHopId":"","isGateway":false,"techs":[]}],"failure_reason":"Neither the next hop IP address nor the output interface has been discovered by NetBrain.","status":"Failed","category":"Lack of related information","error_code":423,"priority":2}],"failure_reasons":[],"path_name":"L3 Path","description":"192.168.0.197 -> 192.168.0.61","status":"Success"},{"branch_list":[{"hop_detail_list":[{"fromDev":{"devId":"02ef8cd1-27be-414f-bd86-dc62c660b881","devName":"192.168.0.197","devType":1005,"domainId":""},"fromIntf":{"intfKeyObj":{"schema":"intfs._id","value":"5da2f88e-3560-485b-bfaf-04b328117d49"},"intfDisplaySchemaObj":{"schema":"intfs.name","value":"Ethernet0"},"PhysicalInftName":"Ethernet0","ipLoc":""},"hopId":"03ba7a81-fd02-46e9-ad93-9dbf68131668","isComplete":false,"isP2P":true,"mediaId":"","mediaInfo":{"mediaName":"","mediaType":"","neat":false,"topoType":""},"preHopId":"00000000-0000-0000-0000-000000000000","sequnce":0,"toIntf":{"intfKeyObj":{"schema":"intfs._id","value":"567e877a-a726-4039-9e25-9c961afc2dab"},"intfDisplaySchemaObj":{"schema":"intfs.name","value":"GigabitEthernet1/0/5"},"PhysicalInftName":"GigabitEthernet1/0/5","ipLoc":""},"toDev":{"devId":"fe7a50a7-4ce9-4220-aee9-df1fe43b1168","devName":"ACI-QA-SW1","devType":2001,"domainId":""},"topoType":"L2_Topo_Type","trafficState":{"acl":"","alg":-1,"dev_name":"192.168.0.197","dev_type":1005,"in_intf":"","in_intf_schema":"","in_intf_topo_type":"","next_dev_in_intf":"GigabitEthernet1/0/5","next_dev_in_intf_schema":"intfs","next_dev_in_intf_topo_type":"L2_Topo_Type","next_dev_name":"ACI-QA-SW1","next_dev_type":2001,"next_hop_ip":"","next_hop_mac":"","out_intf":"Ethernet0","out_intf_schema":"intfs","out_intf_topo_type":"L2_Topo_Type","pbr":"","vrf":""},"parentHopId":"208cb446-e1c9-4f07-a31a-d47f46fdca5b","isGateway":false,"techs":[]},{"fromDev":{"devId":"fe7a50a7-4ce9-4220-aee9-df1fe43b1168","devName":"ACI-QA-SW1","devType":2001,"domainId":""},"fromIntf":{"intfKeyObj":{"schema":"","value":""},"intfDisplaySchemaObj":{"schema":"","value":""},"PhysicalInftName":"","ipLoc":""},"hopId":"f484faf8-92cb-4f8b-8340-eb8f909c66c7","isComplete":false,"isP2P":false,"mediaId":"","mediaInfo":{"mediaName":"","mediaType":"","neat":false,"topoType":""},"preHopId":"03ba7a81-fd02-46e9-ad93-9dbf68131668","sequnce":1,"toIntf":{"intfKeyObj":{"schema":"","value":""},"intfDisplaySchemaObj":{"schema":"","value":""},"PhysicalInftName":"","ipLoc":""},"toDev":{"devId":"","devName":"","devType":0,"domainId":""},"topoType":"","trafficState":{"acl":"","alg":-1,"dev_name":"ACI-QA-SW1","dev_type":2001,"in_intf":"GigabitEthernet1/0/5","in_intf_schema":"intfs","in_intf_topo_type":"L2_Topo_Type","next_dev_in_intf":"","next_dev_in_intf_schema":"","next_dev_in_intf_topo_type":"","next_dev_name":"","next_dev_type":0,"next_hop_ip":"","next_hop_mac":"","out_intf":"","out_intf_schema":"","out_intf_topo_type":"","pbr":"","vrf":""},"parentHopId":"208cb446-e1c9-4f07-a31a-d47f46fdca5b","isGateway":false,"techs":[]}],"failure_reason":"Output interface was not found","status":"Failed","category":"Lack of related information","error_code":426,"priority":2}],"failure_reasons":[],"path_name":"L2 Path","description":"192.168.0.197 -> 192.168.0.61","status":"Failed"},{"branch_list":[{"hop_detail_list":[{"fromDev":{"devId":"02ef8cd1-27be-414f-bd86-dc62c660b881","devName":"192.168.0.197","devType":1005,"domainId":""},"fromIntf":{"intfKeyObj":{"schema":"intfs._id","value":"5da2f88e-3560-485b-bfaf-04b328117d49"},"intfDisplaySchemaObj":{"schema":"intfs.name","value":"Ethernet0"},"PhysicalInftName":"Ethernet0","ipLoc":""},"hopId":"f6123b62-9a6b-48d6-8420-1aea4652c45e","isComplete":false,"isP2P":true,"mediaId":"","mediaInfo":{"mediaName":"","mediaType":"","neat":false,"topoType":""},"preHopId":"00000000-0000-0000-0000-000000000000","sequnce":0,"toIntf":{"intfKeyObj":{"schema":"intfs._id","value":"567e877a-a726-4039-9e25-9c961afc2dab"},"intfDisplaySchemaObj":{"schema":"intfs.name","value":"GigabitEthernet1/0/5"},"PhysicalInftName":"GigabitEthernet1/0/5","ipLoc":""},"toDev":{"devId":"fe7a50a7-4ce9-4220-aee9-df1fe43b1168","devName":"ACI-QA-SW1","devType":2001,"domainId":""},"topoType":"L2_Topo_Type","trafficState":{"acl":"","alg":-1,"dev_name":"192.168.0.197","dev_type":1005,"in_intf":"","in_intf_schema":"","in_intf_topo_type":"","next_dev_in_intf":"GigabitEthernet1/0/5","next_dev_in_intf_schema":"intfs","next_dev_in_intf_topo_type":"L2_Topo_Type","next_dev_name":"ACI-QA-SW1","next_dev_type":2001,"next_hop_ip":"","next_hop_mac":"","out_intf":"Ethernet0","out_intf_schema":"intfs","out_intf_topo_type":"L2_Topo_Type","pbr":"","vrf":""},"parentHopId":"e38cc13f-147a-44d6-962f-535b734f92b3","isGateway":false,"techs":[]},{"fromDev":{"devId":"fe7a50a7-4ce9-4220-aee9-df1fe43b1168","devName":"ACI-QA-SW1","devType":2001,"domainId":""},"fromIntf":{"intfKeyObj":{"schema":"","value":""},"intfDisplaySchemaObj":{"schema":"","value":""},"PhysicalInftName":"","ipLoc":""},"hopId":"88c13efc-6237-4372-836e-654e7b23bd14","isComplete":false,"isP2P":false,"mediaId":"","mediaInfo":{"mediaName":"","mediaType":"","neat":false,"topoType":""},"preHopId":"f6123b62-9a6b-48d6-8420-1aea4652c45e","sequnce":1,"toIntf":{"intfKeyObj":{"schema":"","value":""},"intfDisplaySchemaObj":{"schema":"","value":""},"PhysicalInftName":"","ipLoc":""},"toDev":{"devId":"","devName":"","devType":0,"domainId":""},"topoType":"","trafficState":{"acl":"","alg":-1,"dev_name":"ACI-QA-SW1","dev_type":2001,"in_intf":"GigabitEthernet1/0/5","in_intf_schema":"intfs","in_intf_topo_type":"L2_Topo_Type","next_dev_in_intf":"","next_dev_in_intf_schema":"","next_dev_in_intf_topo_type":"","next_dev_name":"","next_dev_type":0,"next_hop_ip":"","next_hop_mac":"","out_intf":"","out_intf_schema":"","out_intf_topo_type":"","pbr":"","vrf":""},"parentHopId":"e38cc13f-147a-44d6-962f-535b734f92b3","isGateway":false,"techs":[]}],"failure_reason":"Output interface was not found","status":"Failed","category":"Lack of related information","error_code":426,"priority":2}],"failure_reasons":[],"path_name":"L2 Path","description":"192.168.0.197 -> 192.168.0.62","status":"Failed"}],"failure_reasons":[],"status":"Success"}],"statusCode":790200,"statusDescription":"Success."}
```

# cURL Code from Postman:
```python
curl -X GET \
  http://192.168.28.173/ServicesAPI/API/V1/CMDB/Path/Calculation/dcf25655-81a9-4cfe-82ca-aef80a698971/OverView \
  -H 'Accept: */*' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Host: 192.168.28.173' \
  -H 'Postman-Token: b0cd60b6-d29d-4665-9469-8969c925ee92,c4d2df42-2573-402b-8327-174c45ee1356' \
  -H 'User-Agent: PostmanRuntime/7.13.0' \
  -H 'accept-encoding: gzip, deflate' \
  -H 'cache-control: no-cache' \
  -H 'token: db5757cb-aaa6-4efb-ad25-ce4918def0ce'
```
