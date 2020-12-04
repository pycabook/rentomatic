from rentomatic.responses import ResponseSuccess


def test_response_success_is_true():
    assert bool(ResponseSuccess()) is True
