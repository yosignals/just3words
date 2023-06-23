import os
import sys
import itertools
import gzip

# specify the name of the dictionary file
filename = 'dictionary.txt'
output_filename = 'combinations.gz'

# check if the dictionary file exists
if not os.path.isfile(filename):
    print(f'Dictionary file not found: {filename}', file=sys.stderr)
else:
    # read all words into a list
    try:
        with open(filename, 'r') as f:
            words = [word.strip() for word in f]
    except Exception as e:
        print(f'Error reading dictionary file: {e}', file=sys.stderr)
        words = []

    # create all combinations of three words
    try:
        with gzip.open(output_filename, 'wt') as f:
            for combination in itertools.combinations(words, 3):
                f.write(''.join(combination) + '\n')
    except Exception as e:
        print(f'Error generating combinations: {e}', file=sys.stderr)
