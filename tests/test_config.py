import pytest
import sys

sys.path.insert(0, '/Users/adeoke/Documents/rest_api_testing/helpers')
from config import Config 

def test_config_for_key_host():
    host = Config.api_details_for('host')
    assert host == 'http://dummy.restapiexample.com/api/v1/'


def test_config_for_key_all_employees():
    all_employees = Config.api_details_for('all_employees')
    assert all_employees == 'employees'

def test_config_for_invalid_key():
    with pytest.raises(KeyError, match=r'invalid_key'):
        Config.api_details_for('invalid_key')    
        
    

