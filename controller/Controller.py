from sqlalchemy import create_engine, text
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from controller.Setup import set_up


class Controller:

    def __init__(self):
        self.config = set_up()

        DBNAME = self.config['POSTGRES_DATABASE']
        USER = self.config['POSTGRES_USER']
        PASSWORD = self.config['POSTGRES_PASSWORD']
        HOST = self.config['POSTGRES_HOST']
        PORT = "5432"

        #self.engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}')
        self.engine = create_engine('sqlite:///C://Users//adria//Desktop//Backend LUMA//DATA.db')
        self.conn = self.engine.connect()



    def get_data(self, year: str, month: str):
        session = self.conn

        try:
            date_param = f"{year}-{month}"
            tables = ['eit171', 'eit195', 'eit284', 'eit304', 'hmiigr', 'hmimag']
            namerow = ['data171', 'data195', 'data284', 'data304', 'datahmiigr', 'datahmimag']
            data = {}

            if month in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                date_param = f"{year}-0{month}"


            for table, name in zip(tables, namerow):
                query = text(f"SELECT * FROM {table} WHERE date LIKE '{date_param}%'")
                result = session.execute(query).fetchall()
                data[name] = {"rows": [dict(row._mapping) for row in result]}


        except SQLAlchemyError as error:
            return JSONResponse(content={"error": str(error)}, status_code=500)
        finally:
            session.close()

        return JSONResponse(content=data)