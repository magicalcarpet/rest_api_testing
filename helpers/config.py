import yaml
import os

# This class exists soley to read the yaml file for us

class Config():
    @classmethod  
    def api_details_for(cls, key_name):
        path_to_file = os.path.realpath(__file__)
        directory = os.path.dirname(path_to_file)
        parent = os.path.dirname(directory)
        yaml_file = os.path.join(parent, 'config.yaml')
        
        with open(yaml_file) as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            return data['api'][key_name]
    

# host = Config.api_details_for('host')
# endpoint = Config.api_details_for('endpoint')
# print(host + endpoint)

