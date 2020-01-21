import constants


def write_lemmas_to_file(lemmas_freqdist, path=constants.LEMMAS_PATH):
    '''

    Write lemmas and their frequencies to csv file for further analysis.
    Sort from most to least occurences
    '''

    newfile = open(path, 'w')

    # Sorting keys
    by_alpha_asc = lambda x: (x[0], -x[1])
    by_freq_desc = lambda x: (-x[1], x[0])
    by_freq_asc = lambda x: (x[1], x[0])

    frmt = '{}\t{}\n'
    for lemma, freq in sorted(lemmas_freqdist.items(), key=by_freq_desc):

        line = frmt.format(lemma, freq)
        newfile.write(line)


    newfile.close()
