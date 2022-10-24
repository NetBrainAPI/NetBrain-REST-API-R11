
# Benchmark API Design

## ***POST*** /V1/CMDB/Benchmark/Result/DeviceInfo

Use this API to get failed device detail information by device name.

## Detail Information

> **Title** : Get Benchmark Run Result Device Detail API<br>

> **Version** : 05/16/2022.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Benchmark/Result/DeviceInfo


> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|task | string  | The name of the task.  |
|runId | string  | optional, ID of the execution. If null, the API will return last run result  |
|devices | list of string  | List of device name  |

## Parameters(****required***)

> No parameters required.

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
|deviceInfos| list of Object | List of benchmark device detail   |
|deviceInfos.deviceId| String | Device ID   |
|deviceInfos.deviceName| String | Device Name   |
|deviceInfos.arpTable| String | ARP table retrieval status   |
|deviceInfos.cdpTable| String | CDP table retrieval status   |
|deviceInfos.bgpNbrTable| String | BGP Neighbor table retrieval status   |
|deviceInfos.stpTable| String | STP table retrieval status   |
|deviceInfos.macTable| String | MAC table retrieval status   |
|deviceInfos.config| String | Configuration retrieval status   |
|deviceInfos.cliConfig| String | CLI configuration retrieval status   |
|deviceInfos.routeTable| String | Route table retrieval status   |
|deviceInfos.deviceInfo| String | Device information retrieval status   |
|deviceInfos.interfaceInfo| String | Interface information retrieval status   |
|deviceInfos.nctTable| list of Object | List of NCT table retrieval status   |

> ***Example***


