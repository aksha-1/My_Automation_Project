import pytest

class TestLogin:

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_valid_login(self):
        pass


    @pytest.mark.regression
    @pytest.mark.xfail
    def test_invalid_login(self):
        pass