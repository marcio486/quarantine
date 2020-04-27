from flask import Flask, render_template      
import pandas as pd
from sqlalchemy import create_engine
def createConnection(username,passwd,server,database):
    engine = create_engine('postgresql+psycopg2://'+username+':'+passwd+'@'+server+'/'+database)
    return engine

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("template.html")
    
@app.route('/SomeFunction')
def SomeFunction():
    engine = createConnection('postgres','awayz2020','postgres','postgres')
    x = pd.read_sql('select * from teste',con = engine)
    valor = x.num[0] + 1
    try:
        pd.read_sql('update teste set num = %d'%valor,con = engine)
    except:
        pass
    return "Nothing"

if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = "5124")
