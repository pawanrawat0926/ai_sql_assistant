from app_secrets import OPENAI_API_KEY
import os
import streamlit as st
from sql_execution import execute_sf_query
from langchain import OpenAI
from langchain.prompts import load_prompt
from pathlib import Path
from PIL import Image

def write_to_training_file(file_path,prompt,sql):
     try:
          with (open(file_path,'w')) as file:
               file.write("\n prompt : {}".format(prompt))
               file.write("\n sql : {}".format(sql))
               file.write("\n lable : 1 \n\n")
               file.close()
               return "success"
     except:
          print("problem in opening file")
          return "problem in openeing file"

#setup env variable
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
#project root directory
current_dir = Path(__file__)
root_dir = [p for p in current_dir.parents if p.parts[-1]=='ai_sql_assistant'][0]
#frontend
st.set_page_config(
    page_title="Query Assistant",
    page_icon="🌄"
)
st.sidebar.success("Select a page above")

tab_titles=[
    "Results",
    "Query",
    "ER Diagram"
]

st.title("Your Project Assistant")
prompt = st.text_input("enter your query")
tabs = st.tabs(tab_titles)
with tabs[2]:
        image = Image.open("{}/images/ERD.png".format(root_dir))
        st.image(image,caption="Entity Relationship")

prompt_template = load_prompt(f"{root_dir}/prompts/tpch_prompt.yaml")
final_prompt = prompt_template.format(input=prompt)

llm = OpenAI(temperature=0.9)

if prompt:
    query_text = llm(prompt=final_prompt)
    output = execute_sf_query(query_text)
    with tabs[0]:
        st.write(output)
    with tabs[1]:
        st.write(query_text)
        add_to_training_data = st.button("Add to training data")
        if add_to_training_data:
             file_path="{}/trainings/gpt_trainings.txt".format(root_dir)
             write_to_file_status = write_to_training_file(file_path=file_path,prompt=prompt,sql=query_text)
             if write_to_file_status == "success":
                  st.write("Scenario added to trainings file")
             else:
                  st.write(write_to_file_status)