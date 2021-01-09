from ipleak.functions import print_ipleak_data

possible_returns = [
    {'ip': '127.0.2.1'},
    {'ip': '120.2.1.1'},
    {'ip': 'FE80::1'}
]


def test_ipleak_data() -> None:
    for data in possible_returns:
        assert print_ipleak_data('IP', data) == True
