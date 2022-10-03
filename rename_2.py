import pandas as pd
import glob
import os
folder = os.getcwd()
files = glob.glob('*.txt')
combined = pd.DataFrame()

for file in files:
    data = pd.read_txt(file)
    data['result_filename'] = file
    combined = pd.concat([combined, data])