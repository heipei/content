F5 Silverline Threat Intelligence is a cloud-based service incorporating external IP reputation and reducing threat-based communications. By identifying IP addresses and security categories associated with malicious activity, this managed service integrates dynamic lists of threatening IP addresses with the Silverline cloud-based platform, adding context-based security to policy decisions.
## Configure F5 Silverline on Cortex XSOAR

1. Navigate to **Settings** > **Integrations** > **Servers & Services**.
2. Search for F5 Silverline.
3. Click **Add instance** to create and configure a new integration instance.

    | **Parameter** | **Description** | **Required** |
    | --- | --- | --- |
    | Your F5 Silverline server URL |  | True |
    | API Key | The API Key to use for connection | True |
    | Trust any certificate (not secure) |  | False |
    | Use system proxy settings |  | False |

4. Click **Test** to validate the URLs, token, and connection.
## Commands
You can execute these commands from the Cortex XSOAR CLI, as part of an automation, or in a playbook.
After you successfully execute a command, a DBot message appears in the War Room with the command details.
### f5-silverline-ip-objects-list
***
Get a dynamic list of threatening IP addresses by the given list type. The list type can be one of allowlist or denylist.


#### Base Command

`f5-silverline-ip-objects-list`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| list_type | The dynamic lists type of threatening IP addresses. The type can be one of allowlist or denylist. Possible values are: allowlist, denylist. Note- Allowlists named DDOS IP Allowlists in F5 Silveline portal. | Required | 
| object_id | A comma separated list of IP object IDs. If this argument is given, only those IP objects will be displayed. Otherwise, all IP objects that match the given list_type will be displayed. Note - In case you don't know what is the object ID, you should run this command without object_id arguemnt to get all the IDs. | Optional | 
| page_number | Page number to return. The first page number is 1. | Optional | 
| page_size | Number of results in a page. | Optional | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| F5Silverline.IPObjectList.id | String | The ID of a particular threatening IP address object. | 
| F5Silverline.IPObjectList.type | String | The type of a particular threatening IP address object. | 
| F5Silverline.IPObjectList.attributes.ip | String | The IP address of a particular threatening IP address object. | 
| F5Silverline.IPObjectList.attributes.mask | String | The mask of a particular threatening IP address object. | 
| F5Silverline.IPObjectList.attributes.duration | String | The duration \(in seconds\) of a particular threatening IP address object where list type is 'denylist'. | 
| F5Silverline.IPObjectList.attributes.expires_at | String | The expiration date \(timestamp\) of a particular threatening IP address object. | 
| F5Silverline.IPObjectList.attributes.list_target | String | The list target of a particular threatening IP address object. | 
| F5Silverline.IPObjectList.links.self | String | The F5 Silverline url link of a particular threatening IP address object. | 
| F5Silverline.IPObjectList.meta.note | String | The note of a particular threatening IP address object. | 
| F5Silverline.IPObjectList.meta.tags | Unknown | The tags of a particular threatening IP address object. | 
| F5Silverline.IPObjectList.meta.created_at | String | The creation date \(timestamp\) of a particular threatening IP address object. | 
| F5Silverline.IPObjectList.meta.updated_at | String | The last update date \(timestamp\) of a particular threatening IP address object. | 


#### Command Example
```!f5-silverline-ip-objects-list list_type=denylist```

#### Context Example
```json
{
    "F5Silverline": {
        "IPObjectList": [
            {
                "attributes": {
                    "duration": 0,
                    "expires_at": null,
                    "ip": "1.2.3.4",
                    "list_target": "proxy",
                    "mask": "32"
                },
                "id": "d3a8179e-043d-43cb-acff-745b6765d18a",
                "links": {
                    "self": "https://portal.f5silverline.com/api/v1/ip_lists/denylist/ip_objects/d3a8179e-043d-43cb-acff-745b6765d18a?list_target=proxy"
                },
                "meta": {
                    "created_at": "2021-04-22T13:00:43.175Z",
                    "note": "",
                    "tags": [],
                    "updated_at": "2021-04-22T13:00:43.175Z"
                },
                "type": "ip_objects"
            },
            {
                "attributes": {
                    "duration": 0,
                    "expires_at": null,
                    "ip": "1.2.3.4",
                    "list_target": "proxy",
                    "mask": "32"
                },
                "id": "a7c55ea4-1244-4745-a7ad-b4396f2725b3",
                "links": {
                    "self": "https://portal.f5silverline.com/api/v1/ip_lists/denylist/ip_objects/a7c55ea4-1244-4745-a7ad-b4396f2725b3?list_target=proxy"
                },
                "meta": {
                    "created_at": "2021-04-22T12:54:02.283Z",
                    "note": "",
                    "tags": [],
                    "updated_at": "2021-04-22T12:54:02.283Z"
                },
                "type": "ip_objects"
            },
            {
                "attributes": {
                    "duration": 0,
                    "expires_at": null,
                    "ip": "2.2.3.4",
                    "list_target": "proxy",
                    "mask": "32"
                },
                "id": "6d8eafb9-4c3e-4225-a05e-08995a2b5c34",
                "links": {
                    "self": "https://portal.f5silverline.com/api/v1/ip_lists/denylist/ip_objects/6d8eafb9-4c3e-4225-a05e-08995a2b5c34?list_target=proxy"
                },
                "meta": {
                    "created_at": "2021-04-22T13:01:03.074Z",
                    "note": "",
                    "tags": [],
                    "updated_at": "2021-04-22T13:01:03.074Z"
                },
                "type": "ip_objects"
            }
        ]
    }
}
```

