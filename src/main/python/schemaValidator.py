from jsonschema import validate
from jsonschema.exceptions import ValidationError


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
