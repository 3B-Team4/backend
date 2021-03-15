# API urls

from app import app, models, schemas, database
from flask import jsonify, request
from typing import List
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, jwt_refresh_token_required, create_refresh_token
)

import logging
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    """
    Sample route for getting user data
    inputs: json with email and password object
    outputs: json with access token and refresh token.
    """
    userSchema = schemas.UserSchema
    users = models.User.query.with_entities(models.User.id, models.User.name, models.User.email, models.User.userType).all()
    print(users)
    return jsonify([userSchema.from_orm(user).dict() for user in users])


@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(current_user), 200

@app.route('/users', methods=['GET'])
@jwt_required
def getUsers():
    userSchema = schemas.UserSchema
    users = models.User.query.with_entities(models.User.id, models.User.name, models.User.email, models.User.userType).all()
    print(users)
    return jsonify([userSchema.from_orm(user).dict() for user in users])

@app.route('/reportCovidCase', methods=['POST'])
def reportCovidCase():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"msg": "Not a proper JSON"}), 400

        print(request.json)

        first_name = request.json.get('first_name')
        last_name = request.json.get('last_name')
        mobile = request.json.get('mobile')
        lat = request.json.get('lat')
        lng = request.json.get('lng')

        covidCase = models.CovidCases(first_name=first_name, last_name=last_name, mobile=mobile,
                                      lat=lat, lng=lng)
        try:
            database.db_session.add(covidCase)
            database.db_session.commit()  # SA will insert a relationship row
        except:
            return jsonify({"msg": "Cannot Create Covid Case"}), 500
        return jsonify({"msg": "Covid Case Created"}), 200


@app.route('/getReportedCases', methods=['GET'])
def getReportedCases():
   cases = models.CovidCases.query.all()
   caseList = []
   for case in cases:
        caseList.append({
        'lat': case.lat,
        'lng': case.lng,
        })
   return jsonify(caseList), 200