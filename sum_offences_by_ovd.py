import pandas as pd
import numpy as np
import nltk
import pymystem3

import classify_table
import constants


def main():

    # Get names of categories
    CATEGORIES = list(constants.CATEGORIES_ENG.values())

    # Where to save report
    DATA_DIR = constants.DATA_DIR

    # Classify offences
    classification_results = classify_table.main()

    # Pick ovds and offences for report
    cols = ['ovd'] + CATEGORIES
    to_report = classification_results.loc[:, cols]

    # TODO: Посмотреть, как использовать аггрегатные функции
    # Sum offences by ovd
    sum_report = to_report.groupby(by='ovd')[list(CATEGORIES)].agg('sum')

    sum_report.to_csv(DATA_DIR + 'ovd_offence_report.csv')
    sum_report.to_excel(DATA_DIR + 'ovd_offence_report.xlsx')

    # Перегнать в джсон TODO: (как это сделать удобнее и по формату??)
    sum_report.to_json(DATA_DIR + 'ovd_offence_report.json', orient='index', force_ascii=False)

    return sum_report


if __name__ == '__main__':
    main()





