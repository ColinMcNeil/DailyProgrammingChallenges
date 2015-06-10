__author__ = 'Colin'
__name__='Daily Programs for June'
import easygui as gui

def June(day):
    if day == '8':
        J8()

def J8():
    #Make any number into a palendrome.
    #URL: http://www.reddit.com/r/dailyprogrammer/comments/38yy9s/20150608_challenge_218_easy_making_numbers/
    number=gui.enterbox(title=__name__,msg='Input a number and I will make it a palindrome')
    invnumber=int(number[::-1])
    number=int(number)
    i=1
    while True:
        number=invnumber+number
        invnumber=int(str(number)[::-1])
        if invnumber==number:
            gui.textbox(title='Output',text=('It took '+str(i)+' iterations. Final #: '+number))
            break
        i=i+1