```python
{
    "deviceInfos": [
        {
            "deviceId": "450bb1c1-a8d3-4222-881e-4e172e80f712",
            "deviceName": "US-BOS-R2",
            "arpTable": "Failed",
            "cdpTable": "Failed",
            "bgpNbrTable": "Failed",
            "stpTable": "N/A",
            "macTable": "Failed",
            "config": "Failed",
            "cliConfig": null,
            "routeTable": "Failed",
            "deviceInfo": "Failed",
            "interfaceInfo": "Failed",
            "nctTable": [
                {
                    "name": "BGP Neighbors",
                    "status": "Failed"
                },
                {
                    "name": "BGP Received Route Table",
                    "status": "Failed"
                },
                {
                    "name": "COOP Endpoint Table",
                    "status": "N/A"
                },
                {
                    "name": "Contract Table",
                    "status": "N/A"
                },
                {
                    "name": "EPG Contract Table",
                    "status": "N/A"
                },
                {
                    "name": "External EPG Mapping Table",
                    "status": "N/A"
                },
                {
                    "name": "FHRP Table",
                    "status": "N/A"
                },
                {
                    "name": "Filter Table",
                    "status": "N/A"
                },
                {
                    "name": "GRE Tunnels",
                    "status": "Succeed"
                },
                {
                    "name": "Global Endpoint Table",
                    "status": "N/A"
                },
                {
                    "name": "HA State",
                    "status": "N/A"
                },
                {
                    "name": "Host Guest Table",
                    "status": "N/A"
                },
                {
                    "name": "IPsec VPN Table",
                    "status": "Succeed"
                },
                {
                    "name": "IPsec VPN Table[Real-time]",
                    "status": "Failed"
                },
                {
                    "name": "IPv6 Route Table",
                    "status": "N/A"
                },
                {
                    "name": "L2VPN Forwarding Table[Real-time]",
                    "status": "N/A"
                },
                {
                    "name": "Ltm Pool Table",
                    "status": "N/A"
                },
                {
                    "name": "MPLS LFIB",
                    "status": "N/A"
                },
                {
                    "name": "MPLS VPNv4 Label",
                    "status": "Failed"
                },
                {
                    "name": "Management Route Table",
                    "status": "N/A"
                },
                {
                    "name": "Multicast Route Table",
                    "status": "Failed"
                },
                {
                    "name": "NAT Table",
                    "status": "N/A"
                },
                {
                    "name": "NAT Table[Real-time]",
                    "status": "N/A"
                },
                {
                    "name": "NHRP Table",
                    "status": "N/A"
                },
                {
                    "name": "NVE VNI Mapping Table",
                    "status": "N/A"
                },
                {
                    "name": "Neighbor Discover Table",
                    "status": "N/A"
                },
                {
                    "name": "OSPF Neighbors",
                    "status": "Failed"
                },
                {
                    "name": "OTV Table[Real-time]",
                    "status": "N/A"
                },
                {
                    "name": "Policy Content",
                    "status": "N/A"
                },
                {
                    "name": "Policy Table",
                    "status": "N/A"
                },
                {
                    "name": "QoS Mapping Table",
                    "status": "N/A"
                },
                {
                    "name": "Service Graph Mapping Table",
                    "status": "N/A"
                },
                {
                    "name": "VLAN VNI Mapping Table",
                    "status": "N/A"
                },
                {
                    "name": "Virtual Server Table",
                    "status": "N/A"
                },
                {
                    "name": "Zone Table",
                    "status": "N/A"
                },
                {
                    "name": "Zoning Rule Priority Table",
                    "status": "N/A"
                },
                {
                    "name": "Zoning Rule Table",
                    "status": "N/A"
                }
            ],
            "log": "2022-09-23 ...",
            "operateInfo": {
                "opUser": "chris.ouyang",
                "opTime": "2022-09-23T04:01:05Z",
                "operateUserName": "chris.ouyang",
                "operateTime": "2022-09-23T04:01:05Z"
            },
            "spendSecond": 54,
            "deviceSubType": 2
        },
        {
            "deviceId": "a82b3308-0e04-4013-8268-df67e70af9e5",
            "deviceName": "US-BOS-R1",
            "arpTable": "Failed",
            "cdpTable": "Failed",
            "bgpNbrTable": "Failed",
            "stpTable": "N/A",
            "macTable": "Failed",
            "config": "Failed",
            "cliConfig": null,
            "routeTable": "Failed",
            "deviceInfo": "Failed",
            "interfaceInfo": "Failed",
            "nctTable": [
                {
                    "name": "BGP Neighbors",
                    "status": "N/A"
                },
                {
                    "name": "BGP Received Route Table",
                    "status": "Failed"
                },
                {
                    "name": "COOP Endpoint Table",
                    "status": "N/A"
                },
                {
                    "name": "Contract Table",
                    "status": "N/A"
                },
                {
                    "name": "EPG Contract Table",
                    "status": "N/A"
                },
                {
                    "name": "External EPG Mapping Table",
                    "status": "N/A"
                },
                {
                    "name": "FHRP Table",
                    "status": "N/A"
                },
                {
                    "name": "Filter Table",
                    "status": "N/A"
                },
                {
                    "name": "GRE Tunnels",
                    "status": "Failed"
                },
                {
                    "name": "Global Endpoint Table",
                    "status": "N/A"
                },
                {
                    "name": "HA State",
                    "status": "N/A"
                },
                {
                    "name": "Host Guest Table",
                    "status": "N/A"
                },
                {
                    "name": "IPsec VPN Table",
                    "status": "N/A"
                },
                {
                    "name": "IPsec VPN Table[Real-time]",
                    "status": "N/A"
                },
                {
                    "name": "IPv6 Route Table",
                    "status": "N/A"
                },
                {
                    "name": "L2VPN Forwarding Table[Real-time]",
                    "status": "Failed"
                },
                {
                    "name": "Ltm Pool Table",
                    "status": "N/A"
                },
                {
                    "name": "MPLS LFIB",
                    "status": "Failed"
                },
                {
                    "name": "MPLS VPNv4 Label",
                    "status": "N/A"
                },
                {
                    "name": "Management Route Table",
                    "status": "N/A"
                },
                {
                    "name": "Multicast Route Table",
                    "status": "Failed"
                },
                {
                    "name": "NAT Table",
                    "status": "Failed"
                },
                {
                    "name": "NAT Table[Real-time]",
                    "status": "Failed"
                },
                {
                    "name": "NHRP Table",
                    "status": "N/A"
                },
                {
                    "name": "NVE VNI Mapping Table",
                    "status": "N/A"
                },
                {
                    "name": "Neighbor Discover Table",
                    "status": "Failed"
                },
                {
                    "name": "OSPF Neighbors",
                    "status": "N/A"
                },
                {
                    "name": "OTV Table[Real-time]",
                    "status": "Failed"
                },
                {
                    "name": "Policy Content",
                    "status": "N/A"
                },
                {
                    "name": "Policy Table",
                    "status": "N/A"
                },
                {
                    "name": "QoS Mapping Table",
                    "status": "N/A"
                },
                {
                    "name": "Service Graph Mapping Table",
                    "status": "N/A"
                },
                {
                    "name": "VLAN VNI Mapping Table",
                    "status": "N/A"
                },
                {
                    "name": "Virtual Server Table",
                    "status": "N/A"
                },
                {
                    "name": "Zone Table",
                    "status": "N/A"
                },
                {
                    "name": "Zoning Rule Priority Table",
                    "status": "N/A"
                },
                {
                    "name": "Zoning Rule Table",
                    "status": "N/A"
                }
            ],
            "log": "2022-09-23 ...",
            "operateInfo": {
                "opUser": "chris.ouyang",
                "opTime": "2022-09-23T04:01:56Z",
                "operateUserName": "chris.ouyang",
                "operateTime": "2022-09-23T04:01:56Z"
            },
            "spendSecond": 55,
            "deviceSubType": 2
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
import json

# Set the request inputs
url = "https://192.168.28.79/ServicesAPI/API/V1/CMDB/Benchmark/Result/DeviceInfo"

payload = json.dumps({
    "task": "Basic System Benchmark,
    "runId":"",
    "devices": ["US-BOS-R1","US-BOS-R2"]
    })
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'db3bd646-c480-4cfa-9d59-2e556e22555b'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```    

# cURL Code from Postman

```python
curl --location --request POST 'https://integrationlab.netbraintech.com/ServicesAPI/API/V1/CMDB/Benchmark/Result/DeviceInfo' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: db3bd646-c480-4cfa-9d59-2e556e22555b' \
--data-raw '{
    "task": "Basic System Benchmark",
    "runId":"",  //optional, if null will return last run result
    "devices": [
        "US-BOS-R1",
        "US-BOS-R2"
    ]
}'
```

# Error Examples:


```python

```
