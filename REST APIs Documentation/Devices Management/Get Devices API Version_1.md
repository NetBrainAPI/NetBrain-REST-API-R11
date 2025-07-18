
# Devices API Design

## GET /V1/CMDB/Devices

This API is used to get devices and their attributes data in batch. The response of this API returns a list in JSON format.<br><br>**Note:<br>1. The API follows the privilege control of NB system. If there is restriction set by Access Control Policy for the target querying resources, the response will not return queried data.<br>2. This API doesn't support any GDR that is not set as displayed, except first discovery time and last discovery time.**<br><br>
<b>Important</b>: It is recommended to pass parameter <i>version=1</i> instead of <i>version=0</i>

## Detail Information

>**Title:** Get Devices API

>**Version:** 02/28/2023

>**API Server URL:** http(s)://IP Address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Devices

>**Authentication:**

|**Type**|**In**|**Name**|
|------|------|------|
|Bearer Authentication|Headers|Authentication token|

## Request body (*required)

>No request body.

## Query Parameters (*required)

|**Name**|**Type**|**Description**|
|------|------|------|
|||`*` - indicates mandatory field <br> `^` - indicates optional field|
|hostname|string OR list of string|A list of device hostnames|
|ignoreCase|boolean|Recognizes as case-insensitive hostname|
|ip|string OR list of string|A list of device management IPs|
|||If provided with both of `hostname` and `ip`, `hostname` has higher priority. If any of the devices are not found from the provided query parameter, API returns the found devices as a list in response and add another json key `deviceNotFound`, the value is a mixed list of hostnames and IPs that are not found.|
|*fullattr|integer|`0` (default) - return basic device attributes (device id, management IP, hostname, device type, first discovery time, last discovery time).<br>`1` - return all device attributes, including customized attributes|
|*version|string| `0` (default) - returns basic device attributes (device id, mgmt ip, hostname, device type, first discovery time, last discovery time) <br> `1` - returns all device properties<br It is recommended to pass version=1.|
|skip|integer|The amount of records to be skipped. <br>The value cannot be negative.  <br>If the value is negative, API throws exception `{"statusCode":791001,"statusDescription":"Parameter 'skip' cannot be negative"}`. <br>No upper bound for this parameter.|
|limit|integer|The up limit amount of device records to return per API call. <br>The value cannot be negative. <br>If the value is negative, API throws exception `{"statusCode":791001,"statusDescription":"Parameter 'limit' cannot be negative"}`. <br>No upper bound for this parameter. If the parameter is not specified in API call, it means there is not limitation setting on the call.|
|||If only `skip` value is provided, returns the device list with 50 devices information start from the skip number. <br>If only `limit` value is provided, returns from the first device in DB. <br>If both `skip` and `limit` values are provided, returns as required. <br>Error exceptions follows each parameter's description.<br>`Skip` and `limit` parameters are based on the search result from DB. The `limit` value's valid range is 10 - 100; if the assigned value exceeds the range, the server will respond with an error message: `Parameter 'limit' must be greater than or equal to 10 and less than or equal to 100.`  |
|filter|json|If specified, returns the matched device list with device attributes. <br>Supported filtering attributes: `name`, `assetTag`, `contact`, `descr`, `layer`, `loc`, `mgmtIP`, `model`, `site` (complete site path; e.g. `"My Network\\\Burlington"`), `sn`, `subTypeName`, `vendor`, `ver`, `hasBGPConfig`, `hasOSPFConfig`, `hasEIGRPConfig`, `hasISISConfig`, `hasMulticastConfig`, `hasOTVConfig`, `isHA`, `hasBPEConfig`, `isTransparent`, `isCluster`, `hasVXLANConfig`, `hasVPLSConfig`, `alias` (the alias name of device Telnet/SSH settings)|
|||Only supports AND operator, when multiple filter attributes are specified in JSON.<br>If provided with invalid data format, returns error `invalid filter input`.|

## Headers

>**Data Format Headers**

|**Name**|**Type**|**Description**|
|------|------|------|
|Content-Type|string|support "application/json"|
|Accept|string|support "application/json"|

>**Authorization Headers**

|**Name**|**Type**|**Description**|
|------|------|------|
|token|string|Authentication token, get from login API.|

## Response
** Note that the response will differ based on the parameter. 

