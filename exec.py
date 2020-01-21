#!/usr/bin/env python3

import argparse
import json

import constants

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OVD INFOSHECHKA")
    parser.add_argument("datafile",
                        help="the name of the file containing the data",
                        default=constants.DATA_PATH)
    parser.add_argument("-o", "--output", default="output.json", help="the name of the file where the output will be written")
    args = parser.parse_args()
    print(f"Arguments parsed successfully.\ndatafile={args.datafile}\noutput={args.output}")



    # Execute python -m
    import __main__
    print('Processing data...\n')
    data_path = args.datafile
    __main__.main(data_path)
    print('Data processed!\n')

    print('Making a json...\n')

    with open('output.json', 'w') as write_file:
        source = open('data/ovd_offence_report.json', 'r')
        contents = source.read()
        source.close()

        json.dump(contents, write_file, indent=4)

    print(f'You can pick your json file at {args.output}')



### Мануал: команднeую строку запусти, файлик забери
