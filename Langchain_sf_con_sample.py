
from langchain.document_loaders import SnowflakeLoader

QUERY = "select * from analytics.raw.customer limit 10"
snowflake_loader = SnowflakeLoader(
    query=QUERY,
    user="SNOWFLAKETEST014",
    password="Snowfl@ketest011",
    account="qramxco-el59371",
    warehouse="DBT_WH",
    role="ACCOUNTADMIN",
    database="analytics",
    schema="raw",
)
snowflake_documents = snowflake_loader.load()
i=1
for document in snowflake_documents:
    print("row number = {} =======================".format(i))
    print(document.page_content)
    i=i+1
