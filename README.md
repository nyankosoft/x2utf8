# x2utf8
Converts the input file encoding to UTF-8 and replaces the file.

# Usage
python x2utf8.py myfile.txt


## Core Principles

1. The program shall convert the encoding of a given file to UTF-8 without BOM.
2. User shall not have to specify the encoding of the input file.
3. The program shall replace the input file with the new converted UTF-8 file, i.e. the original file will be gone.
4. If the input file turn out to be utf-8 encoded, the program shall back off and shall exit without doing anything to the file.

## Background

For the last several years I have been plagued by Shift JIS just way too much, and enough is enough already.
I need a way to convert any given text files to UTF-8 fast and easy.

iconv does the job but you have to specify the encoding of the input file, i.e. it does not automatically/intelligently back off should the input file turn out to be encoded with UTF-8.




