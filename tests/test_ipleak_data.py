from ipleak.functions.ipleak import ipleak_string
from ipleak.exceptions import NoIPFound
import os
import json
import pytest

# get data folder
this_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(this_dir, 'data/ipleak_returns.json')

with open(data_path, 'r') as f:
    ipleak_returns = json.load(f)


def test_exception_noipfound():
    with pytest.raises(NoIPFound):
        assert ipleak_string('T', ipleak_returns['missing_ip'])


def test_ipleak_returns():
    assert '123.53.232.22' in ipleak_string('T', ipleak_returns['ip'])

    assert '123.53.232.22' in ipleak_string(
        'T', ipleak_returns['missing_city_name'])
    assert 'test_country' in ipleak_string(
        'T', ipleak_returns['missing_city_name'])

    assert '123.53.232.22' in ipleak_string(
        'T', ipleak_returns['missing_country_name'])
    assert 'test_city' in ipleak_string(
        'T', ipleak_returns['missing_country_name'])

    assert '123.53.232.22' in ipleak_string(
        'T', ipleak_returns['everything'])
    assert 'test_city' in ipleak_string(
        'T', ipleak_returns['everything'])
    assert 'test_country' in ipleak_string(
        'T', ipleak_returns['everything'])
