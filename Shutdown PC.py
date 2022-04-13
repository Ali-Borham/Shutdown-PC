### Shutdown PC Programme ###
# auto-py-to-exe

import os
from threading import Timer 

# os.system("shutdown /s /t 1")

print ("                  ****************************            ")
print ("                  ****************************            ")
print ("     <<<<<< Welcome to (Ali Borham's Shutdown PC App.) >>>>>>"    )
print (" ")
print ("<<< You can Shutdown your PC after any time you want >>>")
print (" ")
print ("                  ****************************            ")
print ("                  ****************************            ")
print (" ")


# time_minutes= float (input ("After how many 'minutes' do you want to shutdown your PC? =>> "))

# def shutdown():
#     os.system("shutdown /s /t 1")

# The_timer= Timer (time_minutes * 60 , shutdown)
# The_timer.start()

#############################################################################################################

while True:
    try:
        time_minutes= float (input ("After how many 'minutes' do you want to shutdown your PC? =>> "))
        def shutdown():
            os.system("shutdown /s /t 1")
        The_timer= Timer (time_minutes * 60 , shutdown)
        The_timer.start() 
        break
    except:
        print("!!!!!")
        print("Please type a minute.")
        print("-------------------------------")
    
#############################################################################################################

