# Detects the encoding of a given file and changes the encoding to utf-8 without BOM
# Note that the program replaces the file given as the input with the one encoded with utf-8.
# If the input file is encoded with utf-8 without BOM, the program does nothing
#
# usage:
# python any2utf8.py file.txt
# -> If the encoding of file.txt is SHIFT_JIS, the program replaces the file with the one encoded with utf-8.

import sys
import codecs
import unicodedata

# Please run 'pip install chardet' if you haven't already.
import chardet


# def detect_encoding_test():
#     with codecs.open("sjis_testfile", mode="w", encoding='SHIFT_JIS') as testfile:
#         text = 'characters unique to sjis'
#         #print(text)
#         testfile.write(text)
#
#     enc = detect_encoding('sjis_testfile')
#     print(enc)
#     myassert(enc,"SHIFT_JIS")


def detect_encoding(file_pathname):
    with open(file_pathname, mode='rb') as file:
        read_bytes = file.read()
        det = chardet.detect(read_bytes)
        # print(det)
        return det['encoding']

def convert_encoding_and_replace_file(file_pathname,src_encoding,dest_encoding):
    src_string = ''
    with codecs.open(file_pathname, mode='r', encoding=src_encoding) as file:
        src_string = file.read()

    with codecs.open(file_pathname, mode='w', encoding=dest_encoding) as output_file:
        output_file.write(src_string)

def convert_to_utf8(pathname):

    enc = detect_encoding(pathname)

    print(enc)

    target_encoding = 'utf-8'

    if( enc == target_encoding ):
        print('The specified file is encoded with ' + target_encoding + '. Conversion is not necessary.')
        return

    convert_encoding_and_replace_file(pathname,enc,'utf-8')

def normalize_nfkc(utf8_file_pathname):

    text = ''
    with codecs.open(utf8_file_pathname, mode='r', encoding='utf-8') as file:
        text = file.read()
        text = unicodedata.normalize('NFKC',text)

    with codecs.open(utf8_file_pathname, mode='w', encoding='utf-8') as output_file:
        output_file.write(text)

def run():

    if( len(sys.argv) < 2 ):
        return # a file pathname needs to be specified.

    pathname = sys.argv[1]

    convert_to_utf8(pathname)

    if 3 <= len(sys.argv) and sys.argv[2] == '--nfkc':
        normalize_nfkc(pathname)


# detect_encoding_test()
run()
