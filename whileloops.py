import importlib
importlib.import_module('inputlogic')
importlib.import_module('ohmslogic')
from inputlogic import inputs
from ohmslogic import *


def whileOne():
    volts, watts, ohms, amps = '', '', '', ''
    varcount = 0
    while varcount < 2:
        inputString = "What is the voltage? (in Volts)"
        if volts == '':
            output = inputs(inputString, volts, varcount)
            volts, varcount = output['law'], output['count']
        if varcount == 2:
            break

        inputString = "What is the power? (in Watts)"
        if watts == '':
            output = inputs(inputString, volts, varcount)
            watts, varcount = output['law'], output['count']
        if varcount == 2:
            break

        inputString = "What is the resistence? (in Ohms)"
        if ohms == '':
            output = inputs(inputString, volts, varcount)
            ohms, varcount = output['law'], output['count']
        if varcount == 2:
            break

        inputString = "What is the current? (in Amps)"
        if amps == '':
            output = inputs(inputString, volts, varcount)
            amps, varcount = output['law'], output['count']
        if varcount == 2:
            break
    whileTwo(volts, watts, ohms, amps)

def whileTwo(volts, watts, ohms, amps):
    while volts == '' or watts == '' or ohms == '' or amps == '':
        if volts != '' and watts != '':
            voltagePower(volts, watts)
            break

        if volts != '' and ohms != '':
            voltageResistance(volts, ohms)
            break

        if volts != '' and amps != '':
            voltageAmps(volts, amps)
            break

        if watts != '' and ohms != '':
            powerResistance(watts, ohms)
            break

        if watts != '' and amps != '':
            powerCurrent(watts, amps)
            break

        if ohms != '' and amps != '':
            resistanceCurrent(ohms, amps)
            break
