from flask import Flask
import KafkaProcessor
from config import config_reader
import InventoryController

config = config_reader.reader()

app = Flask(__name__)

sh = KafkaProcessor.streamhandler

app.register_blueprint(InventoryController.bp)
if __name__ == "__main__":
	sh.consumer.run()
	app.run(debug=True, port=int(config['port']))

