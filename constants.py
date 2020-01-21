import pymystem3
import re
from collections import defaultdict
import pandas as pd


# Папка с данными для обработки
DATA_DIR = 'data/'

# Описания готовые к классификации
DATA_PATH = DATA_DIR + 'opisaniya_zaderzhaniy_to_classify.csv'

# Файл с леммами
LEMMAS_PATH = DATA_DIR + 'lemmas.txt'

# Файл с подбором ключевых слов
KeywordsDict_PATH = DATA_DIR + 'zaderzhaniya_KeywordsDict.csv'


MYSTEM_CONF = pymystem3.Mystem(entire_input=False, disambiguation=True)

# TODO: Опечатки - регулярные и не очень - что с ними делать?
# TODO: Снятие омонимии не то чтобы очень сильно нужно на самом деле

CATEGORIES_ENG = {'несовершеннолетний': 'underage',

                  'медицина': 'medicine',

                  'телефон': 'phone_force',

                  'паспорт': 'passport_force',

                  'еда': 'food',

                  'автозак время': 'car_time',

                  'время задержания': 'detain_time',

                  'досмотр без понятых': 'frisk',

                  'пальчики': 'fingers',

                  'протокол': 'protocol',

                  'давление': 'pressure',

                  'недопуск адвоката': 'lawyer_obstruct',

                  'избиение': 'beating',

                  'задержания журналистов': 'journalist_detain',

                  'условия задержания': 'detain_conditions'}



