# oci-audit-events-to-adw
Automate loading of OCI Audit event exported logs to ADW 

You can enable Audit event log bulk export in your OCI tenancy by following:https://docs.cloud.oracle.com/iaas/Content/Audit/Concepts/bulkexport.htm

Once the Audit event bulk export is enabled, the logs are exported to OCI Object Storage buckets. There will be buckets created for Audit events exported from each compartment. The bucket names has the prefix format "oci-logs.\_audit", we are using this prefix as a filter parameter in OCI Events to trigger an event whenever an Audit events log file is exported to these Object Storage buckets.

Steps:
=====
1. Create an ADW instance(if doesn't exists one)download the credentials and configure access to it as mentioned in: https://oracle.github.io/learning-library/workshops/journey4-adwc/?page=LabGuide1.md

2. Connect to ADW and create a table as mentioned in: https://docs.oracle.com/database/121/ADXDB/json.htm#ADXDB6371
   
    Ex: CREATE TABLE AUDIT_EVENT_JSON_TAB1 (json_document blob); 

3. Create credentials in ADW to access OCI Object Storage as mentioned in: https://docs.oracle.com/en/cloud/paas/autonomous-data-warehouse-cloud/user/dbms-cloud.html#GUID-742FC365-AA09-48A8-922C-1987795CF36A
   
   Ex: 
   begin
   DBMS_CLOUD.create_credential(
   credential_name => 'OBJ_STOR_CRED1',
   username => 'user1@domain.com',
   password => 'cH-yKq:xxxxxxx'
   );
   end;
  /
  
4. Setup your tenancy for OCI Function development and configure your local PC/Laptop/VM for OCI Function development by following: 
https://docs.cloud.oracle.com/iaas/Content/Functions/Tasks/functionsconfiguringtenancies.htm
https://docs.cloud.oracle.com/iaas/Content/Functions/Tasks/functionsconfiguringclient.htm
  
5. Clone/Download this(https://github.com/sherinchandy/oci-audit-events-to-adw.git)git repo into your local directory. Unzip the ADW credentials downloaded in step 1 into the same directory.

6. Edit the file "func.py" and update it with the OCI region where you are enabling the Audit log bulk export. Also update user name, password, DB service name from your ADW environment.

Ex:
region = "us-phoenix-1"
conn = cx_Oracle.connect("ADMIN","Password123","auditdb_medium")

7. Edit the file "func.yaml" and specify your preferred name for the OCI Function, 
   
   Ex: name: objstor2adw

Make sure the Object Storage buckets has "Emit Object Events" enabled. Reference: https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/managingbuckets.htm#usingconsole

8. Create Event rule in Event service to trigger an OCI Function whenever an Audit events log is exported/uploaded to corresponding. We can use "Object-Create" as event type and bucket name prifix format "oci-logs.\_audit" as event attribute. Reference: https://docs.cloud.oracle.com/iaas/Content/Events/Concepts/eventsgetstarted.htm#Console

