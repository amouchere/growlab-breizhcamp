from influxdb import InfluxDBClient
from datetime import datetime
import json, logging, os, sys, time, requests

class storage: 
    def __init__(self, config):
        self.config = config

    def add_measures(self, key, value, client):
        points = []
        
        point = {
                    "measurement": key,
                    "tags": {
                        "event": "breizhcamp"
                    },
                    "time": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "fields": {
                        "value": value
                    }
                }
        points.append(point)
        client.write_points(points)

    def store(self, readings):   
        logger = logging.getLogger("growlab")

        logger.info("Data to store: {}".format(readings))

        hostname = self.config["hostname"]
        port = self.config["port"]
        db = self.config["database"]
        client = InfluxDBClient(hostname, port)

        connected = False
        while not connected:
            try:
                logging.info("Check if database %s exists?", db)
                if not {'name': db} in client.get_list_database():
                    logging.info("Database %s creation..", db)
                    client.create_database(db)
                    logging.info("Database %s created!", db)
                client.switch_database(db)
                logging.info("Connected to %s", db)
            except requests.exceptions.ConnectionError:
                logging.info('InfluxDB is not reachable. Waiting 5 seconds to retry.')
                time.sleep(5)
            else:
                connected = True

        pairs = readings.items()
        for key, value in pairs:
            self.add_measures(key, value, client)
        logger.info("Storage done")

                
        
    