|**Name**|**Type**|**Description**|
|------|------|------|
|devices|string[]|A list of devices.|
|devices.id|string|The device ID.|
|devices.mgmtIP|string|The management IP address of the returned device.|
|devices.hostname|string|The hostname of returned device.|
|devices.deviceTypeName|string|The type of the returned device; e.g. Cisco Router|
|devices.customAttribute1|Refer to GDR data type|Customized Attribute 1.|
|devices.customAttribute2|Refer to GDR data type|Customized Attribute 2.|
|devices.firstDiscoverTime|time|First discovery time of device.|
|devices.lastDiscoverTime|time|Last discovery time of device.|
|...|...|...|
|statusCode|integer|Code issued by NetBrain server indicating the execution result.|
|statusDescription|string|The explanation of the status code.|


# Full Example:

# Example 1
```python
# import python modules 
import requests
import time
import urllib3
import pprint
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "13c7ed6e-781d-4b22-83e7-b1722de4e31d"
nb_url = "http://192.168.28.79"

full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Devices"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"]=token

data = {
    "version": 1,
    "hostname":'IPv6Lab-MPLS',
    "ip": '2020:1111:abcd:ef23:4567:8912:3333:4444',
}


try:
    response = requests.get(full_url, params = data, headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print("Get Devices failed! - " + str(response.text))
except Exception as e:
    print (str(e)) 
```
```python
{
  "devices": [
    {
      "id": "39090c12-981d-4e42-9e9d-ea84ef0837e1",
      "mgmtIP": "2020:1111:abcd:ef23:4567:8912:3333:4444",
      "name": "IPv6Lab-MPLS",
      "subTypeName": "Cisco Router",
      "fDiscoveryTime": "2023-08-21T17:10:52Z",
      "lDiscoveryTime": "2023-08-24T10:42:42Z"
    }
  ],
  "statusCode": 790200,
  "statusDescription": "Success."
}
```

# Example 2: Using `version=0`; it is not recommended to use version=0
```python
# import python modules 
import requests
import time
import urllib3
import pprint
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "13c7ed6e-781d-4b22-83e7-b1722de4e31d"
nb_url = "http://192.168.28.79"

full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Devices"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"]=token

data = {
    "fullattr":1,
    "version": 0
}


try:
    response = requests.get(full_url, params = data, headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print("Get Devices failed! - " + str(response.text))
except Exception as e:
    print (str(e)) 
```
```python
{
  "devices": [
    {
      "id": "ec7cf947-4d66-44f6-bdfc-33454c44cd70",
      "mgmtIP": "10.61.164.6",
      "hostname": "MRFN-CAMCC-F5-AIS-PROD2",
      "deviceTypeName": "F5 Load Balancer",
      "firstDiscoverTime": "2023-01-21T16:56:24Z",
      "lastDiscoverTime": "2024-03-19T16:26:48Z"
    },
    {
      "id": "26ee70e7-9c8d-4d24-86dd-06d3570eb330",
      "mgmtIP": "10.240.246.61",
      "hostname": "mrfn-cascc-f5-ag02-prd",
      "deviceTypeName": "F5 Load Balancer",
      "firstDiscoverTime": "2023-02-27T16:28:55Z",
      "lastDiscoverTime": "2024-04-24T16:00:20Z"
    },
    {
      "id": "43704ff9-2c37-4f3e-9e5a-a51983677976",
      "mgmtIP": "10.65.116.25",
      "hostname": "ALCSWAVG310P01",
      "deviceTypeName": "Cisco Voice Gateway",
      "firstDiscoverTime": "2022-10-21T13:27:16Z",
      "lastDiscoverTime": "2024-08-18T21:00:51Z"
    },
    {
      "id": "0c4e38fd-6c2d-4f15-a4e3-77274e106b41",
      "mgmtIP": "192.168.32.100",
      "hostname": "ST55CN234C",
      "deviceTypeName": "Arista Switch",
      "firstDiscoverTime": "2024-12-11T10:32:20Z",
      "lastDiscoverTime": "2024-12-11T10:32:20Z"
    },
    {
      "id": "d0d8a3a2-0dfe-4ace-a140-7ef940f9fbce",
      "mgmtIP": "172.24.101.61",
      "hostname": "BJ-3750-1",
      "deviceTypeName": "Cisco IOS Switch",
      "firstDiscoverTime": "2025-01-03T20:29:36Z",
      "lastDiscoverTime": "2025-01-03T20:38:02Z"
    }
  ],
  "statusCode": 790200,
  "statusDescription": "Success."
}
```

