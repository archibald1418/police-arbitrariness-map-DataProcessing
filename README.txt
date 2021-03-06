Скрипты берут данные с задержаниями по отделам полиции и классифицируют по категориям.
Классификация построена на пересечениях лемм из описаний и подготовленных ключевых слов.

Данные - ручные описания задержаний в отделах полиции в формате:
(id, овд, метка задержания, описание задержания)

Данные из разных источников, поэтому они предварительно собраны в одной таблице.
Отильтрованы по непустым значениям в колонке "овд"

Приведены к общим категориям задержаний на основе ручного просмотра.
Итоговые категории:

underage          - недопуск родителей/опекунов в отдел полиции к несовершеннолетнему задержанному
medicine          - необеспечение неотложной или любой другой медицинской помощи (напр., недача лекарств)
phone_force       - насильный отъем телефонов или требование их разблокировать
passport_force    - насильный отъем паспорта
food              - недача еды после 3 часов задержания
car_time          - долго держат задержанного в автозаке
detain_time       - долго держат в отделе (больше 3 часов)
frisk             - обыск без понятых
fingers           - насильная дактилоскопия по неуголовному делу
protocol          - нарушение при оформлении протокола
pressure          - психологическое давление
lawyer_obstruct   - недопуск адвоката в отдел
beating           - избиение, причинение травм
journalist_detain - задержание журналиста при исполнении профессиональных обязанностей
detain_conditions - нарушения условий задержания (нет маста, негде спать, негде сидеть, холодно и т.д.)

Ключевые слова отобраны по осмотру частотных списков получившихся лемм и леммовых биграмм.

Результаты анализа представлены в виде матрицы (описание: категории) со значениями 0 (нет такого нарушения) и 1 (есть).
Затем группируются по овд и районам Москвы и суммируются. 

Результаты суммирования выпадают при наведении на район Москвы или ОВД 
на сайте https://ivan-hilckov.github.io/police-arbitrariness-map/

К сожалению, пока нет возможности привести данные, так как имеется чувствительная и личная информация.

Скрипт пока не работает на любых данных, но над этим ведется усиленная работа.

Также ведется работа над улучшением классификации, привлечением более адекватной модели и большего количеству данных

