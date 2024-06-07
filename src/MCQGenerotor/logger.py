import logging
import os
from datetime import datetime




LOG_FILE =  f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"

log_path = os.path.join(os.getcwd(), 'logs')

os.makedirs(log_path,exist_ok=True)

LOG_FILEPATH = os.path.join(log_path,LOG_FILE)


logging.basicConfig(level= logging.INFO, filename = LOG_FILEPATH, format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s')
# [2024-06-07 17:44:03,207] 3 root - INFO - i am going to start the execution..   -> output like this


