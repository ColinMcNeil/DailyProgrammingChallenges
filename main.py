__name__='Daily Program'
__author__ = 'Colin'

import easygui as gui
import June

#Debug Line 1 to skip menus, 0 for normal
debug=0

if debug==1:
    #Put in specific day to skip menu to in format: Month.DayCode()
    June.J8()

if debug ==0:
    #Menu using easygui to select the day you want to run
    year=gui.choicebox('Pick Year',__name__,['2015'])
    month='Not Defined'
    day='Not Defined'
    if year == '2015':
        month=gui.choicebox('Pick Month',__name__,['June'])
        day=gui.choicebox('Pick Day',__name__,['8'])

    if month=='June':
        June.June(day)