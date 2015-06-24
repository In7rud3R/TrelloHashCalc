#HashCalc by In7rud3R
#Calculate Trello string form hash ;) https://trello.com/jobs/developer
#Usage : python HashCalc.py -c <hash>
 
LETTERS = 'acdegilmnoprstuw'
FIRST_LETTER = LETTERS[0]
 
import argparse
 
def compute_hash(string):
 
    h = 7
    for char in string:
        h = h * 37 + LETTERS.index(char)
    return h
 
def compute_string(hash):
 
    hash = int(hash)
 
    hash_length = len(str(hash))
    string_length = 0
    while True:
        current_string = FIRST_LETTER * (string_length + 1)
        current_hash = compute_hash(current_string)
        if len(str(current_hash)) > hash_length:
            break
        string_length += 1
 
    chars = []
    for i in range(string_length):
        previous_char = None
        for char in LETTERS:
            current_string = ''.join(chars) + char + FIRST_LETTER * (string_length - i - 1)
            current_hash = compute_hash(current_string)
            if current_hash == hash:
                return current_string
            elif current_hash > hash:
                chars.append(previous_char or FIRST_LETTER)
                break
            else:
                previous_char = char
    raise ValueError('Cannot find string for hash {hash:d}'.format(hash=hash))
 
parser = argparse.ArgumentParser(usage='Write something here')
parser.add_argument('-c', '--calc', action='store', help='Write something here')
args = parser.parse_args()
if args.calc:
    print compute_string(args.calc)
 
else:
    parser.print_help()
