import os
import jsonschema
from flask import request, jsonify
import logging
from src.main.python.api.app import app
from src.main.python.schemaValidator import SchemaValidator
from src.unittest.python.utils import read_file, read_config_file
from src.main.python import CentralRegistry as cr
from src.main.python import json_data_validator as jdv
from src.main.python import Keycloak
from flask import Blueprint
from src.main.python.models.database import insert_data

fiu_blueprint = Blueprint('/v1/FIU', __name__)

logging.basicConfig(level=logging.DEBUG)


@fiu_blueprint.route('/Health', methods=['GET'])
def v1_fiu_health():
    return jsonify({"status": "Active"})


@fiu_blueprint.route('/', methods=['POST'])
def create_fiu():
    # Extract request headers and body
    headers = request.headers
    data = request.get_json()

    # Validate required headers
    required_headers = ['clientId', 'clientSecret', 'userType']
    if not all(header in headers for header in required_headers):
        return jsonify({"responseCode": 400,
                        "responseText": f"Required headers are missing, Required headers: {required_headers}"}), 400

    # Validate required properties in the request body
    required_properties = ['ver', 'timestamp', 'txnid', 'requester', 'entityinfo']
    if not all(prop in data for prop in required_properties):
        return jsonify({"responseCode": 400,
                        "responseText": f"Required properties are missing, Required properties: {required_properties}"}), 400

    config = read_config_file.read_config(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "application.json"))

    try:
        # Validate schema in the request body
        validator = SchemaValidator(schema=read_file.read_schemas())
        validator.validate_or_raise(data)
        app.logger.info("JSON is valid according to the schema.")

    except jsonschema.exceptions.ValidationError as e:
        app.logger.error("JSON is not valid according to the schema.")
        app.logger.error(e)
        return jsonify({"responseCode": 422, "responseText": "JSON is not valid according to the schema."}), 422

    # validate the requester.id & name with entityinfo.id&name if self onboarding
    if headers['userType'] != 'TSP':

        validation_res = jdv.JsonDataValidator.relational_validator(data)
        if validation_res:

            # create access token from token service
            keycloak_instance = Keycloak.Keycloak(config)
            access_token = keycloak_instance.get_token(headers['clientId'], headers['clientSecret'])

            # Add the fiu in CR
            entity_type = 'FIU'
            res = cr.CentralRegistry(config, entity_type).add_entity(data, access_token)
            if res.status_code == 200:
                client_response = keycloak_instance.create_client(access_token, data['entityinfo']['id'],
                                                                  data['entityinfo']['baseurl'])
                if not client_response:
                    return jsonify({"responseCode": 409, "responseText": "keycloak client creation error"}), 409
                else:
                    if insert_data(data['entityinfo']['id'], headers['clientId'], headers['userType']):
                        return jsonify({"responseCode": 201, "responseText": client_response}), 201
                    else:
                        return jsonify({"responseCode": 500, "responseText": "Failed to create user"}), 500

            else:
                return jsonify({"Meassage": "Error - Central Registry", "responseText": res.json()}), res.status_code,
        else:
            return jsonify({"responseCode": 400, "responseText": "JSON data is not valid."}), 400
    #
    else:
        # create access token from token service
        keycloak_instance = Keycloak.Keycloak(config)
        access_token = keycloak_instance.get_token(headers['clientId'], headers['clientSecret'])

        # Add the fiu in CR
        res = cr.CentralRegistry(config, 'FIU').add_entity(data, access_token)
        if res.status_code == 200:
            return jsonify({"responseText": res.json()}), 201
        else:
            return jsonify({"responseText": res.json()}), res.status_code
