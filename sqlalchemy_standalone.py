from sqlalchemy import create_engine, text

sql_user = "kbase_dev_admin"
sql_pass = "dev%40123"
conn_url = f"postgresql+psycopg2://{sql_user}:{sql_pass}@localhost:5432/kbase_dev_db"
print("Connecting to ", conn_url)

engine = create_engine(conn_url)

with engine.connect() as conn:
    with conn.begin():
        query = text("""
            INSERT INTO dev_db_log (username, email) 
            VALUES (:val1, :val2);
            """)
        
        conn.execute(query, {"val1": "Basav", "val2": "basav@example.com"})

        print("insert completed successfully")

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM dev_db_log;"))

    for row in result:
        print(f"Row data {row[0]} {row[1]} {row[2]} {row[3]}")

# run command `pip install sqlalchemy psycopg2-binary`
# then run python sqlalchemy_standalone.py
