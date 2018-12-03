#!/usr/bin/env python
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
import logging


app = Flask(__name__)
app.config.from_pyfile('config.py')
CORS(app)

engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = scoped_session(sessionmaker(bind=engine))
s = Session()
logging.getLogger('flask_cors').level = logging.DEBUG


@cross_origin()
@app.route("/")
def refseqsjson():
      # {"name": "chr1", "start": 0, "end": 12345678},

    result = s.execute('select feature.name, feature.seqlen, organism.common_name from chado.feature, chado.organism where seqlen > 0 and feature.organism_id = organism.organism_id;')
    response = []
    for r in result.fetchall():
        response.append({
            'organism': r[2],
            'name': r[0],
            'start': 0,
            'end': r[1],
        })
    return jsonify(response)


if __name__ == "__main__":
    app.run()
