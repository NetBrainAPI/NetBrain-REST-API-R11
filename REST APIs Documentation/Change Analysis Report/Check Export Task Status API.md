
# Change Analysis Report API Design -- check export task status API

## ***GET*** /V1/ChangeAnalysis/Export/Tasks/{taskId}/Status
This API is used to submit a task to check the status of the export task. 

## Detail Information

> **Title** : Get Export Task Status for Change Analysis Report API   <br>

> **Version** : 10/14/2020.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB /ChangeAnalysis/Export/Tasks/{taskId}/Status 

> **Authentication** : 

| Type | In | Name |
|---|---|---|
|Bearer Authentication| Headers | Authentication token | 

## Path Parameters(****required***)

|**Name**|**Type**|**Description**|
|---|---|---|
|taskID* | string  | The unique ID of the export task  |


## Headers

> **Data Format Headers**

|**Name**|**Type**|**Description**|
|---|---|---|
| Content-Type | string  | support "application/json" |
| Accept | string  | support "application/json" |

> **Authorization Headers**

|**Name**|**Type**|**Description**|
|---|---|---|
| token | string  | Authentication token, get from login API. |

## Response

|**Name**|**Type**|**Description**|
|---|---|---|
|fileTotal| Integer | The total amount of files need to processed  |
|fileProcessed| Integer | The amount of files have been processed |
|statusCode| string | Code issued by NetBrain server indicating the execution result.  |
|statusDescription| string | The explanation of the status code.  |

## Status Code

|**Code**|**Message**|**Description**|
|---|---|---|
|790200| OK | Success  |
|793404| No resource | No resource |
|794004| Task Not Exist | Task does not exist  |
|793001| Internal Server Error | System Failure  |






