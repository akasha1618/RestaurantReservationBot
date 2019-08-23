    
""" main function of numero calculation of matrix by python """
import datetime
from addDigit.AddDigits import AddDigits
from telnetlib import Telnet
import sys


# --- main def ---
def main(argv):
    calc_date = datetime.datetime.now()
    add_digs = AddDigits()
    add_digs.calc_digits(calc_date)
    print(" calculated date:", calc_date.date())
    print("dd-mm-yyyy:", calc_date.day, calc_date.month, calc_date.year)
    print("ADs:")
    print(add_digs.AD_01.value, add_digs.AD_02.value)
    print(add_digs.AD_03.value, add_digs.AD_04.value)


    pass
# --- main def ---

# --- Call of Main function ---
if __name__ == '__main__':
    main(sys.argv)