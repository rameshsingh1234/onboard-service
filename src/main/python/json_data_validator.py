import os

from src.unittest.python.utils import read_file


class JsonDataValidator:

    @staticmethod
    def relational_validator(data):
        validation_spec = read_file.read_data(os.path.join(os.path.dirname(__file__), "resources","data_validation_spec.json"))
        for i in validation_spec['comparison']:
            if i['type'] == "equals":
                validation_result = []
                for keys in i['keys']:
                    requester_name = data[(keys[0].split('.')[0])][(keys[0].split('.')[1])]
                    entity_name = data[(keys[1].split('.')[0])][(keys[1].split('.')[1])]
                    print(requester_name, entity_name)
                    res = JsonDataValidator.compare_values(data[(keys[0].split('.')[0])][(keys[0].split('.')[1])],
                                                           data[(keys[1].split('.')[0])][(keys[1].split('.')[1])])
                    validation_result.append(res)
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
