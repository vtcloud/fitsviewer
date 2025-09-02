"""
fitsviewer execution script.
"""

__date__ = '09/02/2025'
__updated__ = '20250902'
__version__ = '0.1'
__author__ = 'V. Tolls, CfA | Harvard & Smithsonian'

from .fitsviewer import fitsviewer
import argparse
import textwrap
import importlib


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


tpipe = 'fitsviewer'



def execfv():
    parser = argparse.ArgumentParser(
        prog=tpipe,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            fitviewer
            -----------------------
                I have indented it
                exactly the way
                I want it
            '''))
    parser.add_argument('--File', '-f', nargs='?', type=str,
                        help=f'{tpipe} input file.')
    args = parser.parse_args()

    fitsviewer(args=args)
