from rentomatic.response_objects import response_objects as res


def test_response_success_is_true():
    assert bool(res.ResponseSuccess()) is True
