# Databricks notebook source
Display name: ayushapp
Application (client) ID : 92e55b72-fcd5-4561-82cd-01a4512c2fbf
Object ID : 3684cf1b-a37a-4675-99fb-d094826508fe
Directory (tenant) ID:5cf70121-83f6-4a7c-a5da-30176aa09997
    
value : BPx7Q~Zvy2ll..iQscRwPq9ussEr5b4YPkYQ7
secret ID : 7e020166-b195-4185-a3be-a5d41dea3d82


# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": "92e55b72-fcd5-4561-82cd-01a4512c2fbf",
          "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope="ayushscope1",key="adlsappkey"),
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/5cf70121-83f6-4a7c-a5da-30176aa09997/oauth2/token"}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://sales@ayushaccount.dfs.core.windows.net/",
  mount_point = "/mnt/ayushmountcc",
  extra_configs = configs) 

# COMMAND ----------


