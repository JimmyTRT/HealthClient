from fastapi import FastAPI
from logger import setup_logger
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session
import logging
logger = logging.getLogger(__name__)

#logger = setup_logger()
api = FastAPI()


@api.post('/write')
def write_data():
    # ontvang data van de server
    data = {'key': 'value'}
    logger.info(f'api write:' + data)
    # schrijf data weg naar de database
    #   conn = sqlite3.connect('database.db')
    #   cursor = conn.cursor()
    #   cursor.execute('INSERT INTO my_table (key, value) VALUES (?, ?)', (data['key'], data['value']))
    #   conn.commit()
    #   conn.close()
    return {'message': 'Data is weggeschreven naar de database.'}


# Model voor de JSON-payload
class EventCreate(BaseModel):
    controllernaam: str
    timestamp: str
    event: str
    value: float



