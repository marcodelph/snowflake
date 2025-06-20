# session.py
import os
from snowflake.snowpark.session import Session
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env que está no MESMO diretório do script
load_dotenv()

def create_session_object():
    connection_parameters = {
        "account": os.getenv("SNOWFLAKE_ACCOUNT"),
        "user": os.getenv("SNOWFLAKE_USER"),
        "password": os.getenv("SNOWFLAKE_PASSWORD"),
        "role": os.getenv("SNOWFLAKE_ROLE"),
        "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
        "database": os.getenv("SNOWFLAKE_DATABASE"),
        "schema": os.getenv("SNOWFLAKE_SCHEMA")
    }

    session = Session.builder.configs(connection_parameters).create()
    return session

# Exemplo de como usar a função:
if __name__ == "__main__":
    try:
        snowpark_session = create_session_object()
        print("Sessão Snowpark criada com sucesso!")
        print(f"Versão Snowflake: {snowpark_session.sql('SELECT current_version()').collect()[0][0]}")
        snowpark_session.close()
        print("Sessão Snowpark fechada.")
    except Exception as e:
        print(f"Erro ao criar ou usar a sessão Snowpark: {e}")