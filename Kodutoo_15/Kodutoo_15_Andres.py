'''
Kodutoo 15
11.11.2014
Andres Liiver
'''

import re
import sympy as sp
import numpy as np
from matplotlib import pyplot as plt

def get_data_from_csv(file):
    data = {}
    file_contents = file.read()
    data['years'] = re.findall(r'(?!")\d{4}(?=")', file_contents)
    return data

def main():
    file = open("RV030s.csv")
    data = get_data_from_csv(file)
    print(data)
    file.close()

if __name__ == "__main__":
    main()
