
# Return the devices path results


During current use case, the final goal is to present the path result between two specified devices in current domain. There are a total of 8 REST APIs used in this use case, as shown in following:

1. Import python modules and global variables for sample code.
2. Call login API to get authentication token.
3. Call get_all_accessible_tenants API to get all accessible tenant IDs.
4. Call get_all_accessible_domains API to get all accessible domain IDs in specified tenant.
5. Call specify_a_working_domain API to specified which domain to work with.
6. Call resolve_device_gateway API to get devices gateway information. 
7. Call calculate_path API to get the task ID.
8. Call get_path_result API to get the result of calculation path.
9. Call logout API to log out from current account.

The sequencial of provided APIs is also the sequence of our workflow steps.

***Note***: if users want to find the path results of devices, then the step sequence must be followed. If users call these APIs with a different sequential then there would be no results or some errors would be occured.

## Step Explanation
***1. Import python modules and global variables for sample code.***<br>
> Note: If users try to use this code, please remember to change "nb_url" to users' own working url, along with its following information such as username, password, etc.

***2. Call login API to get authentication token.***<br>
>Same with use case 2, we call the login API with "username" and "password" as inputs in the first step. We receive the authentication token from the response, as one fixed input in following APIs calling. If users get errors when calling this API, please check the API documentation on [Github_login](https://github.com/NetBrainAPI/NetBrain-REST-API-R10.1/blob/10.1.2/REST%20APIs%20Documentation/Authentication%20and%20Authorization/Login%20API.md).

***3. call get_all_accessible_tenants API***
>After we get the token from the previous section, we need to use this token as a key to find all tenants which we have the access authentication. During this step, the most important feature is to get the tenant id of the corresponding tenant which we decide to work in. After running this API successfully, we will get the tenantId of the willing tenant which will be set as another input for next step API calling. If users want to get more details about this API or get errors when calling this API, please check the API documentation on [Github_tenant](https://github.com/NetBrainAPI/NetBrain-REST-API-R10.1/blob/10.1.2/REST%20APIs%20Documentation/Tenants%20and%20Domains%20Management/Get%20All%20Accessible%20Tenants%20API.md) 

***4. call get_all_accessible_domains API.***
>In this section, we are going to find all accessible domains in the corresponding tenant with the tenantId from the previous step. Similar to step 2, during the current API call, we need to decide which domain we'd like to work in, and get the domainId meanwhile to prepare for the next API calling. If users get errors when calling this API, please check the API documentation on [Github_domain](https://github.com/NetBrainAPI/NetBrain-REST-API-R10.1/blob/10.1.2/REST%20APIs%20Documentation/Tenants%20and%20Domains%20Management/Get%20All%20Accessible%20Domains%20API.md) 

***5. call specify_a_working_domain API.***<br>
>After running this step successfully, the full login processes is complete; this means we have joined the Netbrain System by calling APIs (Because we have recorded our tenantId and domainId, if users don't know the ID of corresponding tenant and domain, please fully follow step 1 ~ step 4 in use case 1). As the next step, we will start to use Netbrain functions formally. If users want to get more details about this API or get errors when calling this API, please check the API documentation on [Github_working_domain](https://github.com/NetBrainAPI/NetBrain-REST-API-R10.1/blob/10.1.2/REST%20APIs%20Documentation/Authentication%20and%20Authorization/Specify%20A%20Working%20Domain%20API.md).

***6. call resolve_device_gateway API***
>Since we have specified the hostname of source device and destination device in the beginning, we can call resolve devices gateway API here. To re-iterate, if users want to get path result by calling APIs, then users must follow step 2 sequentially. In this section, we will input the Ips list we got from previous section. After the API runs successfully, we will get a gateway list with some device information which will be required as the input for the next section. If users want to get more details about this API or get errors when calling this API, please check the API documentation on [Github_Gateway](https://github.com/NetBrainAPI/NetBrain-REST-API-R10.1/blob/10.1.2/REST%20APIs%20Documentation/Path%20Management/Resolve%20Device%20Gateway%20API.md)

***7. call calculate_path API***
>In this section, we are going to call the Calculate Path API and set the gateway information list as a input (other inputs are shown in following code cell). When calling this API, users must input the required parameters correctly and follow the format of each inputs examples ([Github_calPath](https://github.com/NetBrainAPI/NetBrain-REST-API-R10.1/blob/10.1.2/REST%20APIs%20Documentation/Path%20Management/Path%20Calculation%20API.md)). After calling this API successfully, we will get the corresponding taskId of gateway information which has been put in. And the taskId is the only required input for next section. If users want to get more details about this API or get errors when calling this API, please check the API documentation on [Github_calPath](https://github.com/NetBrainAPI/NetBrain-REST-API-R10.1/blob/10.1.2/REST%20APIs%20Documentation/Path%20Management/Calculate%20Path%20API.md).

***8. call get_path_result API***
>Now, we attempt to the final functional step of this use case: to get the calculation result of the task with taskId in section 2c. After running the following sample code successfully, we will finally get the path result in a json file. If users want to get more details about this API or get errors when calling this API, please check the API documentation on [Github_pathResult](https://github.com/NetBrainAPI/NetBrain-REST-API-R10.1/blob/10.1.2/REST%20APIs%20Documentation/Path%20Management/Get%20Path%20Calculation%20Result%20API.md). 

***9. call logout API***
>After we get all informations from this case, we have to logout from the Netbrain System.
If users want to get more details about this API or get errors when calling this API, please check the API documentation on [Github_logout](https://github.com/NetBrainAPI/NetBrain-REST-API-R10.1/blob/10.1.2/REST%20APIs%20Documentation/Authentication%20and%20Authorization/Logout%20API.md). 

## Sample Code

### import python modules, global variables 


```python
# import python modules
import requests
import json
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pprint

# Global Variables
nb_url = "http://customer NetBrain environment."
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'} 
TenantName = "tenant name"
DomainName = "domain name"
username = "user name"
password = "password"
source_device = "10.8.30.173"
destination_device = "10.8.1.51"
source_port = None
destination_port = None
protocol = 4
is_live = False
```

### Define calling Functions


```python
# call login API
def login(nb_url, username, password, headers):
    login_URL = nb_url + "/ServicesAPI/API/V1/Session"
    data = {
        "username" : username,      
        "password" : password  
    }
    try:
        # Do the HTTP request
        response = requests.post(login_URL, headers=headers, data = json.dumps(data), verify=False)
        # Check for HTTP codes other than 200
        if response.status_code == 200:
            # Decode the JSON response into a dictionary and use the data
            js = response.json()
            return (js)
        else:
            return ("Get token failed! - " + str(response.text))
    except Exception as e:
        return (str(e))

# call get_all_accessible_tenants API
def get_all_accessible_tenants(nb_url, token, headers):
    Accessible_tenants_url = nb_url + "/ServicesAPI/API/V1/CMDB/Tenants"
    headers["Token"] = token
    try:
        # Do the HTTP request
        response = requests.get(Accessible_tenants_url, headers=headers, verify=False)
        # Check for HTTP codes other than 200
        if response.status_code == 200:
            # Decode the JSON response into a dictionary and use the data
            result = response.json()
            tenants = result["tenants"]   
            return tenants
        else:
            return ("Get tenants failed! - " + str(response.text))
    except Exception as e: return (e)
    
# call get_all_accessible_domains API
def get_all_accessible_domains(nb_url, tenantId, token, headers):
    Accessible_domains_url = nb_url + "/ServicesAPI/API/V1/CMDB/Domains"
    headers["Token"] = token
    data = {"tenantId": tenantId}
    try:
        # Do the HTTP request
        response = requests.get(Accessible_domains_url, params = data, headers=headers, verify=False)
        # Check for HTTP codes other than 200
        if response.status_code == 200:
            # Decode the JSON response into a dictionary and use the data
            result = response.json()
            domains = result["domains"]
            return domains
        else:
            return ("Get domains failed! - " + str(response.text))
    except Exception as e: print (str(e))
        
# call specify_a_working_domain API
def specify_a_working_domain(tenantId, domainId, nb_url, headers, token):
    Specify_a_working_domain_url = nb_url + "/ServicesAPI/API/V1/Session/CurrentDomain"
    headers["Token"] = token
    body = {
        "tenantId": tenantId,
        "domainId": domainId
    }
    
    try:
        # Do the HTTP request
        response = requests.put(Specify_a_working_domain_url, data=json.dumps(body), headers=headers, verify=False)
        # Check for HTTP codes other than 200
        if response.status_code == 200:
            # Decode the JSON response into a dictionary and use the data
            result = response.json()
            return (domainId)
            
        elif response.status_code != 200:
            return ("Login failed! - " + str(response.text))

    except Exception as e: print (str(e))
        
# call resolve device gateway API
def resolve_device_gateway(token, ipOrHost, headers):
    Resolve_Device_Gateway_url = nb_url + "/ServicesAPI/API/V1/CMDB/Path/Gateways"
    headers["Token"] = token
    data = {"ipOrHost":ipOrHost}
    try:
        response = requests.get(Resolve_Device_Gateway_url, params = data, headers = headers, verify = False)
        result = response.json()
        if response.status_code == 200:
            return (result)
        else:
            return ("Create module attribute failed! - " + str(response.text))

    except Exception as e:
        print (str(e))

# call calculate path API
def calculate_path(headers, token, source_device, destination_device, source_port=None, destination_port=None, protocol=4, is_live=False):
    '''
    Args:
        source_port & destination_port - None or 8080, default: None
        protocol - 4 # IP
    '''
    
    Calculate_Path_url = nb_url + "/ServicesAPI/API/V1/CMDB/Path/Calculation"
    headers["Token"] = token

    source_gateway = resolve_device_gateway(token, source_device, headers)
    gateway = {}
    if type(source_gateway) is dict:
        gateway = source_gateway["gatewayList"]
        print ("Detail information of the first gateway in source device: ")
        pprint.pprint(gateway)
        print("")

    else:
        print('Could not find gateway')

    body = {
        "sourceIP" : source_device,                # IP address of the source device.
        "sourcePort" : source_port,
        "sourceGateway" : gateway[0] if type(source_gateway) is dict else {},  
        "destIP" : destination_device,                    # IP address of the destination device.
        "destPort" : destination_port,
        "protocol" : protocol,                # Specify the application protocol, check online help, such as 4 for IPv4.
        "isLive" : is_live                     # False: Current Baseline; True: Live access
    } 
    try:
        response = requests.post(Calculate_Path_url, data = json.dumps(body), headers = headers, verify = False)
        if response.status_code == 200:
            result = response.json()
            return (result)
        else:
            return ("Calculate path failed! - " + str(response.text))

    except Exception as e:
        return (str(e)) 

# Check Path running status.
def get_path_status(taskID, headers, token):
    status_url = nb_url + "/ServicesAPI/API/V1/CMDB/Path/Calculation/" + str(taskID) + "/Status"
    headers["Token"] = token
    try:
        response = requests.get(status_url, headers = headers, verify = False)
        result = response.json()
        return result

    except Exception as e:
        return False
        
# call get path calculation overview API.
def get_path_result(taskID, headers, token):
    Get_Path_Calulation_Result_url = nb_url + "/ServicesAPI/API/V1/CMDB/Path/Calculation/" + str(taskID) + "/OverView"
    headers["Token"] = token
    try:
        running_status = 0
        while running_status < 2:
            print('Path is still running, wait for 5 seconds')
            time.sleep(5)
            status = get_path_status(taskID, headers, token)
            running_status_result = status.get('result')
            if running_status_result is not None:
                running_status = running_status_result.get('resultCode') 

        response = requests.get(Get_Path_Calulation_Result_url, headers = headers, verify = False)
        result = response.json()
        if not result or not result.get('path_overview'):
            print(f'Failed to get path result for task ID:{taskID}')
        else:
            return (result["path_overview"])

    except Exception as e:
        return (str(e)) 
        
        
# call logout API
def logout(nb_url, token, headers):
    Logout_url = nb_url + "/ServicesAPI/API/V1/Session"
    headers["token"] = token
    
    try:
        # Do the HTTP request
        response = requests.delete(Logout_url, headers=headers, verify=False)
        # Check for HTTP codes other than 200
        if response.status_code == 200:
            # Decode the JSON response into a dictionary and use the data
            js = response.json()
            return (js)
        else:
            return ("Session logout failed! - " + str(response.text))

    except Exception as e:
        return (str(e))
```

### Define main function


```python
def main(nb_url, headers, TenantName, DomainName, username, password, source_device, destination_device, source_port, destination_port, protocol, is_live):
    # Calling login API
    print("Calling login API---------------------------------------------------------------------------------------")
    result = login(nb_url, username, password, headers)
    print(result) # print out the authentication token.
    token = result["token"]
    print(token)
    print("")
    
    # Calling get accessible tenant API
    print("Calling get accessible tenant API---------------------------------------------------------------------------------------")
    tenants = get_all_accessible_tenants(nb_url, token, headers)
    tenant =  [x for x in tenants if x["tenantName"] == TenantName] # Name of the tenant which we are going to work inside
    tenantId = tenant[0]["tenantId"]
    print("Tenant ID : " + tenantId) # print out the specified tenant id.
    print("")

    # Calling get accessible domain API
    print("Calling get accessible domain API---------------------------------------------------------------------------------------")
    domains = get_all_accessible_domains(nb_url, tenantId, token, headers)
    domain =  [x for x in domains if x["domainName"] == DomainName]# Name of the domain which we are going to work inside
    domainId = domain[0]["domainId"]
    print("Domain ID : " + domainId) # Print out the specified domain Id.
    print("")

    # Calling specify domain API
    print("Calling specify domain API---------------------------------------------------------------------------------------")
    res =  specify_a_working_domain(tenantId, domainId, nb_url, headers, token)
    print ("Domain ID of Specified Working Domain : " + res)
    print("")
    
    # Calling calculate path API
    print("Calling calculate path API---------------------------------------------------------------------------------------")
    task =  calculate_path(headers, token, source_device, destination_device, source_port=source_port, destination_port=destination_port, protocol=protocol, is_live=is_live)
    print ("Response of the calculate path API : ")
    pprint.pprint(task)
    print("")
    
    # Calling get path calculation overview API
    print("Calling get path calculation overview API---------------------------------------------------------------------------------------")
    print("########################################################################################################")
    taskID = task["taskID"]
    path =  get_path_result(taskID, headers, token)  
    print ("Detail information of path hops: ")
    pprint.pprint(path)
    print("########################################################################################################")
    print("")
    
    # Calling logout API
    print("Calling logout API---------------------------------------------------------------------------------------")
    Logout = logout(nb_url, token, headers)
    print(Logout)

if __name__ == "__main__":
    main(nb_url, headers, TenantName, DomainName, username, password, source_device, destination_device, source_port, destination_port, protocol, is_live)


```

### Sample Output

    Calling login API---------------------------------------------------------------------------------------
    {'token': 'f149791a-567e-4f6a-8b5c-5dcd4d0e8945', 'statusCode': 790200, 'statusDescription': 'Success.'}
    f149791a-567e-4f6a-8b5c-5dcd4d0e8945

    Calling get accessible tenant API---------------------------------------------------------------------------------------
    Tenant ID : b78ac352-2b66-c0bc-ea00-6e6a62dafd5b

    Calling get accessible domain API---------------------------------------------------------------------------------------
    Domain ID : 3e61418c-fee4-43b6-9863-95c383110035

    Calling specify domain API---------------------------------------------------------------------------------------
    Domain ID of Specified Working Domain : 3e61418c-fee4-43b6-9863-95c383110035

    Calling calculate path API---------------------------------------------------------------------------------------
    Detail information of the first gateway in source device: 
    [{'gatewayName': 'CA-TOR-SW1.Vlan302(10.8.30.1)',
    'isCutomized': False,
    'natInfo': [],
    'payload': '{"ip": "10.8.30.1", "endPointInfo": null, "device": '
                '"CA-TOR-SW1", "deviceId": '
                '"4dd0145c-ff8d-4d8f-b33b-a204fb8ca616", "interface": "Vlan302", '
                '"interfaceId": "690489c2-2c26-4380-b48f-00654201abf8", '
                '"prefixLen": 24, "details": [{"device": "CA-TOR-SW1", '
                '"deviceId": "4dd0145c-ff8d-4d8f-b33b-a204fb8ca616", "interface": '
                '"Vlan302", "interfaceId": '
                '"690489c2-2c26-4380-b48f-00654201abf8"}]}',
    'type': 'Device Interface'},
    {'gatewayName': 'CA-TOR-SW1.Vlan302(10.8.30.1)',
    'isCutomized': False,
    'natInfo': [],
    'payload': '{"ip": "10.8.30.1", "endPointInfo": null, "device": '
                '"CA-TOR-SW1", "deviceId": '
                '"4dd0145c-ff8d-4d8f-b33b-a204fb8ca616", "interface": "Vlan302", '
                '"interfaceId": "690489c2-2c26-4380-b48f-00654201abf8", '
                '"prefixLen": 24, "details": [{"device": "CA-TOR-SW1", '
                '"deviceId": "4dd0145c-ff8d-4d8f-b33b-a204fb8ca616", "interface": '
                '"Vlan302", "interfaceId": '
                '"690489c2-2c26-4380-b48f-00654201abf8"}], "Original Type": '
                '"Device Interface"}',
    'type': 'Multicast'}]

    Response of the calculate path API : 
    {'statusCode': 790200,
    'statusDescription': 'Success.',
    'taskID': '4ed3ba9f-1927-4c57-ae95-d2c780f68322'}

    Calling get path calculation overview API---------------------------------------------------------------------------------------
    ########################################################################################################
    Path is still running, wait for 5 seconds
    Detail information of path hops: 
    [{'failure_reasons': [],
    'path_list': [{'branch_list': [{'category': 'Lack of related information',
                                    'error_code': 412,
                                    'failure_reason': 'No matching entries were '
                                                        'found for destination IP '
                                                        '10.8.1.51 in the VRT',
                                    'hop_detail_list': [{'fromDev': {'devId': '00000000-0000-0000-0000-000168304301',
                                                                    'devName': '10.8.30.173',
                                                                    'devType': 1036,
                                                                    'domainId': ''},
                                                        'fromIntf': {'PhysicalInftName': '',
                                                                        'intfDisplaySchemaObj': {'schema': '',
                                                                                                'value': ''},
                                                                        'intfKeyObj': {'schema': '',
                                                                                    'value': ''},
                                                                        'ipLoc': ''},
                                                        'hopId': '836652e5-a1f1-4b77-b564-c20921f13ab1',
                                                        'isComplete': False,
                                                        'isGateway': False,
                                                        'isP2P': False,
                                                        'mediaId': '1f41649c-c2c0-448b-92e0-801fd88a400a',
                                                        'mediaInfo': {'mediaName': '10.78.16.128/29',
                                                                        'mediaType': 'Lan',
                                                                        'neat': True,
                                                                        'topoType': 'L3_Topo_Type'},
                                                        'parentHopId': '',
                                                        'preHopId': '00000000-0000-0000-0000-000000000000',
                                                        'sequnce': 0,
                                                        'techs': [],
                                                        'toDev': {'devId': '225c5da9-96bd-4bde-9409-11d440c7f30d',
                                                                    'devName': 'FW01-VNDR-TTEC-AUS-TX-US/act',
                                                                    'devType': 2009,
                                                                    'domainId': ''},
                                                        'toIntf': {'PhysicalInftName': 'inside',
                                                                    'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
                                                                                            'value': 'inside '
                                                                                                        '10.78.16.129/29'},
                                                                    'intfKeyObj': {'schema': 'ipIntfs._id',
                                                                                    'value': '16556a6b-d687-4a06-8039-9ebb55546937'},
                                                                    'ipLoc': '10.78.16.129/29'},
                                                        'topoType': 'L3_Topo_Type',
                                                        'trafficState': {'acl': '',
                                                                            'alg': -1,
                                                                            'dev_name': '10.8.30.173',
                                                                            'dev_type': 1036,
                                                                            'in_intf': '',
                                                                            'in_intf_schema': '',
                                                                            'in_intf_topo_type': '',
                                                                            'next_dev_in_intf': 'inside '
                                                                                                '10.78.16.129/29',
                                                                            'next_dev_in_intf_schema': 'ipIntfs',
                                                                            'next_dev_in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_name': 'FW01-VNDR-TTEC-AUS-TX-US/act',
                                                                            'next_dev_type': 2009,
                                                                            'next_hop_ip': '10.78.16.129',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': '',
                                                                            'out_intf_schema': '',
                                                                            'out_intf_topo_type': '',
                                                                            'pbr': '',
                                                                            'vrf': ''}},
                                                        {'fromDev': {'devId': '225c5da9-96bd-4bde-9409-11d440c7f30d',
                                                                    'devName': 'FW01-VNDR-TTEC-AUS-TX-US/act',
                                                                    'devType': 2009,
                                                                    'domainId': ''},
                                                        'fromIntf': {'PhysicalInftName': 'inside',
                                                                        'intfDisplaySchemaObj': {'schema': 'intfs.name',
                                                                                                'value': 'inside'},
                                                                        'intfKeyObj': {'schema': 'intfs._id',
                                                                                    'value': '65724b18-2d89-486f-9c42-3e736f5992f6'},
                                                                        'ipLoc': ''},
                                                        'hopId': '21cde94f-8dea-4281-a2cc-f8bf8d6b4ae1',
                                                        'isComplete': False,
                                                        'isGateway': False,
                                                        'isP2P': False,
                                                        'mediaId': '',
                                                        'mediaInfo': {'mediaName': '',
                                                                        'mediaType': '',
                                                                        'neat': False,
                                                                        'topoType': ''},
                                                        'parentHopId': '',
                                                        'preHopId': '836652e5-a1f1-4b77-b564-c20921f13ab1',
                                                        'sequnce': 1,
                                                        'techs': ['In_ACL'],
                                                        'toDev': {'devId': '5447f244-bf92-4d6d-b86f-050488dfe72c',
                                                                    'devName': 'RT01-VNDR-TTEC-AUS-TX-US.citfg.com',
                                                                    'devType': 2,
                                                                    'domainId': ''},
                                                        'toIntf': {'PhysicalInftName': 'TenGigabitEthernet0/1/0.100',
                                                                    'intfDisplaySchemaObj': {'schema': 'intfs.name',
                                                                                            'value': 'TenGigabitEthernet0/1/0.100'},
                                                                    'intfKeyObj': {'schema': 'intfs._id',
                                                                                    'value': 'a8c9ae3e-7e62-496a-8440-5065c4386553'},
                                                                    'ipLoc': ''},
                                                        'topoType': 'L3_Topo_Type',
                                                        'trafficState': {'acl': 'ACL '
                                                                                'outbound '
                                                                                'on '
                                                                                'device '
                                                                                'FW01-VNDR-TTEC-AUS-TX-US/act',
                                                                            'alg': -1,
                                                                            'dev_name': 'FW01-VNDR-TTEC-AUS-TX-US/act',
                                                                            'dev_type': 2009,
                                                                            'in_intf': 'inside '
                                                                                    '10.78.16.129/29',
                                                                            'in_intf_schema': 'ipIntfs',
                                                                            'in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_in_intf': 'TenGigabitEthernet0/1/0.100',
                                                                            'next_dev_in_intf_schema': 'intfs',
                                                                            'next_dev_in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_name': 'RT01-VNDR-TTEC-AUS-TX-US.citfg.com',
                                                                            'next_dev_type': 2,
                                                                            'next_hop_ip': '10.78.16.132',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': 'inside',
                                                                            'out_intf_schema': 'intfs',
                                                                            'out_intf_topo_type': 'L3_Topo_Type',
                                                                            'pbr': '',
                                                                            'vrf': ''}},
                                                        {'fromDev': {'devId': '5447f244-bf92-4d6d-b86f-050488dfe72c',
                                                                    'devName': 'RT01-VNDR-TTEC-AUS-TX-US.citfg.com',
                                                                    'devType': 2,
                                                                    'domainId': ''},
                                                        'fromIntf': {'PhysicalInftName': 'TenGigabitEthernet0/1/1.2',
                                                                        'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
                                                                                                'value': 'TenGigabitEthernet0/1/1.2 '
                                                                                                        '10.78.16.22/30'},
                                                                        'intfKeyObj': {'schema': 'ipIntfs._id',
                                                                                    'value': '0e88a165-c8c5-4704-b78e-3abde617bf03'},
                                                                        'ipLoc': '10.78.16.22/30'},
                                                        'hopId': '36d26a0e-e271-4c05-a236-88975a3408af',
                                                        'isComplete': False,
                                                        'isGateway': False,
                                                        'isP2P': True,
                                                        'mediaId': '',
                                                        'mediaInfo': {'mediaName': '',
                                                                        'mediaType': '',
                                                                        'neat': False,
                                                                        'topoType': ''},
                                                        'parentHopId': '',
                                                        'preHopId': '21cde94f-8dea-4281-a2cc-f8bf8d6b4ae1',
                                                        'sequnce': 2,
                                                        'techs': [],
                                                        'toDev': {'devId': '043acc00-042b-2cf9-6521-ae6048b39a64',
                                                                    'devName': 'MPLS '
                                                                                '- '
                                                                                'AT&T',
                                                                    'devType': 1024,
                                                                    'domainId': ''},
                                                        'toIntf': {'PhysicalInftName': 'TenGigabitEthernet0/1/1.2-10.78.16.21',
                                                                    'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
                                                                                            'value': 'TenGigabitEthernet0/1/1.2-10.78.16.21 '
                                                                                                        '10.78.16.21/30'},
                                                                    'intfKeyObj': {'schema': 'ipIntfs._id',
                                                                                    'value': 'd1e74a9e-c10f-4a9e-a6b7-0c55a2ec1ff8'},
                                                                    'ipLoc': '10.78.16.21/30'},
                                                        'topoType': 'L3_Topo_Type',
                                                        'trafficState': {'acl': '',
                                                                            'alg': -1,
                                                                            'dev_name': 'RT01-VNDR-TTEC-AUS-TX-US.citfg.com',
                                                                            'dev_type': 2,
                                                                            'in_intf': 'TenGigabitEthernet0/1/0.100',
                                                                            'in_intf_schema': 'intfs',
                                                                            'in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_in_intf': 'TenGigabitEthernet0/1/1.2-10.78.16.21 '
                                                                                                '10.78.16.21/30',
                                                                            'next_dev_in_intf_schema': 'ipIntfs',
                                                                            'next_dev_in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_name': 'MPLS '
                                                                                            '- '
                                                                                            'AT&T',
                                                                            'next_dev_type': 1024,
                                                                            'next_hop_ip': '10.78.16.21',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': 'TenGigabitEthernet0/1/1.2 '
                                                                                        '10.78.16.22/30',
                                                                            'out_intf_schema': 'ipIntfs',
                                                                            'out_intf_topo_type': 'L3_Topo_Type',
                                                                            'pbr': '',
                                                                            'vrf': ''}},
                                                        {'fromDev': {'devId': '043acc00-042b-2cf9-6521-ae6048b39a64',
                                                                    'devName': 'MPLS '
                                                                                '- '
                                                                                'AT&T',
                                                                    'devType': 1024,
                                                                    'domainId': ''},
                                                        'fromIntf': {'PhysicalInftName': '',
                                                                        'intfDisplaySchemaObj': {'schema': '',
                                                                                                'value': ''},
                                                                        'intfKeyObj': {'schema': '',
                                                                                    'value': ''},
                                                                        'ipLoc': ''},
                                                        'hopId': '50f97524-3816-4b1f-9dad-6f1e67a6161c',
                                                        'isComplete': False,
                                                        'isGateway': False,
                                                        'isP2P': False,
                                                        'mediaId': '',
                                                        'mediaInfo': {'mediaName': '',
                                                                        'mediaType': '',
                                                                        'neat': False,
                                                                        'topoType': ''},
                                                        'parentHopId': '',
                                                        'preHopId': '36d26a0e-e271-4c05-a236-88975a3408af',
                                                        'sequnce': 3,
                                                        'techs': [],
                                                        'toDev': {'devId': '',
                                                                    'devName': '',
                                                                    'devType': 0,
                                                                    'domainId': ''},
                                                        'toIntf': {'PhysicalInftName': '',
                                                                    'intfDisplaySchemaObj': {'schema': '',
                                                                                            'value': ''},
                                                                    'intfKeyObj': {'schema': '',
                                                                                    'value': ''},
                                                                    'ipLoc': ''},
                                                        'topoType': '',
                                                        'trafficState': {'acl': '',
                                                                            'alg': -1,
                                                                            'dev_name': 'MPLS '
                                                                                        '- '
                                                                                        'AT&T',
                                                                            'dev_type': 1024,
                                                                            'in_intf': 'TenGigabitEthernet0/1/1.2-10.78.16.21 '
                                                                                    '10.78.16.21/30',
                                                                            'in_intf_schema': 'ipIntfs',
                                                                            'in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_in_intf': '',
                                                                            'next_dev_in_intf_schema': '',
                                                                            'next_dev_in_intf_topo_type': '',
                                                                            'next_dev_name': '',
                                                                            'next_dev_type': 0,
                                                                            'next_hop_ip': '',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': '',
                                                                            'out_intf_schema': '',
                                                                            'out_intf_topo_type': '',
                                                                            'pbr': '',
                                                                            'vrf': ''}}],
                                    'priority': 2,
                                    'status': 'Failed'},
                                    {'category': 'Lack of related information',
                                    'error_code': 412,
                                    'failure_reason': 'No matching entries were '
                                                        'found for destination IP '
                                                        '10.8.1.51 in the VRT',
                                    'hop_detail_list': [{'fromDev': {'devId': '00000000-0000-0000-0000-000168304301',
                                                                    'devName': '10.8.30.173',
                                                                    'devType': 1036,
                                                                    'domainId': ''},
                                                        'fromIntf': {'PhysicalInftName': '',
                                                                        'intfDisplaySchemaObj': {'schema': '',
                                                                                                'value': ''},
                                                                        'intfKeyObj': {'schema': '',
                                                                                    'value': ''},
                                                                        'ipLoc': ''},
                                                        'hopId': '836652e5-a1f1-4b77-b564-c20921f13ab1',
                                                        'isComplete': False,
                                                        'isGateway': False,
                                                        'isP2P': False,
                                                        'mediaId': '1f41649c-c2c0-448b-92e0-801fd88a400a',
                                                        'mediaInfo': {'mediaName': '10.78.16.128/29',
                                                                        'mediaType': 'Lan',
                                                                        'neat': True,
                                                                        'topoType': 'L3_Topo_Type'},
                                                        'parentHopId': '',
                                                        'preHopId': '00000000-0000-0000-0000-000000000000',
                                                        'sequnce': 0,
                                                        'techs': [],
                                                        'toDev': {'devId': '225c5da9-96bd-4bde-9409-11d440c7f30d',
                                                                    'devName': 'FW01-VNDR-TTEC-AUS-TX-US/act',
                                                                    'devType': 2009,
                                                                    'domainId': ''},
                                                        'toIntf': {'PhysicalInftName': 'inside',
                                                                    'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
                                                                                            'value': 'inside '
                                                                                                        '10.78.16.129/29'},
                                                                    'intfKeyObj': {'schema': 'ipIntfs._id',
                                                                                    'value': '16556a6b-d687-4a06-8039-9ebb55546937'},
                                                                    'ipLoc': '10.78.16.129/29'},
                                                        'topoType': 'L3_Topo_Type',
                                                        'trafficState': {'acl': '',
                                                                            'alg': -1,
                                                                            'dev_name': '10.8.30.173',
                                                                            'dev_type': 1036,
                                                                            'in_intf': '',
                                                                            'in_intf_schema': '',
                                                                            'in_intf_topo_type': '',
                                                                            'next_dev_in_intf': 'inside '
                                                                                                '10.78.16.129/29',
                                                                            'next_dev_in_intf_schema': 'ipIntfs',
                                                                            'next_dev_in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_name': 'FW01-VNDR-TTEC-AUS-TX-US/act',
                                                                            'next_dev_type': 2009,
                                                                            'next_hop_ip': '10.78.16.129',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': '',
                                                                            'out_intf_schema': '',
                                                                            'out_intf_topo_type': '',
                                                                            'pbr': '',
                                                                            'vrf': ''}},
                                                        {'fromDev': {'devId': '225c5da9-96bd-4bde-9409-11d440c7f30d',
                                                                    'devName': 'FW01-VNDR-TTEC-AUS-TX-US/act',
                                                                    'devType': 2009,
                                                                    'domainId': ''},
                                                        'fromIntf': {'PhysicalInftName': 'inside',
                                                                        'intfDisplaySchemaObj': {'schema': 'intfs.name',
                                                                                                'value': 'inside'},
                                                                        'intfKeyObj': {'schema': 'intfs._id',
                                                                                    'value': '65724b18-2d89-486f-9c42-3e736f5992f6'},
                                                                        'ipLoc': ''},
                                                        'hopId': '8dec2ae9-e314-4543-9776-48c477190d71',
                                                        'isComplete': False,
                                                        'isGateway': False,
                                                        'isP2P': False,
                                                        'mediaId': '',
                                                        'mediaInfo': {'mediaName': '',
                                                                        'mediaType': '',
                                                                        'neat': False,
                                                                        'topoType': ''},
                                                        'parentHopId': '',
                                                        'preHopId': '836652e5-a1f1-4b77-b564-c20921f13ab1',
                                                        'sequnce': 1,
                                                        'techs': ['In_ACL'],
                                                        'toDev': {'devId': '00e59b92-7724-426e-8404-5264f80179ea',
                                                                    'devName': 'RT02-VNDR-TTEC-AUS-TX-US.citfg.com',
                                                                    'devType': 2,
                                                                    'domainId': ''},
                                                        'toIntf': {'PhysicalInftName': 'TenGigabitEthernet0/1/0.100',
                                                                    'intfDisplaySchemaObj': {'schema': 'intfs.name',
                                                                                            'value': 'TenGigabitEthernet0/1/0.100'},
                                                                    'intfKeyObj': {'schema': 'intfs._id',
                                                                                    'value': '556c5960-79c9-4383-a491-00914bea3584'},
                                                                    'ipLoc': ''},
                                                        'topoType': 'L3_Topo_Type',
                                                        'trafficState': {'acl': 'ACL '
                                                                                'outbound '
                                                                                'on '
                                                                                'device '
                                                                                'FW01-VNDR-TTEC-AUS-TX-US/act',
                                                                            'alg': -1,
                                                                            'dev_name': 'FW01-VNDR-TTEC-AUS-TX-US/act',
                                                                            'dev_type': 2009,
                                                                            'in_intf': 'inside '
                                                                                    '10.78.16.129/29',
                                                                            'in_intf_schema': 'ipIntfs',
                                                                            'in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_in_intf': 'TenGigabitEthernet0/1/0.100',
                                                                            'next_dev_in_intf_schema': 'intfs',
                                                                            'next_dev_in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_name': 'RT02-VNDR-TTEC-AUS-TX-US.citfg.com',
                                                                            'next_dev_type': 2,
                                                                            'next_hop_ip': '10.78.16.133',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': 'inside',
                                                                            'out_intf_schema': 'intfs',
                                                                            'out_intf_topo_type': 'L3_Topo_Type',
                                                                            'pbr': '',
                                                                            'vrf': ''}},
                                                        {'fromDev': {'devId': '00e59b92-7724-426e-8404-5264f80179ea',
                                                                    'devName': 'RT02-VNDR-TTEC-AUS-TX-US.citfg.com',
                                                                    'devType': 2,
                                                                    'domainId': ''},
                                                        'fromIntf': {'PhysicalInftName': 'TenGigabitEthernet0/1/1.32',
                                                                        'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
                                                                                                'value': 'TenGigabitEthernet0/1/1.32 '
                                                                                                        '68.139.194.30/30'},
                                                                        'intfKeyObj': {'schema': 'ipIntfs._id',
                                                                                    'value': 'cd1d08d2-ec46-4ed9-850c-ca76241fd258'},
                                                                        'ipLoc': '68.139.194.30/30'},
                                                        'hopId': 'bafe41b6-c07b-4fbc-818a-538debca9794',
                                                        'isComplete': False,
                                                        'isGateway': False,
                                                        'isP2P': True,
                                                        'mediaId': '',
                                                        'mediaInfo': {'mediaName': '',
                                                                        'mediaType': '',
                                                                        'neat': False,
                                                                        'topoType': ''},
                                                        'parentHopId': '',
                                                        'preHopId': '8dec2ae9-e314-4543-9776-48c477190d71',
                                                        'sequnce': 2,
                                                        'techs': [],
                                                        'toDev': {'devId': '56250f01-71ed-58b0-c1d8-7a46616c9f24',
                                                                    'devName': 'MPLS '
                                                                                '- '
                                                                                'Verizon',
                                                                    'devType': 1024,
                                                                    'domainId': ''},
                                                        'toIntf': {'PhysicalInftName': 'TenGigabitEthernet0/1/1.32-68.139.194.29',
                                                                    'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
                                                                                            'value': 'TenGigabitEthernet0/1/1.32-68.139.194.29 '
                                                                                                        '68.139.194.29/30'},
                                                                    'intfKeyObj': {'schema': 'ipIntfs._id',
                                                                                    'value': '42cf2d9b-9866-4c1f-8709-1362e5286385'},
                                                                    'ipLoc': '68.139.194.29/30'},
                                                        'topoType': 'L3_Topo_Type',
                                                        'trafficState': {'acl': '',
                                                                            'alg': -1,
                                                                            'dev_name': 'RT02-VNDR-TTEC-AUS-TX-US.citfg.com',
                                                                            'dev_type': 2,
                                                                            'in_intf': 'TenGigabitEthernet0/1/0.100',
                                                                            'in_intf_schema': 'intfs',
                                                                            'in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_in_intf': 'TenGigabitEthernet0/1/1.32-68.139.194.29 '
                                                                                                '68.139.194.29/30',
                                                                            'next_dev_in_intf_schema': 'ipIntfs',
                                                                            'next_dev_in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_name': 'MPLS '
                                                                                            '- '
                                                                                            'Verizon',
                                                                            'next_dev_type': 1024,
                                                                            'next_hop_ip': '10.78.16.33',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': 'TenGigabitEthernet0/1/1.32 '
                                                                                        '68.139.194.30/30',
                                                                            'out_intf_schema': 'ipIntfs',
                                                                            'out_intf_topo_type': 'L3_Topo_Type',
                                                                            'pbr': '',
                                                                            'vrf': ''}},
                                                        {'fromDev': {'devId': '56250f01-71ed-58b0-c1d8-7a46616c9f24',
                                                                    'devName': 'MPLS '
                                                                                '- '
                                                                                'Verizon',
                                                                    'devType': 1024,
                                                                    'domainId': ''},
                                                        'fromIntf': {'PhysicalInftName': '',
                                                                        'intfDisplaySchemaObj': {'schema': '',
                                                                                                'value': ''},
                                                                        'intfKeyObj': {'schema': '',
                                                                                    'value': ''},
                                                                        'ipLoc': ''},
                                                        'hopId': '59ec2ce6-8e01-492d-a910-5eabc551a9cc',
                                                        'isComplete': False,
                                                        'isGateway': False,
                                                        'isP2P': False,
                                                        'mediaId': '',
                                                        'mediaInfo': {'mediaName': '',
                                                                        'mediaType': '',
                                                                        'neat': False,
                                                                        'topoType': ''},
                                                        'parentHopId': '',
                                                        'preHopId': 'bafe41b6-c07b-4fbc-818a-538debca9794',
                                                        'sequnce': 3,
                                                        'techs': [],
                                                        'toDev': {'devId': '',
                                                                    'devName': '',
                                                                    'devType': 0,
                                                                    'domainId': ''},
                                                        'toIntf': {'PhysicalInftName': '',
                                                                    'intfDisplaySchemaObj': {'schema': '',
                                                                                            'value': ''},
                                                                    'intfKeyObj': {'schema': '',
                                                                                    'value': ''},
                                                                    'ipLoc': ''},
                                                        'topoType': '',
                                                        'trafficState': {'acl': '',
                                                                            'alg': -1,
                                                                            'dev_name': 'MPLS '
                                                                                        '- '
                                                                                        'Verizon',
                                                                            'dev_type': 1024,
                                                                            'in_intf': 'TenGigabitEthernet0/1/1.32-68.139.194.29 '
                                                                                    '68.139.194.29/30',
                                                                            'in_intf_schema': 'ipIntfs',
                                                                            'in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_in_intf': '',
                                                                            'next_dev_in_intf_schema': '',
                                                                            'next_dev_in_intf_topo_type': '',
                                                                            'next_dev_name': '',
                                                                            'next_dev_type': 0,
                                                                            'next_hop_ip': '',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': '',
                                                                            'out_intf_schema': '',
                                                                            'out_intf_topo_type': '',
                                                                            'pbr': '',
                                                                            'vrf': ''}}],
                                    'priority': 2,
                                    'status': 'Failed'}],
                    'description': '10.8.30.173 -> 10.8.1.51',
                    'failure_reasons': [],
                    'path_name': 'L3 Path',
                    'status': 'Failed'},
                    {'branch_list': [{'category': 'Lack of related information',
                                    'error_code': 409,
                                    'failure_reason': 'The L2 connections has '
                                                        'not been discovered by '
                                                        'NetBrain.',
                                    'hop_detail_list': [{'fromDev': {'devId': '225c5da9-96bd-4bde-9409-11d440c7f30d',
                                                                    'devName': 'FW01-VNDR-TTEC-AUS-TX-US/act',
                                                                    'devType': 2009,
                                                                    'domainId': ''},
                                                        'fromIntf': {'PhysicalInftName': '',
                                                                        'intfDisplaySchemaObj': {'schema': '',
                                                                                                'value': ''},
                                                                        'intfKeyObj': {'schema': '',
                                                                                    'value': ''},
                                                                        'ipLoc': ''},
                                                        'hopId': '30c47e86-c3a7-4c55-8042-d0b57207cba3',
                                                        'isComplete': False,
                                                        'isGateway': False,
                                                        'isP2P': False,
                                                        'mediaId': '',
                                                        'mediaInfo': {'mediaName': '',
                                                                        'mediaType': '',
                                                                        'neat': False,
                                                                        'topoType': ''},
                                                        'parentHopId': '21cde94f-8dea-4281-a2cc-f8bf8d6b4ae1',
                                                        'preHopId': '00000000-0000-0000-0000-000000000000',
                                                        'sequnce': 0,
                                                        'techs': [],
                                                        'toDev': {'devId': '',
                                                                    'devName': '',
                                                                    'devType': 0,
                                                                    'domainId': ''},
                                                        'toIntf': {'PhysicalInftName': '',
                                                                    'intfDisplaySchemaObj': {'schema': '',
                                                                                            'value': ''},
                                                                    'intfKeyObj': {'schema': '',
                                                                                    'value': ''},
                                                                    'ipLoc': ''},
                                                        'topoType': '',
                                                        'trafficState': {'acl': '',
                                                                            'alg': -1,
                                                                            'dev_name': 'FW01-VNDR-TTEC-AUS-TX-US/act',
                                                                            'dev_type': 2009,
                                                                            'in_intf': '',
                                                                            'in_intf_schema': '',
                                                                            'in_intf_topo_type': '',
                                                                            'next_dev_in_intf': '',
                                                                            'next_dev_in_intf_schema': '',
                                                                            'next_dev_in_intf_topo_type': '',
                                                                            'next_dev_name': '',
                                                                            'next_dev_type': 0,
                                                                            'next_hop_ip': '',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': '',
                                                                            'out_intf_schema': '',
                                                                            'out_intf_topo_type': '',
                                                                            'pbr': '',
                                                                            'vrf': ''}}],
                                    'priority': 2,
                                    'status': 'Failed'}],
                    'description': '10.78.16.129 -> 10.78.16.132',
                    'failure_reasons': [],
                    'path_name': 'L2 Path',
                    'status': 'Failed'},
                    {'branch_list': [{'category': 'Lack of related information',
                                    'error_code': 409,
                                    'failure_reason': 'The L2 connections has '
                                                        'not been discovered by '
                                                        'NetBrain.',
                                    'hop_detail_list': [{'fromDev': {'devId': '225c5da9-96bd-4bde-9409-11d440c7f30d',
                                                                    'devName': 'FW01-VNDR-TTEC-AUS-TX-US/act',
                                                                    'devType': 2009,
                                                                    'domainId': ''},
                                                        'fromIntf': {'PhysicalInftName': '',
                                                                        'intfDisplaySchemaObj': {'schema': '',
                                                                                                'value': ''},
                                                                        'intfKeyObj': {'schema': '',
                                                                                    'value': ''},
                                                                        'ipLoc': ''},
                                                        'hopId': 'd43e2741-f3be-497e-8085-e1568583eb0c',
                                                        'isComplete': False,
                                                        'isGateway': False,
                                                        'isP2P': False,
                                                        'mediaId': '',
                                                        'mediaInfo': {'mediaName': '',
                                                                        'mediaType': '',
                                                                        'neat': False,
                                                                        'topoType': ''},
                                                        'parentHopId': '8dec2ae9-e314-4543-9776-48c477190d71',
                                                        'preHopId': '00000000-0000-0000-0000-000000000000',
                                                        'sequnce': 0,
                                                        'techs': [],
                                                        'toDev': {'devId': '',
                                                                    'devName': '',
                                                                    'devType': 0,
                                                                    'domainId': ''},
                                                        'toIntf': {'PhysicalInftName': '',
                                                                    'intfDisplaySchemaObj': {'schema': '',
                                                                                            'value': ''},
                                                                    'intfKeyObj': {'schema': '',
                                                                                    'value': ''},
                                                                    'ipLoc': ''},
                                                        'topoType': '',
                                                        'trafficState': {'acl': '',
                                                                            'alg': -1,
                                                                            'dev_name': 'FW01-VNDR-TTEC-AUS-TX-US/act',
                                                                            'dev_type': 2009,
                                                                            'in_intf': '',
                                                                            'in_intf_schema': '',
                                                                            'in_intf_topo_type': '',
                                                                            'next_dev_in_intf': '',
                                                                            'next_dev_in_intf_schema': '',
                                                                            'next_dev_in_intf_topo_type': '',
                                                                            'next_dev_name': '',
                                                                            'next_dev_type': 0,
                                                                            'next_hop_ip': '',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': '',
                                                                            'out_intf_schema': '',
                                                                            'out_intf_topo_type': '',
                                                                            'pbr': '',
                                                                            'vrf': ''}}],
                                    'priority': 2,
                                    'status': 'Failed'}],
                    'description': '10.78.16.129 -> 10.78.16.133',
                    'failure_reasons': [],
                    'path_name': 'L2 Path',
                    'status': 'Failed'}],
    'status': 'Failed'}]
    ########################################################################################################

    Calling logout API---------------------------------------------------------------------------------------
    {'statusCode': 790200, 'statusDescription': 'Success.'}

