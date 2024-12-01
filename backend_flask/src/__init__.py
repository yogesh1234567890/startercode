from flask import Flask,g, request, jsonify
from .middlewares import setup_middlewares
from .database import connect_to_db
from .routes import api_routes
from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import Redis
from kafka import KafkaProducer

def create_kafka_producer():
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
    )
    return producer

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    databse = connect_to_db(app)
    redis = Redis(host='localhost', port=6379, db=0)
    kafka_producer = create_kafka_producer()
    
    @app.before_request
    def before_request():
        # stroing database connection in global variable
        g.database = databse
        g.redis = redis
        g.kafka_producer = kafka_producer
        # also see if there is any json data in req body and if yes then parse it and store it in g object
        if request.is_json:
            g.request_json_body = request.get_json()
        else:
            g.request_json_body = None
    setup_middlewares(app)
    app.register_blueprint(api_routes, url_prefix="/api")
    return app
