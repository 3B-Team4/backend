from app import app
from flask import jsonify, request
import lightgbm as lgb

import logging
logger = logging.getLogger(__name__)


@app.route('/')
def index():
    """
    Hi
    """
    return 'Hello, World!'


# @app.route('/prediction',  methods=['POST'])
@app.route('/prediction', method=['POST'])
def predict():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"msg": "Not a proper JSON"}), 400
        sex = request.json.get('sex')
        age = request.json.get('age')
        headaches = request.json.get('headaches')
        fever = request.json.get('fever')
        covidContact = request.json.get('covidContact')
        soreThroat = request.json.get('soreThroat')
        shortnessOfBreath = request.json.get('shortnessOfBreath')
        cough = request.json.get('cough')

        dataset = [age, sex, cough, shortnessOfBreath,
                   fever, soreThroat, headaches, covidContact]

        model = lgb.Booster(
            model_file="./app/model/lgbm_model_all_features.txt")
        prediction = model.predict([dataset])
        print(prediction)
        return jsonify({"prediction": prediction[0]}), 200
    return jsonify({"msg": "Not a proper JSON"}), 500


@app.route('/test')
def test():
    model = lgb.Booster(model_file="./app/model/lgbm_model_all_features.txt")
    prediction = model.predict([[1, 0, 0, 1, 0, 0, 0, 1]])
    print(prediction)
    return jsonify({"prediction": prediction[0]}), 200
