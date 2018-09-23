#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 __         _           _         __
( '\___      \_  (^)  _/      ___/' )
 \ , ' \____   \ / \ /   ____/ ' , /
  \__ ' , ' \___{~V~}___/ ' , ' __/
 ____\_________ {<!>} _________/____
/ , ' , ' , ' ,`{<!>}~, ' , ' , ' , \
\_____________ /{<!>}\______________/
                 \./
                 (~)
                 (~)
                 (~)
                 (~)
                 (~)
                 (~)
                 ,0,
                  "
 * Author: Ibrar Yunus
 * <University of St. Andrews>
 * <Queries:      yunus.ibrar@gmai.com>
 * United Kingdom
 * ------------------------------------
 * Setup Details:
 * ---------- Lenovo Y700 Gaming Laptop
 * ------------------------- Windows 10
 * ------------------------- Python 3.6
 * --------------------- PyCharm 2017.3
 * --------- Interfaced with VLC Player
"""

import os

graphic = [ '\033[1;96;49m ',
'------___-----------___-------___-----------___-----',
'-----/\--\---------/\__\-----/\--\---------/\__\----',
'----/::\--\-------/:/--/----/::\--\-------/:/-_/_---',
'---/:/\:\--\-----/:/--/----/:/\:\--\-----/:/-/\__\--',
'--/::\~\:\--\---/:/--/----/:/--\:\--\---/:/-/:/-_/_-',
'-/:/\:\-\:\__\-/:/__/----/:/__/-\:\__\-/:/_/:/-/\__\\',
'-\/__\:\-\/__/-\:\--\----\:\--\-/:/--/-\:\/:/-/:/--/',
'------\:\__\----\:\--\----\:\--/:/--/---\::/_/:/--/-',
'-------\/__/-----\:\--\----\:\/:/--/-----\:\/:/--/--',
'------------------\:\__\----\::/--/-------\::/--/---',
'-------------------\/__/-----\/__/---------\/__/----'
]


def display_header():
    width = os.get_terminal_size().columns
    for x in graphic:
        x = x.replace('-', ' ')
        print(x.center(width), end = '')
    print("\n")
    print("created by Ibrar Yunus".center(width))
    print("\n")
