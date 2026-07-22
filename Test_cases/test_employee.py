import pytest

class TestLogin:
   # @pytest.mark.flaky(reruns=3) ##@pytest.mark.flaky is available only when the appropriate plugin is installed
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_valid_login(self):
        pass


    @pytest.mark.regression
    @pytest.mark.xfail
    def test_invalid_login(self):
        pass