#### Human Readable Output

>### F5 Silverline IP Objects
>|ID|IP|List Target|Created At|Updated At|
>|---|---|---|---|---|
>| d3a8179e-043d-43cb-acff-745b6765d18a | 1.2.3.4 | proxy | 2021-04-22T13:00:43.175Z | 2021-04-22T13:00:43.175Z |
>| a7c55ea4-1244-4745-a7ad-b4396f2725b3 | 1.2.3.4 | proxy | 2021-04-22T12:54:02.283Z | 2021-04-22T12:54:02.283Z |
>| 6d8eafb9-4c3e-4225-a05e-08995a2b5c34 | 2.2.3.4 | proxy | 2021-04-22T13:01:03.074Z | 2021-04-22T13:01:03.074Z |


### f5-silverline-ip-object-add
***
Add a new particular threatening IP address object by its IP address.


#### Base Command

`f5-silverline-ip-object-add`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| list_type | The dynamic lists type of threatening IP addresses. The type can be one of allowlist or denylist. Possible values are: allowlist, denylist. Note- Allowlists named DDOS IP Allowlists in F5 Silveline portal. | Required | 
| list_target | This argument can be supplied to target either the proxy or routed denylist. If list_target is not specified it will assume both proxy and routed are requested (i.e proxy-routed). The allowed values for list_target are proxy or routed or proxy-routed. This argument limits the denylist type but is ignored for the other list types. Possible values are: proxy, routed, proxy-routed. | Optional | 
| IP | The IP address of a new particular threatening IP address object. | Required | 
| mask | The mask address of a new particular threatening IP address object. Default is 32. | Optional | 
| duration | The duration (in seconds) of a new particular threatening IP address object where the list type is 'denylist'. Setting the duration to 0 (default) means the new IP address object will never expire. This feature has been removed for allowlist. | Optional | 
| note | The note of a new particular threatening IP address object. Defaut is empty. | Optional | 
| tags | A Comma separated list of tags of a new particular threatening IP address object. Defaut is empty. | Optional | 


#### Context Output

There is no context output for this command.

#### Command Example
```!f5-silverline-ip-object-add IP=2.2.3.4 list_type=denylist```

#### Human Readable Output

>IP object with IP address: 2.2.3.4 created successfully to the denylist list.

### f5-silverline-ip-object-delete
***
Delete an exising particular threatening IP address object by its object ID.


#### Base Command

`f5-silverline-ip-object-delete`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| list_type | The dynamic lists type of threatening IP addresses. The type can be one of allowlist or denylist. Possible values are: allowlist, denylist. Note- Allowlists named DDOS IP Allowlists in F5 Silveline portal. | Required | 
| object_id | The ojbect ID of a particular threatening IP address object that should be deleted. | Required | 


#### Context Output

There is no context output for this command.

#### Command Example
```!f5-silverline-ip-object-delete list_type=denylist object_id=d3a8179e-043d-43cb-acff-745b6765d18a```

#### Human Readable Output

>IP object with ID: d3a8179e-043d-43cb-acff-745b6765d18a deleted successfully from the denylist list.


## Fetch F5 Silverline alerts

| **F5 Silverline supported alert type** | **Incident Type** | 
| --- | --- |
| WAF logs | F5 Silverline WAF Events |
| L7 DDoS logs | F5 Silverline L7 DDoS Events |  
| Threat Intelligence logs | F5 Silverline Threat Intelligence Events |  
| iRule logs | F5 Silverline iRule Events |  


As F5 Silverline API does not support fetch incidents for now, we retrieve alerts via log collector.   
In order to fetch alerts you should follow the instructions below:
1. In your Cortex XSOAR install F5 Silverline integration.
2. In F5 Silverline portal, go to **Config** > **Log Export** .
3. F5 Silverline "Log Export" should be configured with a "Host" destination that supports TLS+TCP communication.
4. Follow the instructions here: https://support.f5silverline.com/hc/en-us/articles/214152048
5. In your Cortex XSOAR go to Syslog integration (installed by  default).
6. Configure the Syslog instance with your log receiver details:
   * Click on "Fetches incidents".
   * Set the Classifier to "F5 Silverline Classifier". 
   * Set the Mapper to "F5 Silverline Mapper".
   * IP address - specify the IP of your log receiver host.
   * Port - specify the port of your log receiver host.
   * Protocol - choose TCP or UDP.
   * Format - specify to 'Auto'.
7. Once the log receiver is configured it should forward the logs in TCP or UDP toward Cortex XSOAR - Syslog integration.
If everything goes as expected you should be able to ses that incidents were successfully pulled. 

* After incidents are being created you can go to incidents page and sort them by their type.
* You can go to an incident info tab (by clicking on an incident) and see all of the incident fields (under the Case Details header). 