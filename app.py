from flask import Flask, request
import xmltodict
#import ruamel.yaml
import sys
import json, simplejson
import yaml

"""@package docstring
Documentation for the xml-to-yaml service
The service uses RESTful API and receives POST requests with xml
It sends the same data but in YAML format
"""



"""
Creating the main app
"""
app = Flask(__name__)

"""
Setting a POST request handler
Setting the service name to /xml/to/yaml/v1.0
"""
@app.route('/xml/to/yaml/v1.0', methods=['POST'])
def convert():
    """
    Convert xml data to dictionary format and then dump to YAML format
    :return:
    YAML message
    """
    d = xmltodict.parse(request.data)
    j = json.dumps(d)
    return yaml.dump(simplejson.loads(j), default_flow_style=False), 201



"""
Calling the handler
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
