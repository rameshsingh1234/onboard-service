import jsonschema
from flask import Flask, request, jsonify
import logging
from src.unittest.python.utils import read_config_file
from src.main.python.schemaValidator import SchemaValidator
from src.unittest.python.utils import read_file
from src.main.python import CentralRegistry as cr
from src.main.python import json_data_validator as jdv
from src.main.python import Keycloak

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)


@app.route('/v1/FIU/Health', methods=['GET'])
def v1_fiu_health():
    return jsonify({"status": "Active"})


@app.route('/v1/FIU', methods=['POST'])
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

    config = read_config_file.read_config('/home/amith/Desktop/Onboard-Service-Vishwaas/onboard-service-AUG09/onboard'
                                          '-service/src/main/python/resources/application.json')



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
            res = cr.CentralRegistry(config, 'FIU').add_entity(data, access_token)
            # print("Result",res)
            if res.status_code == 200:
                client_response = keycloak_instance.create_client(access_token, data['entityinfo']['id'])
                if not client_response:
                    return jsonify({"responseCode": 409, "responseText": "keycloak client creation error"}), 409

                else:
                    return jsonify({"responseCode": 201, "responseText": client_response}), 201

            else:
                return jsonify({"Meassage":"Error - Central Registry", "responseText": res.json()}), res.status_code,
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



@app.route('/v1/FIU', methods=['PUT'])
def update_fiu():
    # Extract request headers and body
    headers = request.headers
    data = request.get_json()

    # Validate required headers
    required_headers = ['clientId', 'clientSecret', 'userType']
    if not all(header in headers for header in required_headers):
        return jsonify({"responseCode": 401, "responseText": "Unauthorized"}), 401

    # Validate required properties in the request body (SetEntityRequest schema)
    required_properties = ['ver', 'timestamp', 'txnid', 'requester', 'entityinfo']
    if not all(prop in data for prop in required_properties):
        return jsonify({"responseCode": 400, "responseText": "Invalid path specified"}), 400

    # Check if the FIU exists (dummy check without actual data storage)
    # You can add further logic to handle the update operation
    fiu_id = data['entityinfo']['id']
    if fiu_id == "some_existing_fiu_id":
        # You can perform the update operation here
        # Assuming that entityinfo in the request payload contains the updated information
        # Example:
        # updated_entity_info = data['entityinfo']
        # Perform update logic using updated_entity_info and fiu_id

        # Return success response
        return jsonify({"responseCode": 200, "responseText": "FIU updated successfully"}), 200
    else:
        return jsonify({"responseCode": 404, "responseText": "FIU is not found."}), 404


@app.route('/v1/FIU/<string:entityId>', methods=['PATCH'])
def update_fiu_by_id(entityId):
    # Extract request headers and body
    headers = request.headers
    data = request.get_json()

    # Validate required headers
    required_headers = ['clientId', 'clientSecret', 'userType']
    if not all(header in headers for header in required_headers):
        return jsonify({"responseCode": 401, "responseText": "Unauthorized"}), 401

    # Validate required properties in the request body (UpdateEntityRequest schema)
    required_properties = ['ver', 'timestamp', 'txnid', 'requester', 'entityinfo']
    if not all(prop in data for prop in required_properties):
        return jsonify({"responseCode": 400, "responseText": "Invalid path specified"}), 400

    # Check if the FIU exists (dummy check without actual data storage)
    # You can add further logic to handle the update operation
    if entityId != "some_existing_fiu_id":
        return jsonify({"responseCode": 404, "responseText": "FIU is not found."}), 404

    # Return success response
    return jsonify({"responseCode": 200, "responseText": "FIU updated successfully"}), 200


@app.route('/v1/FIU/<string:entityId>', methods=['DELETE'])  # New endpoint for DELETE
def delete_fiu_by_id(entityId):
    # Extract request headers and body
    headers = request.headers

    # Validate required headers
    required_headers = ['clientId', 'clientSecret', 'userType']
    if not all(header in headers for header in required_headers):
        return jsonify({"responseCode": 401, "responseText": "Unauthorized"}), 401

    # Validate entityId (assuming "some_existing_fiu_id" is the FIU to be deleted)
    if entityId != "fiu@finarkein":
        return jsonify({"responseCode": 404, "responseText": "FIU is not found."}), 404

    # Perform the delete operation here
    # Example:
    # delete_fiu(entityId)

    # Return success response
    return jsonify({"responseCode": 200, "responseText": "FIU deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
