__author__ = 'Colin'
import easygui as gui
import June

#Debug Line
debug=1
June.J8()

if debug ==0:
    __name__='Daily Program'
    year=gui.choicebox('Pick Year',__name__,['2015'])
    month='Not Defined'
    day='Not Defined'
    if year == '2015':
        month=gui.choicebox('Pick Month',__name__,['June'])
        day=gui.choicebox('Pick Day',__name__,['8'])

    if month=='June':
        June.June(day)
