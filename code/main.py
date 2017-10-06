#!/usr/bin/env python


import os
import glob
import sys
import surveygen

REPO_PATH = './'
sys.path.append(REPO_PATH)
output_folder = './output'
input_folder = './input'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)


for txt_file in glob.iglob(os.path.join(input_folder, '*.txt')):
    surveygen.survey_pipeline(txt_file, output_folder)

for subfolder in os.listdir(input_folder):
    input_subfolder_path = os.path.join(input_folder, subfolder)
    output_subfolder_path = os.path.join(output_folder, subfolder)
    for txt_file in glob.iglob(os.path.join(input_subfolder_path, '*.txt')):
        if not os.path.exists(output_subfolder_path):
            os.makedirs(output_subfolder_path)
        surveygen.survey_pipeline(txt_file, output_subfolder_path)
