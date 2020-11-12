import pytest
import requests
import sys
sys.path.insert(0, '/Users/adeoke/Documents/rest_api_testing/helpers')
from config import Config 


def test_get_employees():
    employees_all_employees = Config.api_details_for('host')+Config.api_details_for('all_employees')
    response = requests.get(employees_all_employees)
    assert response.status_code == 200


def test_get_verify_first_employee_details():
    employees_all_employees = Config.api_details_for('host')+Config.api_details_for('all_employees')
    response = requests.get(employees_all_employees)
    response_json = response.json()
    assert response_json['data'][0]['id'] == '1'
    assert response_json['data'][0]['employee_name'] == "Tiger Nixon"
    assert response_json['data'][0]['employee_salary'] == '320800'
    assert response_json['data'][0]['employee_age'] == '61'


