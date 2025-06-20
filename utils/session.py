from snowflake.snowpark.session import Session

def create_session_object():
    connection_parameters = {
        "account": "your_account",
        "user": "your_username",
        "password": "your_password",
        "role": "your_role",  # Optional, specify if needed
        "warehouse": "your_warehouse",  # Optional, specify if needed
        "database": "your_database",  # Optional, specify if needed
        "schema": "your_schema"  # Optional, specify if needed
    }

    session = Session.builder.configs(connection_parameters).create()
    return session