import pytest
from utilities.custome_logger import LogGen
import sys
class TestEmployee:
    log=LogGen.log_gen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_employee(self):
        self.log.info("function executing -test_add_employee")
        pass
    
    @pytest.mark.skip
    def test_delete_employee(self):
        self.log.info("function executing -test_delete_employee")
        pass


    @pytest.mark.e2e
    def test_employee_workflow(self):
        self.log.info("function executing -test_employee_workflow")
        pass
    @pytest.mark.regression
    @pytest.mark.skipif(sys.platform == "linux",reason="Platform specific")
    def test_log_out(self):
        self.log.info("function executing -test_log_out")
        pass

    @pytest.mark.skipif("plaform=linux",reason="platform specifice")
    def test_log_out(self):
        self.log.info("function executing -test_log_out")
        pass
    
    @pytest.mark.xfail(reason="know defact")
    def test_log_out(self):
        self.log.info("function executing -test_log_out")
        pass