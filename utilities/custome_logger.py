import logging 
import os

worker = os.getenv("PYTEST_XDIST_WORKER", "master")
print(worker)
if worker=="master":
    worker="master"
class LogGen:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename=f".\\Logs\\test_{worker}.log",level=logging.INFO,format="%(asctime)s | %(levelname)s | %(filename)s | %(funcName)s| Line:%(lineno)d | %(message)s",
                            datefmt='%d-%b-%y %H:%M:%S',filemode="w", force=True)
        

        return logging.getLogger()
    

