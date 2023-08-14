import os

absolute_path = os.path.dirname(__file__)
# relative_path = "resources/templates/"
# full_path = os.path.join(absolute_path, relative_path)
# os.rel


current_directory = os.path.dirname(__file__)  # Get the current directory of the script
config_file_path = os.path.join(current_directory, "config", "config_file.yaml")

upper_dir = os.path.join(os.path.dirname(current_directory), "config_file","q.yaml")


print(upper_dir)
data ={
    "baseurl":[]
}
data['baseurl'].clear()
data['baseurl'].append('http')
print(data)
