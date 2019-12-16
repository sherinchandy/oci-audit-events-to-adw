# oci-audit-events-to-adw
Automate loading of OCI Audit event exported logs to ADW 

You can enable Audit event log bulk export in your OCI tenancy by following:https://docs.cloud.oracle.com/iaas/Content/Audit/Concepts/bulkexport.htm

Once the Audit event bulk export is enabled, the logs are exported to OCI Object Storage buckets. There will be buckets created for Audit events exported from each compartment. The bucket names has the prefix format "oci-logs.\_audit", we are using this prefix as a filter parameter in OCI Events to trigger an event whenever an Audit events log file is exported to these Object Storage buckets.

**Audit Event Bulk Export Buckets**
![](images/AuditExportBuckets.png)
**Audit Event Log Files**
![](images/AuditLogFiles.png)


##Steps:##

1. Make sure the Object Storage buckets has "Emit Object Events" enabled. Reference: https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/managingbuckets.htm#usingconsole

 ![](images/AuditBucketEnableEmit.png)

 ![](images/EnableEmit2.png)

2. Create an ADW instance(if doesn't exists one)download the credentials and configure access to it as mentioned in: https://oracle.github.io/learning-library/workshops/journey4-adwc/?page=LabGuide1.md

3. Connect to ADW and create a table as mentioned in: https://docs.oracle.com/database/121/ADXDB/json.htm#ADXDB6371
   
  ![](images/TableCreate.png)

4. Create credentials in ADW to access OCI Object Storage as mentioned in: https://docs.oracle.com/en/cloud/paas/autonomous-data-warehouse-cloud/user/dbms-cloud.html#GUID-742FC365-AA09-48A8-922C-1987795CF36A
   
  ![](images/CredentialCreate.png)
  
5. Create an Application of your desired name(Ex: ObjStor2ADW)from OCI console by following:https://docs.cloud.oracle.com/iaas/Content/Functions/Tasks/functionscreatingapps.htm#console 

  ![](images/FuncAppCreate.png)

6. Setup your tenancy for OCI Function development and configure your local PC/Laptop/VM for OCI Function development by  following:
https://docs.cloud.oracle.com/iaas/Content/Functions/Tasks/functionsconfiguringtenancies.htm
https://docs.cloud.oracle.com/iaas/Content/Functions/Tasks/functionsconfiguringclient.htm
  
7. Clone/Download this(https://github.com/sherinchandy/oci-audit-events-to-adw.git)git repo into your local directory. Unzip the ADW credentials downloaded in step 1 into the same directory.

  ![](images/DownloadGitRepo.png)
  
  ![](images/UnzipWalltet.png)

8. Edit the file "func.py" and update it with the OCI region where you are enabling the Audit log bulk export. Also update DB user name, password and DB service name from your ADW environment.

  ![](images/UpdateFuncPY.png)

9. Edit the file "func.yaml" and specify your preferred name(Ex: name: objstor2adw) for the OCI Function. 

  ![](images/UpdateFuncYAML.png)

10. Deploy the function and configure the environment parameters. This step should push the Function image to OCIR service and attach the function to the OCI Function service Application created in step 5.

11. Make sure you are now able to see the Function created in previous step is appearing in the OCI Function service Application's console. 

12. Create an Event rule in Event service to generate an event when Audit Event log file is bulk exported/uploaded to an Object Storage bucket. We can use "Object-Create" as event type, bucket name prifix "oci-logs.\_audit" as event attribute and the Function created in step 10 as Action item. Reference: https://docs.cloud.oracle.com/iaas/Content/Events/Concepts/eventsgetstarted.htm#Console

13. Test and verify that Audit Events in bulk exported gzip files are loaded in the ADW table.

14. Since the JSON data loaded into the table is of BLOB type, we can create a view on the table and run SQL queries to get insight into the Audit logs.




