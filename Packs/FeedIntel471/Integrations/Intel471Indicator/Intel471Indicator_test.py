import pytest
import Intel471Indicator as feed

BUILD_PARAM_DICT_DATA = [
    (
        {'credentials': {'identifier': 'username', 'password': 'apikey'}, 'insecure': True,
         'search_indicator_type': 'ipv4', 'confidence': 'high', 'auto_detect_type': False, 'proxy': True},  # input
        {'confidence': 'high'}  # expected

    ),
    (
        {'credentials': {'identifier': 'username', 'password': 'apikey'}, 'insecure': True,
         'auto_detect_type': False, 'proxy': True},  # input
        {}  # expected

    ),
    (
        {'credentials': {'identifier': 'username', 'password': 'apikey'}, 'insecure': True,
         'search_indicator_type': 'ipv4', 'threat_type': 'malware', 'confidence': 'high', 'auto_detect_type': False,
         'proxy': True},  # input
        {'confidence': 'high', 'threatType': 'malware'}  # expected
    )
]


@pytest.mark.parametrize("input,expected_results", BUILD_PARAM_DICT_DATA)
def test_build_url_parameter_dict(mocker, input, expected_results):
    """
    Given:
        - set of parameters from demisto.

    When:
        - create an instance and on every run.

    Then:
        - Returns a dictionary of relevant params only.

    """
    params_dict = feed._build_url_parameter_dict(**input)
    assert params_dict == expected_results


BUILD_URL_DATA = [
    (
        {'confidence': 'high', 'indicatorType': 'ipv4'},  # input
        'https://api.intel471.com/v1/indicators/stream?confidence=high&indicatorType=ipv4'  # expected

    ),
    (
        {},  # input
        'https://api.intel471.com/v1/indicators/stream?'  # expected

    )
]


@pytest.mark.parametrize("input,expected_results", BUILD_URL_DATA)
def test_create_url(mocker, input, expected_results):
    """
    Given:
        - set of parameters from demisto.

    When:
        - create an instance and on every run.

    Then:
        - Returns a url for a get request.

    """
    url = feed._create_url(**input)
    assert url == expected_results


def test_create_relationships():
    config = {'relation_entity_b_type': 'STIX Malware', 'relation_name': 'communicates-with'}
    indicator_data = {'type': 'URL', 'threat_data_family': 'test_malware', 'indicator_type': 'url',
                      'indicator_data_url': 'http://example_url.com', 'value': 'http://example_url.com'}
    mapping = {'threat_data_family': 'malwarefamily', 'indicator_data_url': 'url',
               'relation_entity_b': 'threat_data_family'}

    res = feed.custom_build_relationships(config, mapping, indicator_data)
    assert res[0] == {'name': 'communicates-with', 'reverseName': 'communicated-by', 'type': 'IndicatorToIndicator',
                      'entityA': 'http://example_url.com', 'entityAFamily': 'Indicator', 'entityAType': 'URL',
                      'entityB': 'test_malware', 'entityBFamily': 'Indicator', 'entityBType': 'STIX Malware',
                      'fields': {}}
