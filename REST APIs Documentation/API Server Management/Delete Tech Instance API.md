Tech Instance REST API
======================

DELETE /V1/CMDB/TechInstance/{techType}/{instance}
--------------------------------------------------

Call this API to delete the specified AWS instance(s) data from NetBrain domain.

The required user privileges follow the system requirement.

Detail Information
------------------

\| Title: Discovery Task API

\| Version: 03/10/2021

\| API Server URL: http(s)://IP Address of NetBrain Web API
Server/ServicesAPI/API/V1/CMDB/TechInstance/{techType}/{instance}

\| Authentication:

| **Type**              | **In**  | **Name**             |
|-----------------------|---------|----------------------|
| Bearer Authentication | Headers | Authentication token |

Path Parameters (\*required)
----------------------------

| **Name**   | **Type** | **Description**                                                                                   |
|------------|----------|---------------------------------------------------------------------------------------------------|
| instance\* | String   | AWS: AWS Account ID Azure: Azure Application/Client ID Cisco ACI: APIC IP ESXi: vCenter IP NSX-V: |
| techType\* | String   | AWS/Azure (Xuefei will provide the values)                                                        |

Request body (\*required)
-------------------------

\| No parameters required.

Headers
-------

\| Data Format Headers

| **Name**     | **Type** | **Description**            |
|--------------|----------|----------------------------|
| Content-Type | String   | Support “application/json” |
| Accept       | String   | Support “application/json” |

\| Authorization Headers

| **Name** | **Type** | **Description**                           |
|----------|----------|-------------------------------------------|
| Token    | String   | Authentication token, get from login API. |

Response
--------

| **Name**          | **Type** | **Description**                               |
|-------------------|----------|-----------------------------------------------|
| statusCode        | Integer  | The returned status code of executing the API |
| statusDescription | String   | The explanation of the status code            |

\| *Example*

1.  {  }
