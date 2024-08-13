import json

with open('plugin-metadata\plugin_names.txt', 'r') as file:
    plugin_names = [line.strip() for line in file if line.strip()]

plugins_dict = {"plugins": {name: "" for name in plugin_names}}

with open('plugin-metadata.json', 'w') as json_file:
    json.dump(plugins_dict, json_file, indent=4)

print("JSON file created successfully!")
