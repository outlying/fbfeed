#!/usr/bin/env python3
import getopt, sys

argumentList = sys.argv[1:]

unixOptions = "p:"
gnuOptions = ["page="]

try:
    arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))
    sys.exit(2)

page = None

for currentArgument, currentValue in arguments:
    if currentArgument in ("-p", "--page"):
        page = currentValue

if page is None:
	raise Exception('Missing -p --page parameter')


