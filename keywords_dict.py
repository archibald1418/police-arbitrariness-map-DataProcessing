# Классификация по ключевым словам

import pickle
import numpy as np
import nltk
import pymystem3
import pandas as pd
from collections import defaultdict

import constants


KEYWORDS_DICT = defaultdict(set)

# TODO: Все-таки хочется сравнить полуручную работу с хи-квадратом, фишером и др. тестами
# Тогда нужны ожидаемые частоты и небольшой подкорпус

#TODO: На основании тех же тестов можно удалить ненадежные (общие) слова


def conserve_KeywordsDict (keywords_dict):
    '''

    Take keywrods_dict and dump it to .pkl using pickle library
    '''

    obj = keywords_dict

    path = constants.DATA_DIR + 'keywords.pickle'
    output = open(path, 'wb')

    pickle.dump(obj, file=output, protocol=2)

    print('Pickle file can be found at ', output.name)



def read_to_dataframe ():
    '''
    
    - Read csv with keywords to Pandas.DataFrame for further computations
    - Erase empty columns
    - Sort by final_type column

    'Final_type' column - final offence types

    :return: Pandas.DataFrame (lemma, final_type)
    '''

    print('Filtering and sorting data...')

    df = pd.read_csv(constants.KeywordsDict_PATH)
    # Load csv with keywords to pandas

    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    # Filter table to remove "Unnamed" columns

    df_sorted = df.loc[:, ['LEMMA', 'final_type']].sort_values(by='final_type')
    # Sort by detention final type

    return df_sorted


def map_keywords_to_type(df):
    '''

    This adds to KEYWORDS_DICT dict(set) where

    keys:   offence types
    values: set of keywords flagged by final_type column

    dataframe: (LEMMA, final_type) columns sorted by offence types
    '''

    print('Mapping sets of keywords to detention types...' + '\n')


    keywords_file = open(constants.DATA_DIR + 'keywords_mapping.txt', 'w')

    frmt = '{0}\t{1}\n'
    for cat in df['final_type'].unique():

        eng_cat = constants.CATEGORIES_ENG[cat.strip()]

        keywords = {word.strip() for word in df[df['final_type'] == cat]['LEMMA']}
        KEYWORDS_DICT[eng_cat] = keywords
        # Map LEMMAS with current final_type to english category

        line = frmt.format(cat, keywords)
        keywords_file.write(line)
        # Write keywords to text file

    keywords_file.close()


    print()
    print('Keyword sets are mapped to offence types')
    print()
    print('You can check keywords at ', keywords_file.name)

    conserve_KeywordsDict(KEYWORDS_DICT)


def main():

    df_clean = read_to_dataframe()
    map_keywords_to_type(df_clean)

    return KEYWORDS_DICT

if __name__ == '__main__':
    main()


