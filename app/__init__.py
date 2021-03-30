from flask import Flask
from flask_cors import CORS
import os
import pathlib

logPath = str(pathlib.Path(__file__).resolve().parent) + '/config/logger.ini'
print(logPath)
from pathlib import Path
Path("./logs/").mkdir(parents=True, exist_ok=True)

import logging.config
logging.config.fileConfig(
    logPath, disable_existing_loggers=False
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'swag!'

CORS(app)

from app import views