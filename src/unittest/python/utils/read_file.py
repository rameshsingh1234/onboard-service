import os
import json


def read_data(data_file_path):
    if not os.path.exists(data_file_path):
        raise FileNotFoundError(f"File not found at: {data_file_path}")
    with open(data_file_path, "r") as dataFile:
        return json.load(dataFile)


def read_headers():
    resource_dir = os.path.join(os.path.dirname(__file__), "..", "resources")
    header_file = os.path.join(resource_dir, "testHeaders.json")
    # print("Header file path:", header_file)
    return read_data(header_file)


def read_entities():
    resource_dir = os.path.join(os.path.dirname(__file__), "..", "resources")
    entities_file = os.path.join(resource_dir, "testEntities.json")
    # print("data file path:", entities_file)
    return read_data(entities_file)


read_headers = read_headers()
read_entities = read_entities()
