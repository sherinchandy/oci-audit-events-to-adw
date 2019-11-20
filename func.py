import io
import json
import cx_Oracle
import os

def handler(ctx, data: io.BytesIO = None):

    region = "us-phoenix-1"     ### Change region here ###
    body = json.loads(data.getvalue())
    jsondata = body.get("data")
    resourceId = jsondata.get("resourceId")
    namespacedata = jsondata.get("additionalDetails")
    namespacedata = jsondata.get("additionalDetails")
    nameSpace = namespacedata.get("namespace")
    bucketName = namespacedata.get("bucketName")
    ObjectName = jsondata.get("resourceName")
    ObjectURL = "https://objectstorage." + region + ".oraclecloud.com" + resourceId
    TNS_ADMIN = os.environ["TNS_ADMIN"]
 
    try:
 
        conn = cx_Oracle.connect("ADMIN","Password123","auditdb_medium")
        cursor = conn.cursor()
        
        SQL = """begin
          DBMS_CLOUD.COPY_DATA(table_name =>'JSON_GZIP_TAB1',
          credential_name =>'OBJ_STOR_CRED',
          file_uri_list =>:ObjStorURL, 
          format => json_object('compression' value 'gzip'), 
          field_list => 'json_document CHAR(50000)'
          ); 
        end;"""
        
        adw_exec = cursor.execute(SQL, ObjStorURL=ObjectURL)

        return 
    
    except Exception as e:
        
        print (e)
