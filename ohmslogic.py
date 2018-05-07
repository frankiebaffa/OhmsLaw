import math

sq = math.sqrt

def voltagePower(volts, watts):
    amps = watts / volts
    ohms = (volts ** 2) / watts
    print(result(volts, watts, ohms, amps))

def voltageResistance(volts, ohms):
    amps = volts/ohms
    watts = (volts ** 2) / ohms
    print(result(volts, watts, ohms, amps))

def voltageAmps(volts, amps):
    ohms = volts / amps
    watts = volts * amps
    print(result(volts, watts, ohms, amps))

def powerResistance(watts, ohms):
    amps = sq(watts / ohms)
    volts = sq(watts * ohms)
    print(result(volts, watts, ohms, amps))

def powerCurrent(watts, amps):
    ohms = watts / (amps ** 2)
    volts = watts / amps
    print(result(volts, watts, ohms, amps))

def resistanceCurrent(ohms, amps):
    volts = amps * ohms
    watts = (amps ** 2) * ohms
    print(result(volts, watts, ohms, amps))

def result(volts, watts, ohms, amps):
    print('')
    return "Volts: {}, Watts: {}, Ohms: {}, Amps: {}".format(
        round(volts, 2), round(watts, 2), round(ohms, 2), round(amps, 2))
