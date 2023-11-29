import sys
sys.path.append("C:\\Users\\lauth\\OneDrive\\Desktop\\openai_assistant")
from demos.tools.sql_translator import SQLTranslatorTool, SQLQueryFixer
from demos.tools.sql_result import SQLQueryTool
from demos.config.env_config import OPENAI_API_KEY
from demos.agents.agent import create_agent

from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback

search_tables = [
    "fcs_computadores",
    "fcs_computador_medidor",
    "med_sistema_medicion",
    "var_tipo_variable",
    "var_variable_datos",
]

# Model
llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY, temperature=0, model_name="gpt-3.5-turbo"
)

# Tools
tools = [
    SQLTranslatorTool(search_tables=search_tables),
    SQLQueryTool(),
    SQLQueryFixer(),
]

# Agent
agent = create_agent(llm=llm, verbose=True, tools=tools, max_iterations=7)

# Testing
query = "Average of the 'Pressão Estática (kPa)' values registered in october 17th in 2022 for all measurements systems for the computer with tag FQI-EMED_05-08-10"
# query_str = "Meters of each computer"
# query_str = "how many computers are?"
# query_str_v2 = "quantity of meters that the computer with IP equal to 10.233.117.63 has"
# query_str_v3 = "List the names of the measurement system of the meters that the computer has with tag FQI-3161.01-017?"
# query_str_v4 = "List the names of the measurement system of the meters that the computer has with IP equal to 10.233.81.59?"
# query_str_v5 = "the computers that are in port 4000"
# query_str_v6 = "Values of the static pressure for all measurements systems for the computer with tag FQI-EMED_05-08-10"
# query_str_v7 = "values of the 'average flow' registered in August 2023 of all measurements systems for the computer with tag FQI-EMED_05-08-10"
# query_str_v8 = "average of values of the 'static pressure' of all measurements systems for the computer with tag FQI-EMED_05-08-10"

with get_openai_callback() as cb:
    agent.run(query)
    print(f"Total Tokens: {cb.total_tokens}")
    print(f"Prompt Tokens: {cb.prompt_tokens}")
    print(f"Completion Tokens: {cb.completion_tokens}")
    print(f"Total Cost (USD): ${cb.total_cost}")
