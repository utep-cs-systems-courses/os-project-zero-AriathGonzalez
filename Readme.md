This repository contains the code for the python introduction lab. The
purpose is to have a fairly simple python assignment that introduces
the basic features and tools of python

In the repository are two plain text files with lots of words. Your
assignment is to create a python 3 program which:
* takes as input the name of an input file and output file
* example

`$ python wordCount.py input.txt output.txt`
* keeps track of the total the number of times each word occurs in the text file 
* excluding white space and punctuation
* is case-insensitive
* print out to the output file (overwriting if it exists) the list of
  words sorted in descending order with their respective totals
  separated by a space, one word per line

To test your program we provide wordCountTest.py and two key
files. This test program takes your output file and notes any
differences with the key file. An example use is:

`$ python wordCountTest.py declaration.txt myOutput.txt declarationKey.txt`

The re regular expression library and python dictionaries should be
used in your program. 

Note that there are two major dialects of Python.  Python 3.* is
incompatible with 2*.  As a result, Python 2.7 remains popular.  All
of our examples were ported to 3.* during the summer of 2018.  We (mildly)
encourage students to use that dialect of Python.
