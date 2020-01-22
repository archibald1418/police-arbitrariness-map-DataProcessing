#!/usr/bin/env python3

if __name__ == "__main__":

    import argparse

    import constants
    import main

    parser = argparse.ArgumentParser(description=
                                     '''OVD INFOSHECHKA/n
    This executes main.py and saves .json for future use''')

    parser.add_argument("output",
                        default="output.json",
                        help="the name of the json-file where the output will be written")
    args = parser.parse_args()
    print(f"Argument parsed successfully.\noutput={args.output}")



    # Execute python -m
    print('Processing data...\n')
    data_path = constants.DATA_PATH
    main.main(data_path)
    print('Data processed!\n')

    print('Making a json...\n')

    target_path = parser.get_default('output') if args.output == 'output' else args.output
    with open(target_path, 'w') as write_file:
        # TODO: Actually it copies the file...

        source = open('data/ovd_offence_report.json', 'r')
        contents = source.read()
        source.close()

        write_file.write(contents)

    print(f'You can pick your json file at {target_path}')



### Мануал: команднeую строку запусти, файлик забери
