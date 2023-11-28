import sys

sys.path.append("C:\\Users\\lauth\\OneDrive\\Desktop\\openai_assistant")
from demos.config.langchain_config import get_langchain_sql_object
from demos.tools.sql_translator import SQLTranslatorTool
from demos.tools.sql_result import SQLQueryTool
from demos.config.env_config import OPENAI_API_KEY
from demos.agents.agent import create_agent

import environ
from sqlalchemy.engine import URL
import openai

from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.agents import initialize_agent
from langchain.callbacks import get_openai_callback

from langchain.tools.sql_database.tool import (
    InfoSQLDatabaseTool,
    ListSQLDatabaseTool,
    QuerySQLCheckerTool,
    QuerySQLDataBaseTool,
)

search_tables = [
    "fcs_computadores",
    "fcs_computador_medidor",
    "med_sistema_medicion",
    "var_tipo_variable",
    "var_variable_datos",
]

langchain_sql_object = get_langchain_sql_object(search_tables=search_tables)

# Model and memory
llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY, temperature=0, model_name="gpt-3.5-turbo"
)
# conversational_memory = ConversationBufferWindowMemory(
#     memory_key="chat_history", k=5, return_messages=True
# )

# Tools
tools = [
    # InfoSQLDatabaseTool(db=langchain_sql_object),
    # ListSQLDatabaseTool(db=langchain_sql_object),
    # QuerySQLCheckerTool(db=langchain_sql_object, llm=llm),
    SQLTranslatorTool(search_tables=search_tables),
    SQLQueryTool(),
    # QuerySQLDataBaseTool(db=langchain_sql_object),
]

# Agent
agent = create_agent(
    llm=llm,
    verbose=True,
    tools=tools
)

query = "Values of the 'Pressão Estática (kPa)' registered in october 17th in 2022 for all measurements systems for the computer with tag FQI-EMED_05-08-10"

with get_openai_callback() as cb:
    agent.run(query)
    print(f"Total Tokens: {cb.total_tokens}")
    print(f"Prompt Tokens: {cb.prompt_tokens}")
    print(f"Completion Tokens: {cb.completion_tokens}")
    print(f"Total Cost (USD): ${cb.total_cost}")
