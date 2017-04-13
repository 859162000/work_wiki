#! $PATH/python

# file name: yihuo.py
# author: lianghy
# time: 2017-3-21 13:13:39

"""Simple encrypt/decrypt program."""

from optparse import OptionParser

usage = """Usage: %prog -i filename -o filename -a en|de -w word [args]"""

parser = OptionParser(usage)
parser.add_option('-i', '--file_input', dest='input_filename', 
        help='read data from file')
parser.add_option('-o', '--file_output', dest='output_filename', 
        help='store data to file')
parser.add_option('-a', '--action', dest='action', help='encrpyt or decrypt')
parser.add_option('-w', '--word', dest='password', help='password')

(options, args) = parser.parse_args()

defualt_password = "random1do8atal0skdf"

def pencrypt():
    """ 1. bitlise the password
        2. make the same length of binary_password and the line
        3. xor compute"""
    if options.password is not None:
        binary_password = options.password.encode('utf-8')
        password_length = len(binary_password)
    else:
        binary_password = defualt_password.encode('utf-8')
        password_length = len(binary_password)
    with open(options.input_filename, 'r', encoding='utf-8') as fin, open(
            options.output_filename, 'wb') as fout:
        new_str = bytes()
        line_bytes = fin.read().encode('utf-8')
        for index, one_byte in enumerate(line_bytes):
            new_str += bytes([one_byte^binary_password[index%password_length]])
        fout.write(new_str)

def pdecrypt():
    """ 1. bitlise the password
        2. make the same length of binary_password and the line
        3. xor compute"""
    if options.password is not None:
        binary_password = options.password.encode('utf-8')
        password_length = len(binary_password)
    else:
        binary_password = defualt_password.encode('utf-8')
        password_length = len(binary_password)
    with open(options.input_filename, 'rb') as fin, open(
            options.output_filename, 'w', encoding='utf-8') as fout:
        all_str = fin.read()
        new_str = bytes()
        for index, one_byte in enumerate(all_str):
            new_str += bytes([one_byte^binary_password[index%password_length]])
        newline = new_str.decode('utf-8')
        fout.write(newline)

#if all([options.input_filename, options.output_filename, options.action, 
#    options.password]):
if options.action == 'en':
    pencrypt()
elif options.action == 'de':
    pdecrypt()
else:
    print("Error in parameters")
    print(usage)

if __name__ == "__main__":
    print("yihuo.py")
