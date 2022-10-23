import requests
import json
from requests.auth import HTTPBasicAuth

token = 'sqp_383fb4d1e0c0901bf1db4e6b16dff602a06290cf'
PARAM = {'component': 'project', 'metricKeys': 'complexity'}
admin = 'admin'
test_url = 'http://localhost:9000/api/measures/component_tree'
test_response = requests.get(test_url, auth=HTTPBasicAuth(username=admin, password="admin1"), verify=False, params=PARAM)
test_json = test_response.json()

json_object = json.dumps(test_json, indent=4)

# Writing to sample.json
with open("../Data/SonarQube_cyclomatic_complexity.json", "w") as outfile:
    outfile.write(json_object)
