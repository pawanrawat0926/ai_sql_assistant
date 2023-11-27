import streamlit as st

tab_title=[
    "REGION",
    "NATION",
    "CUSTOMER",
    "ORDERS"
]

tbl_tabs = st.tabs(tab_title)
with tbl_tabs[0]:
    st.code('''
REGION (
	R_REGIONKEY NUMBER(38,0),
	R_NAME VARCHAR(25),
	R_COMMENT VARCHAR(152)
)
''',language="python")
with tbl_tabs[1]:
    st.code('''
NATION (
	N_NATIONKEY NUMBER(38,0),
	N_NAME VARCHAR(25),
	N_REGIONKEY NUMBER(38,0),
	N_COMMENT VARCHAR(152)
)
''',language="python")
with tbl_tabs[2]:
    st.code('''
CUSTOMER (
	C_CUSTKEY NUMBER(38,0),
	C_NAME VARCHAR(25),
	C_ADDRESS VARCHAR(40),
	C_NATIONKEY NUMBER(38,0),
	C_PHONE VARCHAR(15),
	C_ACCTBAL NUMBER(12,2),
	C_MKTSEGMENT VARCHAR(10),
	C_COMMENT VARCHAR(117)
)
''',language="python")
with tbl_tabs[3]:
    st.code('''
ORDERS (
	O_ORDERKEY NUMBER(38,0),
	O_CUSTKEY NUMBER(38,0),
	O_ORDERSTATUS VARCHAR(1),
	O_TOTALPRICE NUMBER(12,2),
	O_ORDERDATE DATE,
	O_ORDERPRIORITY VARCHAR(15),
	O_CLERK VARCHAR(15),
	O_SHIPPRIORITY NUMBER(38,0),
	O_COMMENT VARCHAR(79)
)
''',language="python")