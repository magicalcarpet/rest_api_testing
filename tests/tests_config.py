import pytest
import sys

sys.path.insert(0, '/Users/adeoke/Documents/rest_api_testing/helpers')
from config import Config 

def test_config_for_host():
    host = Config.api_details_for('host')
    assert host == 'http://dummy.restapiexample.com/api/v1/'


def test_config_for_endpoint():
    endpoint = Config.api_details_for('endpoint')
    assert endpoint == 'employees'

