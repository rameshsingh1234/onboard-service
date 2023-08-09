import ast
import json

from src.unittest.python.utils import read_file

data = {
    "ver": "1.0",
    "timestamp": "2023-07-19T12:34:56",
    "txnid": "abcd1234",
    "requester": {
        "name": "John",
        "id": "user1234"
    },
    "entityinfo": {
        "name": "saveEntity",
        "id": "entity45645",
        "code": "ENT1234",
        "entityhandle": "examples-entity",
        "baseurl": "https://examples.com",
        "webviewurl": "https://examples.com/webview",
        "certificate": {
            "alg": "RS256",
            "e": "AQAB",
            "kid": "key12345",
            "kty": "RSA",
            "n": "mzvzI3_E11...",
            "use": "sig"
        },
        "inboundports": ["8080", "8443"],
        "outboundports": ["80", "443"],
        "ips": ["192.168.1.1", "10.0.0.1"],
        "credentialsPk": {
            "alg": "RS256",
            "e": "AQAB",
            "kid": "key7894",
            "kty": "RSA",
            "n": "9s87F3S_D1...",
            "use": "enc"
        }
    }
}


class JsonDataValidator:

    def __init__(self):
        pass

    @staticmethod
    def relational_validator(data):
        validation_spec = read_file.read_data(
            '/home/krishna/Tibil/sahamati/onboard-service/src/main/python/resources/data_validation_spec.json')
        for i in validation_spec['comparison']:
            if i['type'] == "equals":
                count = 1
                validation_result =[]
                for keys in i['keys']:
                    print(keys)
                    print(count)
                    requester_name = data[(keys[0].split('.')[0])][(keys[0].split('.')[1])]
                    entity_name = data[(keys[1].split('.')[0])][(keys[1].split('.')[1])]
                    print(requester_name, entity_name)
                    res = JsonDataValidator.compare_values(data[(keys[0].split('.')[0])][(keys[0].split('.')[1])],
                                                           data[(keys[1].split('.')[0])][(keys[1].split('.')[1])])
                    validation_result.append(res)
                    count += 1
                    print(res)
                if all(validation_result):
                    return True
                else:
                    return False

    @staticmethod
    def compare_values(*values):
        if len(values) < 2:
            return "Provide at least two values for comparison"

        first_value = values[0]
        all_equal = all(value == first_value for value in values)

        if all_equal:
            return True
        else:
            return False
    # def compare_values(*values):
    #     values = list(kwargs.values())
    #     print("from compare values", values)
    #
    #     if len(values) < 2:
    #         return "Provide at least two values for comparison"
    #
    #     first_value = values[0]
    #     all_equal = all(value == first_value for value in values)
    #
    #     if all_equal:
    #         return True
    #     else:
    #         return False


# JsonDataValidator.relational_validator(data=data)
