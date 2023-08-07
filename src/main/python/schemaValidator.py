#import necessary libraries

import jsonschema
from jsonschema import validate
from jsonschema.exceptions import ValidationError

# class SchemaValidator:
#
#     def validate_json(self):
#         """
#         file name should start with entity name
#         validate the file name according to the entity type
#         handle the exception with the try block load the schema file
#         use json library validate() method to validate the instance(requestBody) and schema(schema)
#         """
#
#     def validate_enum(self):
#         """
#         parse the json data using json loads
#         and use validate() method to verify the enum values from the schema.
#         """


class SchemaValidator:
    def __init__(self, schema):
        self.schema = schema

    def is_valid(self, data):
        try:
            validate(instance=data, schema=self.schema)
            return True
        except ValidationError:
            return False

    def validate_or_raise(self, data):
        validate(instance=data, schema=self.schema)
