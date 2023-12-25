from clean_data import clean_data

def test_clean_hts_request_with_valid_data():
    request_id = 21912
    result = clean_data(request_id)
    assert result is not None

def test_clean_hts_request_with_invalid_data():
    request_id = 456
    result = clean_data(request_id)
    assert result is None
