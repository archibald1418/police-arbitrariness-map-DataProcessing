# Лемматизация описаний. Сжатие текстов для определения ключевых слов.

"""Вместо паймастем можно попробовать пайморфи.
Он лучше справляется с бастардами и там есть морфоанализатор.
Там нет разрешения омонимии, но ее сделали другие чуваки: проект PyPi: rnnmorph"""

import re
from collections import defaultdict, namedtuple

import pandas as pd
import numpy as np

import pymystem3

import constants

import write_lemmas_to_file


MYSTEM = pymystem3.Mystem(entire_input=False, disambiguation=True)

# Frequency distribution of lemmas
LEMMAS = defaultdict(lambda: 0)

# Lemmas and their hashes
LEMMAS_HASHES = dict()


# Filter for non-proper Nouns (S) and all Verbs (V)
PAT = re.compile('([SV]),(?!имя,|фам,|сокр=|гео)')


""" FIXME: Лемматизация происходит для двух задач: 
    - составление ключ слов
    - классификация строк описаний на основе ключевых слов
    """
# Добавит в дату просто колонку с леммами


def get_lemmas(DATA):
    '''

    Read detention descriptions from csv-table.
    Get list of RELEVANT lemmas with their frequencies as dict(int)
    Relevant -> nouns and verbs (S, V from Yandex MyStem tags)
    '''

    data = DATA

    # Add column for lemmatizaion output
    data["Lemmas"] = np.nan
    data['Lemmas'] = data['Lemmas'].astype(object)

    # Get a note and a long description of detention from DATA
    descr_col = ['source_type', 'source_description']

    # Wipe out all None, NaNs in descr. Leave an empty string
    data[descr_col] = data[descr_col].fillna(value='')

    #TODO: Итерируемся просто по датафрейму и цепляем все, что нужно
    # Оставляя за собой в новой колонке лемматизацию строки
    # Код станет понятнее в разы

    for i in data.index:
        # Loop through both columns at the same time
        # We lemmatize all available detention info

        # Add all lemmas to row
        lemmas_to_df_row = []

        # Get full description
        row_descr = data.loc[i, descr_col]

        # Join columns to lemmatize
        text = ' '.join(row_descr)

        # Parse
        parse = MYSTEM.analyze(text=text)

        for a in parse:

            for word in a['analysis']:
                # Won't loop if a['analysis'] is an empty list
                # With MYSTEM.disambiguation=False loops through all possible variants
                # With MYSTEM.disambiguation=True loops through list of length 1

                pos_tag = word.get('gr', '#')
                # Get pos-tag of word if MyStem parsed it
                # Else return a placeholder

                # TODO: Подумать, что делать с out-of-vocab (и нужно ли вообще?)

                if PAT.match(pos_tag):
                    # Filter for non-proper Nouns (S) and all Verbs (V)
                    # FIXME: Эта проверка не гарантирует потерю ложно позитивных out-of-vocab

                    # Get lemma of the word
                    lemma = word.get('lex', '').lower()

                    # Add lemma to dataframe
                    lemmas_to_df_row.extend([lemma])

                    # Add lemma into dict and assign a hash
                    LEMMAS[lemma] += 1
                    LEMMAS_HASHES[lemma] = hash(lemma)

        # Add lemmas to column "Lemmas" in this row
        data.at[i, "Lemmas"] = lemmas_to_df_row

    return data



def main(DATA):
    # DATA will be loaded from __main__.py

    print('List of lemmas is being created...')

    lemmatized_data = get_lemmas(DATA)

    print('List of lemmas and frequencies is created!')

    print('Writing lemmas to csv file...')

    lemmas_freqdist = LEMMAS
    write_lemmas_to_file.write_lemmas_to_file(lemmas_freqdist)

    print('Lemmas-frequencies file can be found at ', constants.LEMMAS_PATH)

    #TODO: Кинуть обновленный датафрейм в жесткий диск
    # Или последовательно написать в __main__.py

    Output = namedtuple('Output', ['lemmas_hashes', 'lemmatized_data'])
    output = Output(LEMMAS_HASHES, lemmatized_data)

    return output


if __name__ == '__main__':
    # If in debug mode load data straight from here

    DATA = pd.read_csv(constants.DATA_PATH, index_col='id')
    main(DATA)