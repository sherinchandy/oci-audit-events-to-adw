# oci-audit-events-to-adw
Automate loading of OCI Audit event exported logs to ADW 

https://docs.cloud.oracle.com/iaas/Content/Audit/Concepts/bulkexport.htm

Steps:
=====
1. Create an ADW instance(if doesn't exists one)and configure access to it as mentioned in: https://oracle.github.io/learning-library/workshops/journey4-adwc/?page=LabGuide1.md

2. Connect to ADW and create a table. Ex: CREATE TABLE AUDIT_EVENT_JSON_TAB1 (json_document blob); 

2. Create credentials in ADW to access OCI Object Storage as mentioned in: https://docs.oracle.com/en/cloud/paas/autonomous-data-warehouse-cloud/user/dbms-cloud.html#GUID-742FC365-AA09-48A8-922C-1987795CF36A
   
   Ex: 
   begin
   DBMS_CLOUD.create_credential(
   credential_name => 'OBJ_STOR_CRED',
   username => 'user1@domain.com',
   password => 'cH-yKq:xxxxxxx'
   );
   end;
  /

3. Create Event rule in Event service to 
