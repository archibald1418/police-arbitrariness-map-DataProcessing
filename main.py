#!/usr/bin/env python3



import re
from collections import defaultdict, namedtuple

import pandas as pd
import numpy as np

import pymystem3

import lemmatize_descriptions
import keywords_dict
import classify_table
import sum_offences_by_ovd
import write_lemmas_to_file

import constants


def parse_data(data):
    '''Parse loaded data, save temp files to data/'''

    parsed_data = sum_offences_by_ovd.main()

    return parsed_data


def load_data(path):
    '''Load csv file to Pandas.DataFrame'''

    DATA = pd.read_csv(path, index_col='id')

    return DATA


def main(path=constants.DATA_PATH):
    ''''''

    print('Loading data...')
    print()

    # Load data

    data = load_data(path)

    print('Data succesfully loaded!')
    print()

    print('Classifying ovds by offences...')
    print()

    # Classification report
    parsed_data = parse_data(data)

    print('Classifying finished!')
    print('Report can be found at data/ovd_offence_report.csv')
    print('Json can be data/found at ovd_offence_report.json')

    return

if __name__ == '__main__':
    main()
