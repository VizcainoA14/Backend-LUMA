import psycopg2
from psycopg2 import sql
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv




load_dotenv(dotenv_path='.env')

def set_up():
    load_dotenv()

    config = {
        "host": "postgresqlfs-akita-server.postgres.database.azure.com",
        "database": "postgresqlfs-akita-db",
        "user": "adminTerraform",
        "password": "Z@QttY5oy8!AN$bg###w",
        "port": "5432",
    }
    return config



class Controller:

    def __init__(self):
        
        self.config = set_up()
        try:
            self.pg = psycopg2.connect(
                user=self.config['user'],
                password=self.config['password'],
                host=self.config['host'],
                port=self.config['port'],
                database=self.config['database'],
                sslmode='require'
            )
            
            
        except Exception as e:
            print(f"Error al conectar a PostgreSQL: {e}")

    def get_data(self, year: str, month: str):
        conn = self.pg
        cursor = conn.cursor()

        try:
            date_param = f"{year}-{month}"
            tables = ['eit171', 'eit195', 'eit284', 'eit304', 'hmiigr', 'hmimag']
            namerow = ['data171', 'data195', 'data284', 'data304', 'datahmiigr', 'datahmimag']
            data = {}

            if month in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                date_param = f"{year}-0{month}"

            for table, name in zip(tables, namerow):
                query = sql.SQL("SELECT * FROM {} WHERE date LIKE %s").format(sql.Identifier(table))
                cursor.execute(query, (f"{date_param}%",))
                result = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                data[name] = {"rows": [dict(zip(columns, row)) for row in result]}

        except Exception as error:
            return JSONResponse(content={"error": str(error)}, status_code=500)
        finally:
            cursor.close()
            conn.close()

        return JSONResponse(content=data)

    def get_range(self, startdate: str, enddate: str):
        conn = self.pg
        cursor = conn.cursor()

        try:
            tables = ['eit171', 'eit195', 'eit284', 'eit304', 'hmiigr', 'hmimag']
            namerow = ['data171', 'data195', 'data284', 'data304', 'datahmiigr', 'datahmimag']
            data = {}

            for table, name in zip(tables, namerow):
                query = sql.SQL("SELECT * FROM {} WHERE date BETWEEN %s AND %s").format(sql.Identifier(table))
                cursor.execute(query, (startdate, enddate))
                result = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                data[name] = {"rows": [dict(zip(columns, row)) for row in result]}

        except Exception as error:
            return JSONResponse(content={"error": str(error)}, status_code=500)
        finally:
            cursor.close()
            conn.close()

        return JSONResponse(content=data)