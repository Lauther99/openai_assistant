import sys

sys.path.append("C:\\Users\\lauth\\OneDrive\\Desktop\\openai_assistant")

import openai
from demos.prompts.instructions import (
    sql_translator_instruction,
    system_instruction,
    content_error_instruction,
)
from demos.mongo.users_manager import save_to_chat, find_user
from demos.data.data_info import tables
from demos.config.env_config import OPENAI_API_KEY
from demos.utils.getDescription import get_description
from langchain.tools import BaseTool
from langchain.pydantic_v1 import BaseModel, Field


def get_sql_query(search_tables, query_input) -> str:
    openai.api_key = OPENAI_API_KEY

    description = ""
    for name in search_tables:
        description += get_description(name, tables)

    user_prompt = """
    Language Microsoft SQL Server 2014
    You will have information about the database involved in triple single quotes with this format: Table, Columns, Description.
    Read the table descriptions and the columns carefully to understand and then translate.
    '''
    {description}
    '''
    {sql_translator}
    """

    user_prompt = user_prompt.format(
        sql_translator=sql_translator_instruction.format(query=query_input),
        description=description,
    )
    messages = [
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": user_prompt},
    ]

    client = openai.OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=messages
    )

    messages.append(
        {
            "role": "assistant",
            "content": completion.choices[0].message.content.replace('"', "") or "",
        }
    )

    # Agregando a la db
    save_to_chat(messages, "51989915557")
    return completion.choices[0].message.content.replace('"', "") or ""


def sql_error(error_message) -> str:
    openai.api_key = OPENAI_API_KEY

    user = find_user("51989915557")
    messages = user["chats"] or []

    messages.append(
        {
            "role": "user",
            "content": content_error_instruction.format(error_message=error_message),
        }
    )

    client = openai.OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=messages
    )

    messages.append(
        {
            "role": "assistant",
            "content": completion.choices[0].message.content.replace('"', "") or "",
        }
    )

    # Agregando a la db
    save_to_chat(messages, "51989915557")

    return completion.choices[0].message.content.replace('"', "") or ""


class BaseSQLDatabaseTool(BaseModel):
    """Base tool for interacting with a SQL database."""

    search_tables: list[str] = Field(exclude=True)

    class Config(BaseTool.Config):
        pass


class SQLTranslatorTool(BaseSQLDatabaseTool, BaseTool):
    name = "sql_translator"
    description = "this tool allows you to translate a text to SQL code or rewrite the query. Input to this tool is the complete user question not a code, only the output to this tool is a SQL code"

    def _run(self, query_input: str):
        return get_sql_query(self.search_tables, query_input)

    def _arun(self, query_input: str):
        raise NotImplementedError("This tool does not support async")


search_tables = [
    "fcs_computadores",
    "fcs_computador_medidor",
    "med_sistema_medicion",
    "var_tipo_variable",
    "var_variable_datos",
]

query = "Values of the 'Pressão Estática (kPa)' registered in october 17th in 2022 for all measurements systems for the computer with tag FQI-EMED_05-08-10"

get_sql_query(search_tables, query)
# print(
#     sql_error(
#         """Msg 207, Level 16, State 1, Line 4
# Invalid column name 'IdComputador_fk'.
# """
#     )
# )
