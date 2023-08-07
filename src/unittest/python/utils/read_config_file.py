import json
import yaml
import os


def read_config(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()

    with open(file_path) as config_file:
        if file_extension == '.json':
            config = json.load(config_file)
        elif file_extension in ['.yaml', '.yml']:
            config = yaml.safe_load(config_file)
        else:
            raise ValueError("Unsupported file format. Supported formats: json, yaml")
    return config
