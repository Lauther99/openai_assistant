import sys

sys.path.append("C:\\Users\\lauth\\OneDrive\\Desktop\\openai_assistant")
from demos.config.database_connection import conn
from langchain.tools import BaseTool


def get_sql_query(sql_query: str):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error executing SQL query: {e}")
        return e.args[1]
    finally:
        cursor.close()


class SQLQueryTool(BaseTool):
    name = "sql_db_query"
    description: str = """
    Input to this tool is a detailed and correct SQL query, output is a result from the database.
    If the query is not correct, an error message will be returned.
    If an error is returned, rewrite the query, check the query, and try again.
    """

    def _run(self, sql_query):
        return get_sql_query(sql_query)

    def _arun(self):
        raise NotImplementedError("This tool does not support async")

# query = '''SELECT vvd.Valor
# FROM dbo_v2.var_variable_datos vvd
# JOIN dbo_v2.med_sistema_medicion msm ON vvd.idSistemaMedicion_fk = msm.Id
# JOIN dbo_v2.fcs_computadores fc ON fc.Id = msm.IdComputador_fk
# JOIN dbo_v2.var_tipo_variable vtv ON vtv.Id = vvd.idVariable_fk
# WHERE vtv.Nombre = 'Pressão Estática (kPa)'
# AND vvd.Fecha = '2022-10-17'
# AND fc.Tag = 'FQI-EMED_05-08-10';'''
# print(get_sql_query(query))