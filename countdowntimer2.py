#importing time module 
import time
#defining the countdown function
def countdowntimer(t):
    while t:
        minutes,seconds=divmod(t,60)
        timer='{:02d}:{:02d}'.format(minutes,seconds)
        print (timer,end="\n")
        time.sleep(1)
        t -= 1

    print('\nTIMES UP!!!')

t=input("Enter the time in seconds:")
countdowntimer(int(t))
