import pandas as pd
import numpy as np

import pymystem3

import keywords_dict
import lemmatize_descriptions
import constants

from collections import namedtuple

# Save data to:
DATA_DIR = constants.DATA_DIR

DATA = pd.read_csv(constants.DATA_PATH, index_col='id')

# Lemmatize descriptions from csv file
# This gets hashed lemmas and lemmatized lines
lemmatize_output = lemmatize_descriptions.main(DATA)


# Lemmatized descriptions
lemmatized_data = lemmatize_output.lemmatized_data

LEMMAS_HASHES = lemmatize_output.lemmas_hashes

# Get keyword mapping
keywords_dict_output = keywords_dict.main()
KEYWORDS_DICT = keywords_dict_output
CATEGORIES = KEYWORDS_DICT.keys()



def isnan(x):
    '''

    Check if x is NOT a np.nan type
    return bool
    '''

    return not (x is np.nan)


def build_objects_features_dataframe(raw_dataframe):
    '''
    raw_dataframe is read from csv_file

    ::param csv_file table (id, ovd, source_type, source_description)
    :return Pandas.DataFrame with zeros

    - Create resulting dataframe from csv table (id, ovd, source_type, source_description)

    id: id from source data. TODO: прописать путь к таблице с самыми исходными данными
    ovd: police department name (cyrillic)
    source_type: author's notes on detention (cyrillic)
    source_description: verified description of detention (cyrillic)

    - Filter for non-empty OVDs

    - Add feature columns (final_type) and fill them with 0

    The resulting is detention_description - detention_type (object - features) table with zeros
    '''


    #TODO: Проверка на валидность наименования ОВД

    # If no ovd  - this row has to go
    df = raw_dataframe.copy()
    df = df[~pd.isnull(df['ovd'])]

    # Таблица с нулями для классификации
    for cat in CATEGORIES:
        # Цикл, чтобы убедиться, что по ключам все совпадает

        df[cat] = 0.0


    return df



def has_offence(lemmas, offence, keywords):
    '''
    From source_type, source_description and keywords infer
    whether the offence has happened.
    Based on ANY intersection of lemmas with keywords for given offence type

    :params
        - lemmas: list of lemmas from both descriptions
        - offnece: offence type (final_type)
        - keywords: set of keywords for given offence type

    :return
        - TRUE if intersection
        - FALSE if no intersection (empty set)
    '''

    lemmaset = set(lemmas)
    keywords = KEYWORDS_DICT[offence]

    lemmas_hashes = {LEMMAS_HASHES[lemma] for lemma in lemmaset}
    keywords_hashes = {LEMMAS_HASHES[keyword] for keyword in keywords}


    has_offence = bool(lemmas_hashes & keywords_hashes)

    return has_offence


def classify(dataframe, keyword_dict=KEYWORDS_DICT):
    """
    Classify full descriptions based on keywords.
    Change dataframe filled with 0 and 1 based on has_offence function.

    :params
        - dataframe: Pandas.DataFrame with description and offence types
        - keyword_dict: offence type to keywords set mapping from keywords_dict.py
    """

    kw = keyword_dict


    indices = dataframe.index
    # Индексирование по pd.DataFrame.index - это массив индексов

    for i in indices:

        source_type = dataframe.loc[i, 'source_type']
        source_description = dataframe.loc[i, 'source_description']
        lemmas = dataframe.loc[i, 'Lemmas']


        for cat in CATEGORIES:

            # Get keywords for the category
            keywords = kw[cat]

            # Find if has intersection (=has offence)
            if_offence = has_offence(lemmas=lemmas, offence=cat, keywords=keywords)

            # update dataframe with 1 or 0
            value = int(if_offence)

            # Set the value
            dataframe.at[i, cat] = value


    return dataframe


def main():
    data = lemmatized_data

    # Строим матрицу объектов - признаков
    # Добавляем колонки с признаками и заполняем нулями
    class_matrix = build_objects_features_dataframe(data)

    # Запускаем классификатор, который меняет датафрейм
    class_results = classify(dataframe=class_matrix)

    class_results.to_csv(DATA_DIR + 'opisaniya_zaderzhaniy_class_matrix.csv')
    class_results.to_excel(DATA_DIR + 'opisaniya_zaderzhaniy_class_matrix.xlsx')

    return class_results


if __name__ == '__main__':
    main()

# Импортировать внутри if __name__ или наверху?




