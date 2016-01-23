import pygame
import serial
pygame.init()
j = pygame.joystick.Joystick(0)#j is the alias of joystick
pygame.joystick.init()
ser=serial.Serial('COM5',9600)#COM5 is the connection port to arduino
import time
j.init()#initiallizing joystick
temp_string=[]

while(True):
    for event in pygame.event.get(): # Pygame is retarded it needs events
        pass
    
    vertical_axis=j.get_axis(1)#vertical_axis input
    horizontal_axis=j.get_axis(0)# horizontal_axis input
    lever=-(j.get_axis(2)-1)/2 #the shiftable joystick in the bottom "+" and "-" to control the speed, scaled to the desired high to low position
    
    if(vertical_axis*100<0):#when the vertical axis is pushed up
        forward_backward=93+vertical_axis*63*lever
        forward_backward=int(forward_backward)
     
    if(vertical_axis*100>0):#when the vertical axis is pushed down
        forward_backward=93+vertical_axis*57*lever
        forward_backward=int(forward_backward)
       
    if(horizontal_axis*100<0):#when pushed left
        left_right=93+horizontal_axis*63*lever
        left_right=int(left_right)
    
    if(horizontal_axis*100>0):#when pushed right
        left_right=93+horizontal_axis*67*lever
        left_right=int(left_right)
       
    if(vertical_axis*100==0):
        forward_backward=93 #rest values- no motion
    if(horizontal_axis*100==0):
        left_right=93 #rest values- no motion

    #in the blow below the numbers e.g 9 is made to 009 and 99 is made to 099 so there is constant array of 7 characters
    if(forward_backward<=9):
        temp_string="0"+"0"+str(forward_backward)
        forward_backward=''.join(temp_string)
    if(forward_backward<=99):
        temp_string="0"+str(forward_backward)
        forward_backward=''.join(temp_string)
    if(left_right<=9):
        temp_string="0"+"0"+str(left_right)
        left_right=''.join(temp_string)
    if(left_right<=99):
        temp_string="0"+str(left_right)
        left_right=''.join(temp_string)
    #the block ends here
    
    array = []
    array.append(str(forward_backward))#forward backward signal
    array.append('a')#a is the signal separator
    array.append(str(left_right))#angle of turning signal i.e. left right
    final_signal = ''.join(array)#make the array in to a single string
    
    print("Horizontal axis: "+str(left_right))
    print("Vertical axis: "+str(forward_backward))
    print("Speed Control: "+str(lever*100))
    print("Sent Signal: "+str(final_signal))
    
    ser.write(final_signal)#final signal is in the form "120a090","093a050" etc
    time.sleep(0.9) #due to unknown reasons for now arduino doesn't process the signal if its less than 0.9 seconds changing this will change speed of signal transmission
    
        
