import json
def load_config_data(file_path):
    with open(file_path) as f:
        return json.load(f)
    
def parametrize_generator(config_file_path, *keys):
    config_data = load_config_data(config_file_path)
    value_keys = keys[1:]
    key_string = ", ".join(keys)
    value_list = []
    for key, values in config_data.items():
        if all([value_name in values for value_name in value_keys]):
            value_list.append((key, *[values[value_name] for value_name in value_keys]))
    return key_string, value_list