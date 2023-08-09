import jsonschema
from flask import Flask, request, jsonify
import logging
from src.unittest.python.utils import read_config_file
from src.main.python.schemaValidator import SchemaValidator
from src.unittest.python.utils import read_file
from src.main.python import CentralRegistry as cr
from src.main.python import json_data_validator as jdv
from src.main.python import Keycloak

logging.basicConfig(level=logging.DEBUG)  # filename='fiu-app.log', filemode='w',
app = Flask(__name__)


@app.route('/v2/FIU', methods=['POST'])
def v2_fiu():
    return jsonify({"api-version": "v2"})


@app.route('/v1/FIU', methods=['POST'])
def create_fiu():
    # Extract request headers and body
    headers = request.headers
    data = request.get_json()

    # Validate required headers
    required_headers = ['clientId', 'clientSecret', 'userType']
    if not all(header in headers for header in required_headers):
        return jsonify({"responseCode": 400,
                        "responseText": f"Required headers are missing, Required headers: {required_headers}"}), 401

    # """ Read configuration"""
    config = read_config_file.read_config('/home/krishna/Tibil/sahamati/onboard-service/src/main/python/resources'
                                          '/application.json')

    # keycloak_base_url = config.get('keycloak_base_url')
    #
    #
    #
    # client_id = headers['clientId']  # Replace with your client ID
    # client_secret = headers['clientSecret']  # Replace with your client secret
    #
    # access_token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ3N2RmZkhZS0JvUzJJUTFhU0t1YjZTcUtRUUI4d2NTWkFzTEpfN19IWXg0In0.eyJleHAiOjE2OTE0NDMxMDgsImlhdCI6MTY5MTQwNzEwOCwianRpIjoiNjNkOTIyZDQtYzVjYi00NTM2LWJjYzItN2E2MGE5NzBhMTJlIiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9zYWhhbWF0aSIsImF1ZCI6WyJyZWFsbS1tYW5hZ2VtZW50IiwiYWNjb3VudCJdLCJzdWIiOiIxYjk1ODdjOC1kY2ZhLTQxZjAtYmZlYy1mMDUxNDcwMTRjMDkiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJzYWhhbWF0aS1hZG1pbiIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiLyoiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtc2FoYW1hdGkiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsic2FoYW1hdGktYWRtaW4iOnsicm9sZXMiOlsidW1hX3Byb3RlY3Rpb24iXX0sInJlYWxtLW1hbmFnZW1lbnQiOnsicm9sZXMiOlsibWFuYWdlLXVzZXJzIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImNsaWVudEhvc3QiOiIxNzIuMTcuMC4xIiwicHJlZmVycmVkX3VzZXJuYW1lIjoic2VydmljZS1hY2NvdW50LXNhaGFtYXRpLWFkbWluIiwiY2xpZW50QWRkcmVzcyI6IjE3Mi4xNy4wLjEiLCJjbGllbnRfaWQiOiJzYWhhbWF0aS1hZG1pbiJ9.Nbz4L8BxhYE279I3lMS9EdsBZaNFTaMTc7tt2sBQWEFq1QUU2gq2biRJMQC3vrAP3cudpbGEUn2-uH07a4wiAuoOi_UJI6YiXkJ_QO5Qb5eAe6o4MCH0NQZJjJL_uYr5woByb1Ry52BVwPFXYAUPVRm27xPs0B79uRXMuBZiQ6XGwQYRQNvjXgz3YKLPp96mopzit35nWDT-3oIo8nGZuE4gCtKVesLAI5bHK0j4FI68KMol7RD4sf8kPAQl4g8H0go9RrDoghmBte7sNMKU8NXvgDx8mk53zW5sFt8iGunViP2OZ0szapviXmh1V5mcsGUTmaz-ej12VTmfmZ4M8g"'
    # ''
    #
    #
    # keycloak_instance = Keycloak(config)
    #
    # introspection_result = keycloak_instance.validate_token(client_id, access_token)
    #
    # if introspection_result.get('active'):
    #     app.logger.info("Token is valid.")
    #     app.logger.info("Token claims:", introspection_result)
    # else:
    #     app.logger.warning("Token is not valid.")

    required_properties = ['ver', 'timestamp', 'txnid', 'requester', 'entityinfo']
    if not all(prop in data for prop in required_properties):
        return jsonify({"responseCode": 400,
                        "responseText": f"required property is missing, required properties {required_properties}"}), 400

    try:
        # Validate schema in the request body
        print("inside json schema validation")
        validator = SchemaValidator(schema=read_file.read_schemas())
        validator.validate_or_raise(data)
        app.logger.info("JSON is valid according to the schema.")

    except jsonschema.exceptions.ValidationError as e:
        app.logger.error("JSON is not valid according to the schema.")
        app.logger.error(e)
        return jsonify({"responseCode": 400, "responseText": "JSON is not valid according to the schema."}), 400

    # validate the requester.id & name with entityinfo.id&name if self onboarding
    if headers['userType'] != 'TSP':

        validation_res = jdv.JsonDataValidator.relational_validator(data)
        if validation_res:

            # create access token from token service
            keycloak_instance = Keycloak.Keycloak(config)
            access_token = keycloak_instance.get_token(headers['clientId'], headers['clientSecret'])

            # Add the fiu in CR
            res = cr.CentralRegistry(config, 'FIU').add_entity(data, access_token)
            if res.status_code == 200:
                client_response = keycloak_instance.create_client(config, access_token, data['entityinfo']['id'])
                if not client_response:
                    return jsonify({"responseText": client_response}), 201
            else:
                return jsonify({"responseText": res.json()}), res.status_code
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

    # Return success response


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
    if entityId != "some_existing_fiu_id":
        return jsonify({"responseCode": 404, "responseText": "FIU is not found."}), 404

    # Perform the delete operation here
    # Example:
    # delete_fiu(entityId)

    # Return success response
    return jsonify({"responseCode": 200, "responseText": "FIU deleted successfully"}), 200




if __name__ == '__main__':
    app.run(debug=True)