# Example 3: Get All Devices

```python
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Devices"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"]=token
skip = 0
count = 50
try:
    while count == 50:
        data = {
            "version": 1,
            "skip":skip,
            "fullattr":1
        }
        response = requests.get(full_url, params = data, headers = headers, verify = False)
        if response.status_code == 200:
            result = response.json()
            count = len(result["devices"])
            skip = skip + count
            print (result)
        else:
            print("Get Devices failed! - " + str(response.text))
except Exception as e:
    print (str(e)) 
```
```python
{
  "devices": [
    {
      "name": "ALCSWAVG310P01",
      "mgmtIP": "10.65.116.25",
      "mgmtIntf": "GigabitEthernet0/0",
      "subTypeName": "Cisco Voice Gateway",
      "vendor": "Cisco",
      "model": "VG310",
      "ver": "15.9(3)M6",
      "sn": "FJC2134A07N",
      "site": "My Network\\Unassigned",
      "loc": "",
      "contact": "",
      "mem": "864503964",
      "os": "",
      "assetTag": "",
      "layer": "",
      "descr": "",
      "oid": "1.3.6.1.4.1.9.1.1769",
      "driverName": "Cisco Voice Gateway",
      "fDiscoveryTime": "2022-10-21T13:27:16Z",
      "lDiscoveryTime": "2024-08-18T21:00:51Z",
      "assignTags": "",
      "policyGroup": "",
      "hasEIGRPConfig": false,
      "hasBGPConfig": false,
      "hasOSPFConfig": false,
      "hasISISConfig": false,
      "hasMulticastConfig": false,
      "BPE": "",
      "OTV": "",
      "l3vniVrf": "",
      "cluster": "",
      "VXLAN": "",
      "VPLS": "",
      "vADCs": "",
      "_nb_features": "",
      "bgpNeighbor": "",
      "ap_mode": "",
      "APMeshRole": "",
      "snmpName": "ALCSWAVG310P01.pmusa.net",
      "vADId": "",
      "vADCid": "",
      "ciscoContractId": "",
      "ciscoBasePid": "",
      "module_serial": "",
      "id": "43704ff9-2c37-4f3e-9e5a-a51983677976"
    },
    {
      "name": "BJ-3750-1",
      "mgmtIP": "172.24.101.61",
      "mgmtIntf": "Vlan10",
      "subTypeName": "Cisco IOS Switch",
      "vendor": "Cisco",
      "model": "catalyst37xxStack",
      "ver": "",
      "sn": "",
      "site": "My Network\\Unassigned",
      "loc": "",
      "contact": "",
      "mem": "",
      "os": "",
      "assetTag": "",
      "layer": "",
      "descr": "",
      "oid": "1.3.6.1.4.1.9.1.516",
      "driverName": "Cisco IOS Switch",
      "fDiscoveryTime": "2025-01-03T20:29:36Z",
      "lDiscoveryTime": "2025-01-03T20:38:02Z",
      "assignTags": "",
      "policyGroup": "",
      "hasEIGRPConfig": false,
      "hasBGPConfig": false,
      "hasOSPFConfig": true,
      "hasISISConfig": false,
      "hasMulticastConfig": false,
      "BPE": "",
      "OTV": "",
      "l3vniVrf": "",
      "cluster": "",
      "VXLAN": "",
      "VPLS": "",
      "vADCs": "",
      "hasLISPConfig": false,
      "_nb_features": "",
      "bgpNeighbor": "",
      "ap_mode": "",
      "APMeshRole": "",
      "snmpName": "BJ-3750-1",
      "vADId": "",
      "vADCid": "",
      "ciscoContractId": "",
      "ciscoBasePid": "",
      "module_serial": "",
      "id": "d0d8a3a2-0dfe-4ace-a140-7ef940f9fbce"
    },
    {
      "name": "EX2200-2",
      "mgmtIP": "192.168.32.100",
      "mgmtIntf": "",
      "subTypeName": "Juniper EX Switch",
      "vendor": "",
      "model": "",
      "ver": "",
      "sn": "CW0213350716",
      "site": "My Network\\Unassigned",
      "loc": "",
      "contact": "",
      "mem": "",
      "os": "",
      "assetTag": "",
      "layer": "",
      "descr": "",
      "oid": "",
      "driverName": "Juniper EX Switch",
      "fDiscoveryTime": "2024-09-09T18:02:29Z",
      "lDiscoveryTime": "2024-09-09T18:02:29Z",
      "assignTags": "",
      "policyGroup": "",
      "hasIPv6Config": true,
      "hasEIGRPConfig": false,
      "hasBGPConfig": false,
      "hasOSPFConfig": false,
      "hasISISConfig": false,
      "hasMulticastConfig": false,
      "BPE": "",
      "OTV": "",
      "l3vniVrf": "",
      "cluster": "",
      "VXLAN": "",
      "VPLS": "",
      "vADCs": "",
      "virtualTechnology": "",
      "childDevices": "",
      "_nb_features": "",
      "bgpNeighbor": "",
      "ap_mode": "",
      "APMeshRole": "",
      "snmpName": "",
      "vADId": "",
      "vADCid": "",
      "module_serial": "",
      "id": "858c319c-ace5-4468-9031-c10a536922ec"
    }
  ],
  "statusCode": 790200,
  "statusDescription": "Success."
}
```


