#1. import flask
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


from flask import Flask, jsonify


#Database setup
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

#classes
Base.classes.keys()

#2. Create a local app
app = Flask(__name__)

#3. define what to do when the user hits the index route (home route of the local server)
@app.route("/")
def home():
        
    return(
        f"This is Surfs Up API <br>"
        f"Available routes: <br>"
        f"/api/v1.0/precipitation <br>"
        f"/api/v1.0/stations <br>"
        f"/api/v1.0/tobs <br>"
        )
               
    


#4. define what happens when the user accesses a different route

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > query_date).all()
    
    session.close()

    prcp = list(np.ravel(results))

    return jsonify(prcp)

   

@app.route("/api/v1.0/stations")

def stations():

    session = Session(engine)

    stationsresults = stations = session.query(Measurement.station,func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
    session.close()
    station = list(np.ravel(stationsresults))
    return jsonify(station)
    


@app.route("/api/v1.0/tobs")

def mostactive():

    session = Session(engine)
    Mostactive = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > query_date).filter(Measurement.station=='USC00519281').all()
    session.close()

    mostactive_station = list(np.ravel(Mostactive))
    return jsonify(mostactive_station)
    



# define the main function - defines the behavior for flask
if __name__== "__main__":
    app.run(debug=True)




