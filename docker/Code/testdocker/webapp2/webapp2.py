import pandas as pd
from sqlalchemy import create_engine
from flask import Flask
def createConnection(username,passwd,server,database):
    engine = create_engine('postgresql+psycopg2://'+username+':'+passwd+'@'+server+'/'+database)
    return engine

app = Flask(__name__)

@app.route('/')
def main():
    engine = createConnection('postgres','awayz2020','postgres','postgres')
    x = pd.read_sql('select * from teste',con = engine)
    return x.to_json()

if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = "5123")
