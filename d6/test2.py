import re,sys
year = sys.argv[1]

reg_expr = re.compile("(19|20)\d\d-(0[1-9]|1[12])-(0[1-9]|[12][0-9]|3[01])")

match = reg_expr.match(year)

if match == None:
    print("Fel format, ange på formen YYYY-MM-DD")


