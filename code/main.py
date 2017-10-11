#!/usr/bin/env python

import logging
import logging.handlers

import os
import glob
import sys
from datetime import datetime
import time

import smdpipeline

start_time = time.time()

REPO_PATH = './'
sys.path.append(REPO_PATH)
output_folder = './output'
input_folder = './input'
logs_folder = './logs'

if not os.path.exists(logs_folder):
    os.makedirs(logs_folder)

logger = logging.getLogger(__name__)
fh = logging.handlers.RotatingFileHandler("".join([logs_folder,
                                                   '/',
                                                   datetime.strftime(datetime.today(), "%m%d%Y_%H%M"),
                                                  'debug.log']
                                                  ),
                                          maxBytes=1000000,
                                          backupCount=10)
fh.setLevel(logging.DEBUG)
fh2 = logging.handlers.RotatingFileHandler("".join([logs_folder,
                                                    '/',
                                                    datetime.strftime(datetime.today(), "%m%d%Y_%H%M"),
                                                   'info.log']
                                                   ),
                                           maxBytes=1000000,
                                           backupCount=10)
fh2.setLevel(logging.INFO)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(1)
fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
fh2.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
ch.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))

root = logging.getLogger()
root.setLevel(logging.INFO)

root.addHandler(fh)
root.addHandler(fh2)
root.addHandler(ch)

logger.info("Program started")


if not os.path.exists(output_folder):
    os.makedirs(output_folder)


for txt_file in glob.iglob(os.path.join(input_folder, '*.txt')):
    smdpipeline.survey_pipeline(txt_file, output_folder)

for subfolder in os.listdir(input_folder):
    input_subfolder_path = os.path.join(input_folder, subfolder)
    output_subfolder_path = os.path.join(output_folder, subfolder)
    for txt_file in glob.iglob(os.path.join(input_subfolder_path, '*.txt')):
        if not os.path.exists(output_subfolder_path):
            os.makedirs(output_subfolder_path)
        smdpipeline.survey_pipeline(txt_file, output_subfolder_path)
execution_time = int((time.time() - start_time)*1000)
logger.info("Done! Execution time: {} milliseconds" .format(execution_time))

