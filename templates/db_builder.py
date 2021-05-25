import os
import pandas as pd
import psycopg2
#import the relevant sql library
from sqlalchemy import create_engine


# connect and create tables if they don't exist yet
DATABASE_URL = os.environ['DATABASE_URL']

engine = create_engine(DATABASE_URL, echo = False)


df.to_sql('projects', con=engine, if_exists='replace')

