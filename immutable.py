my_string="Hello"
try:
    my_string[7]='W'
except TypeError as e:
    print (e)