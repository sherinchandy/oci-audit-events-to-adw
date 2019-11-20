# oci-audit-events-to-adw
Automate loading of OCI Audit event exported logs to ADW 

Steps:
=====
1. Create a table in ADW. 
    
    Ex: CREATE TABLE AUDIT_EVENT_JSON_TAB1 (json_document blob); 

2. Create credentials in ADW to access OCI Object Storage
   
   Ex: 
   begin
   DBMS_CLOUD.create_credential(
   credential_name => 'OBJ_STOR_CRED',
   username => 'user1@domain.com',
   password => 'cH--dgPoyKq:xxxxxxx'
   );
   end;
  /

3. Create Event rule in Event service to 
