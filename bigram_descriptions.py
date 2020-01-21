import pandas as pd
import numpy as np
import pymystem3
import nltk

from nltk import bigrams, FreqDist
from collections import Counter

# Импорт настроек, и MyStem-объект
from lemmatize_descriptions import MYSTEM

DESCRIPTION = '/Users/user/Desktop/zaderzhania_lemmatize.txt'

DIR = '/Users/user/Desktop/'


def get_bigrams ():
    '''
    Read detention descriptions from xlsx-table.
    Retrieve list lemma bigrams with their frequencies as Counter object
    :return: Counter object {bigram : count}
    '''

    print('List of lemma bigrams is being created...')

    file = open(DESCRIPTION)
    text = file.read()
    file.close()

    bigr = bigrams(MYSTEM.lemmatize(text, speedup=True))
    # nltk.bigrams works on already lemmatized text

    print('List of lemma bigrams and frequencies is created!')

    return bigr


def write_bigrams_to_file ():
    '''
    Write lemma bigrams and their frequencies to csv file for further analysis.
    Sort from most to least occurences.
    '''

    print('Writing bigrams to csv file...')

    directory = DIR + 'bigram_descriptions.txt'

    newfile = open(directory, 'w')

    bigr = get_bigrams()

    bigr_fd = FreqDist(bigr)
    # bigram frequency distribution

    frmt = '{}\t{}\n'
    for bigram, count in bigr_fd.most_common():
        newfile.write(frmt.format(' '.join(bigram), count))

    print('The lemma bigrams-freq file can be found at ', newfile.name)

    newfile.close()


write_bigrams_to_file()
