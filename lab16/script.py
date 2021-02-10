import logging
import subprocess
import sys

import time

start_time = time.time()

logging.basicConfig(filename="sample.log", level=logging.INFO)
logging.info('Starting script')
logging.info('Started with time {}'.format(start_time))
logging.info("Getting arguments {}".format(sys.argv))
try:
    logging.info('Start first program with argument {}'.format(sys.argv[1]))
    subprocess.Popen(['python', '../lab16/lab1314/main.py', sys.argv[1]])
    logging.info('Start second program without argument')
    subprocess.Popen(['python', '../lab16/lab15/lab15.py'])
    logging.info('Start third program without argument')
    subprocess.Popen(['python', '../lab16/lab15/lab15_2.py'])
    temp = time.time() - start_time
    logging.info('Script done with time - {}'.format(temp))
except Exception as e:
    print(e)

