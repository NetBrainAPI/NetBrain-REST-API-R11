# Full Example

```python
import requests
import json
import time
import sys

class Netbrain(object):

    endpoint = ""
    tenantId = ""
    domainId = ""
    username = ""
    token = ""
    headers = {"Content-Type":"application/json","Accept":"application/json"}

    def __init__(self, endpoint, username, password, tenantName, domainName):
        self.endpoint = endpoint
        self.username = username
        self.token = self.getTokens(username,password)
        self.headers["token"] = self.token
        self.tenantId = self.getTenantIdByName(tenantName)
        self.domainId = self.getDomainIdByName(self.tenantId, domainName)


    def getTokens(self, username, password):
        login_api_url = "/ServicesAPI/API/V1/Session"
        login_url = self.endpoint + login_api_url
        body_data = {
            "username": username,
            "password": password
        }
        try:
            token = requests.post(login_url, data=json.dumps(body_data), headers=self.headers, verify=True)
            if token.status_code == 200:
                return token.json()["token"]
            else:
                return token.text
        except Exception as e:
            return str(e)

    def setCurrentDomain(self):
        set_domain_api_url = "/ServicesAPI/API/V1/Session/CurrentDomain"
        set_domain_url = self.endpoint + set_domain_api_url
        body = {
            "tenantId":self.tenantId,
            "domainId":self.domainId
        }
        try:
            response = requests.put(set_domain_url, headers=self.headers, data=json.dumps(body), verify=True)
            if response.status_code == 200:
                # print(response.json())
                print("Session set to Tenant ID: {}/Domain ID: {}".format(body["tenantId"], body["domainId"]))
                return True
            else:
                return response.text
        except Exception as e:
            return str(e)
        
    def publishEvent(self, event_body):
        publish_event_api_url = "/ServicesAPI/API/V1/CMDB/EventDriven/Events"
        publish_event_url = self.endpoint + publish_event_api_url
        body = event_body
        try:
            response = requests.post(publish_event_url, headers=self.headers, data=json.dumps(body), verify=True)
            if response.status_code == 200:
                response_json = response.json()
                return response_json
            else:
                return response.text
        except Exception as e:
            return str(e)
        
    def getEventTriggerStatus(self, eventId):
        get_event_trigger_status_api_url = "/ServicesAPI/API/V1/CMDB/EventDriven/Events/" + eventId
        get_event_trigger_status_url = self.endpoint + get_event_trigger_status_api_url
        try:
            response = requests.get(get_event_trigger_status_url, headers=self.headers, verify=True)
            if response.status_code == 200:
                response_json = response.json()
                return response_json
            else:
                return response.text
        except Exception as e:
            return str(e)

    def getTenantIdByName(self, tenantName):
        get_tenant_api_url = "/ServicesAPI/API/V1/CMDB/Tenants"
        get_tenant_url = self.endpoint + get_tenant_api_url
        try:
            response = requests.get(get_tenant_url, headers=self.headers, verify=True)
            if response.status_code == 200:
                response_json = response.json()
                tenants = response_json['tenants']
                for tenant in tenants:
                    if tenant['tenantName'] == tenantName:
                        tenantId = tenant["tenantId"]
                        return tenantId
            else:
                return response.text
        except Exception as e:
            return str(e)

    def getDomainIdByName(self, tenantId, domainName):
        get_domain_api_url = "/ServicesAPI/API/V1/CMDB/Domains/?" + tenantId
        get_domain_url = self.endpoint + get_domain_api_url
        try:
            response = requests.get(get_domain_url, headers=self.headers, verify=True)
            if response.status_code == 200:
                response_json = response.json()
                domains = response_json['domains']
                for domain in domains:
                    if domain['domainName'] == domainName:
                        domainId = domain["domainId"]
                        return domainId
            else:
                return response.text
        except Exception as e:
            return str(e)

    def logout(self):
        logout_api_url = "/ServicesAPI/API/V1/Session"
        logout_url = self.endpoint + logout_api_url
        try:
            response = requests.delete(logout_url, headers=self.headers, verify=True)
            if response.status_code == 200:
                print("Logout successfully.")
            else:
                return response.text
        except Exception as e:
            return str(e)

if __name__ == "__main__":
    
    endpoint = "https://integrationlab.netbraintech.com"
    tenantName = "Initial Tenant"
    domainName = "Integration"
    username = "haoran.song"
    password = "xxxxxxxxxxx"
    
    # Define the event_body according to the real event data template and the NetBrain Event Template qualification definition.
    event_body = {
        "hostname":"US-BOS-R1",
        "interface_name":"ethernet0/1"
        }
    
    # Initiate NetBrain object
    nb = Netbrain(endpoint, username, password, tenantName, domainName)
    
    # If set working domain successfully, continue...
    if nb.setCurrentDomain():
        print("\r\nPost the event...")
        event = nb.publishEvent(event_body)
        print(event)
        if "nbEventId" in event:
            event_id = event["nbEventId"]
            translationStatus = -1
            task_status = 2
            count = 1
            event_status = {}
            
            # Change sleep_interval and event_status_check_max to extend or shorten the event task status query maximum duration.
            sleep_interval = 3
            event_status_check_max = 5
            
            # Within maximum event task status query duration, if event translation is not completed successfully OR 
            # the task is not finished, keep querying the event_status. 
            while translationStatus != 2 or task_status != 1 :
                print("\r\nTask status check: {}".format(count))
                event_status = nb.getEventTriggerStatus(event_id)
                print(event_status)
                count += 1
                
                # If the task is not completed within the max query duration, end the program execution.
                if count > event_status_check_max:
                    print("\r\nThe task is not completed by the server for {} seconds, stop checking task status. \
                        Please check from NetBrain.".format(sleep_interval*(count-1)))
                    sys.exit(0)
                    
                # Update event task status
                translationStatus = event_status["task"]["translationStatus"]
                if "taskStatus" in event_status["task"]:
                    
                    # Break when the task is finished.
                    if event_status["task"]["taskStatus"] == 1:
                        break
                    else:
                        task_status = event_status["task"]["taskStatus"]
                time.sleep(sleep_interval)
            
            # Task executed successfully. Print the NetBrain map URL.
            print("\r\nEvent triggered successfully!\r\nNetBrain Map URL: {}/{}".format(endpoint,event_status["task"]["mapUrl"]))

```