
def get_description(name, tables):
    for table in tables:
        if table["table_name"] == name:
            table_columns = ", ".join([f'"{column}" text' for column in table["columns"]])
            result = f'- Table = "{table["query_name"]}", columns = [{table_columns}], description = "{table["description"]}'
            return result
        