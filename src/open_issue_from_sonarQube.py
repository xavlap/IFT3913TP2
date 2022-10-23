# Pour arriver à cette métrique nous avons installer

# sonar-scanner
#     -Dsonar.projectKey=project\
#     -Dsonar.sources=.\
#     -Dsonar.host.url=http://localhost:9000\
#     -Dsonar.login=sqp_383fb4d1e0c0901bf1db4e6b16dff602a06290cf\
#     -Dsonar.java.binaries=target\
#     -Dsonar.analysis.mode=preview
#     -Dsonar.issuesReport.html.enable=true

import requests
import json
from requests.auth import HTTPBasicAuth
token = 'sqp_383fb4d1e0c0901bf1db4e6b16dff602a06290cf'
PARAM = {'componentKey': 'project', 'additionalFields': '_all'}
test_url = 'http://localhost:9000/api/issues/search'
test_response = requests.get(test_url, auth=HTTPBasicAuth(username=token, password=""), verify=False,params=PARAM)
test_json = test_response.json()

json_object = json.dumps(test_json, indent=4)

# Writing to sample.json
with open("../SonarQube_open_issues.json", "w") as outfile:
    outfile.write(json_object)