# Example 4: Using `limit`
```python
token = "c3d73da6-aa56-4cc7-bc20-f72788a4badc"

def getdevicev1():
    full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Devices"
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    headers["Token"]=token
    skip = 0
    count = 100
    try:
        while count == 100:
            data = {
                "version": 1,
                "skip":skip,
                "fullattr":1,
                'limit' : count
            }
            response = requests.get(full_url, params = data, headers = headers, verify = False)
            if response.status_code == 200:
                result = response.json()
                count = len(result["devices"])
                skip = skip + count
                ss = "" 
                for device in result["devices"]:
                    #break
                    ss += '{},'.format(device['name'])
                print(ss)
            else:
                print("Get Devices failed! - " + str(response.text))
            #break
    except Exception as e:
        print (str(e))
        
result = getdevicev1()
result
```

```
ALCSWAVG310P01,BJ-3750-1,EX2200-2,JMCKOPVG310P01,MRFN-CAMCC-F5-AIS-PROD2,ST55CN234C,mgd-pcm-wdc-fw01/vsys2,mrfn-cascc-f5-ag02-prd,
```


# Example 5: Using `filter`

```python
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Devices"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"]=token
filter1 = {
    "name":"EX2200-2"
}

data = {
    "version": 1,
    "limit" : 15,
    "fullattr" : 1,
    "filter" : json.dumps(filter1)
}


try:
    response = requests.get(full_url, params = data, headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print("Get Devices failed! - " + str(response.text))
except Exception as e:
    print (str(e)) 

```
```python
{
  "devices": [
    {
      "name": "EX2200-2",
      "mgmtIP": "192.168.32.100",
      "mgmtIntf": "",
      "subTypeName": "Juniper EX Switch",
      "vendor": "",
      "model": "",
      "ver": "",
      "sn": "CW0213350716",
      "site": "My Network\\Unassigned",
      "loc": "",
      "contact": "",
      "mem": "",
      "os": "",
      "assetTag": "",
      "layer": "",
      "descr": "",
      "oid": "",
      "driverName": "Juniper EX Switch",
      "fDiscoveryTime": "2024-09-09T18:02:29Z",
      "lDiscoveryTime": "2024-09-09T18:02:29Z",
      "assignTags": "",
      "policyGroup": "",
      "hasIPv6Config": true,
      "hasEIGRPConfig": false,
      "hasBGPConfig": false,
      "hasOSPFConfig": false,
      "hasISISConfig": false,
      "hasMulticastConfig": false,
      "BPE": "",
      "OTV": "",
      "l3vniVrf": "",
      "cluster": "",
      "VXLAN": "",
      "VPLS": "",
      "vADCs": "",
      "virtualTechnology": "",
      "childDevices": "",
      "_nb_features": "",
      "bgpNeighbor": "",
      "ap_mode": "",
      "APMeshRole": "",
      "snmpName": "",
      "vADId": "",
      "vADCid": "",
      "module_serial": "",
      "id": "858c319c-ace5-4468-9031-c10a536922ec"
    }
  ],
  "statusCode": 790200,
  "statusDescription": "Success."
}
```


# cURL Code from Postman:
This cURL command is based on Example 1

```python
curl -X GET \
  'http://192.168.32.17/ServicesAPI/API/V1/CMDB/Devices?ip=&fullattr=1&version=1' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Cache-Control: no-cache' \
  -H 'token: 4056241d-948b-478e-93e6-d0edc5774120'
```
