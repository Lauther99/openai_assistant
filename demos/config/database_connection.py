import sys
sys.path.append("C:\\Users\\lauth\\OneDrive\\Desktop\\openai_assistant")
from demos.config.env_config import ODBCDRIVER, HOST, DBNAME, USER, PWD
import pyodbc


conn = pyodbc.connect(f"DRIVER={ODBCDRIVER};SERVER={HOST};DATABASE={DBNAME};UID={USER};PWD={PWD}")