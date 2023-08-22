import os
import json

RESOURCE_DIR = os.path.join(os.path.dirname(__file__), "..", "resources/schema")


def read_data(data_file_path):
    if not os.path.exists(data_file_path):
        raise FileNotFoundError(f"File not found at: {data_file_path}")
    with open(data_file_path, "r") as dataFile:
        return json.load(dataFile)


def read_schemas(schema_file_name):
    """Function to read schema files"""
    file = os.path.join(RESOURCE_DIR, schema_file_name)
    return read_data(file)


def aa_read_schemas():
    return read_schemas("aa-schema.json")


def fip_read_schemas():
    return read_schemas("fip-schema.json")


def fiu_read_schemas():
    return read_schemas("fiu-schema.json")


def read_headers():
    resource_dir = os.path.join(os.path.dirname(__file__), "..", "resources")
    header_file = os.path.join(resource_dir, "testHeaders.json")
    return read_data(header_file)


read_headers = read_headers()

# import os
# import json
#
#
# RESOURCE_DIR = os.path.join(os.path.dirname(__file__), "..", "resources/schema")
#
# def read_data(data_file_path):
#     if not os.path.exists(data_file_path):
#         raise FileNotFoundError(f"File not found at: {data_file_path}")
#     with open(data_file_path, "r") as dataFile:
#         return json.load(dataFile)
#
#
# def read_headers():
#     resource_dir = os.path.join(os.path.dirname(__file__), "..", "resources")
#     header_file = os.path.join(resource_dir, "testHeaders.json")
#     return read_data(header_file)
#
#
# def read_schemas():
#     """Function to read file"""
#     resource_dir = os.path.join(os.path.dirname(__file__), "..", "resources/schema")
#     file = os.path.join(resource_dir, "fiu-schema.json")
#     return read_data(file)
#
#
# def aa_read_schemas():
#     """Function to read file"""
#     resource_dir = os.path.join(os.path.dirname(__file__), "..", "resources/schema")
#     file = os.path.join(resource_dir, "aa-schema.json")
#     return read_data(file)
#
#
# def fip_read_schemas():
#     """Function to read file"""
#     resource_dir = os.path.join(os.path.dirname(__file__), "..", "resources/schema")
#     file = os.path.join(resource_dir, "fip-schema.json")
#     return read_data(file)
#

