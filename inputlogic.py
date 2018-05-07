import importlib
importlib.import_module('sint')
from sint import ignore_exception

sint = ignore_exception(ValueError)(float)

def inputs(inputString, lawInput, varcount):
    lawInput = sint(input(inputString))
    if lawInput == None:
        lawInput = ''
        return {'law':lawInput, 'count':varcount}

    if lawInput != '':
        varcount += 1
        return {'law':lawInput, 'count': varcount }
