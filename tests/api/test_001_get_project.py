from requests.auth import HTTPBasicAuth

from infra.api.projects_api import ProjectsApi
from main_config import config
import requests


def test_something():
    project_id = 368
    url = f"{config['base_url']}/api/v3/projects/{project_id}"
    basic_auth = HTTPBasicAuth('apikey', '63c179dae3358a43245a1a3ba7ece45c1762bd5a8d9266395f18415e336aad05')
    response = requests.get(url, auth=basic_auth)
    assert response.status_code == 200


def test_001_get_project():

    projects_api = ProjectsApi(config['base_url'])

    project_id = config['project_id']
    expected_project_name = "TestProject1"
    expected_project_description = "This is the first test project"

    project = projects_api.get_project(project_id)

    assert project["name"] == expected_project_name, f"Project name should be '{expected_project_name}'"
    assert project["description"]["raw"] == expected_project_description, f"Project description should be '{expected_project_description}'"
