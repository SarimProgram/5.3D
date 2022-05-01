from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
import time

                     
      
betweenCharTime = 30.0 / 100    
inputString = ""

converted = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.",".":".-.-.-",",":"--..--",":":"---...","?":"..--..","'":".----.","-":"-....-","/":"-..-.","(":"-.--.-",")":"-.--.-","\"":".-..-.","@":".--.-.","=":"-...-","[":"-.--.-","]":"-.--.-","$":"...-..-","+":".-.-.",";":"-.-.-.","_":"..--.-","!":"---."}



led = LED(14)





root = Tk()
root.title("Text to LED Morse Code")
myFont = tkinter.font.Font(family = 'Helvetica' , size = 12, weight = "bold")


def Dash():
    led.on()
    time.sleep(0.05)
    led.off()


def Dot():
    led.on()
    time.sleep(0.03)
    led.off()


def space():
    time.sleep(0.07)

entry_1 = Entry(root)
entry_1.grid(row = 0, column = 1)




def ledToggle():
    inputString = entry_1.get().lower()
    if len(inputString) >= 12:
            print("To many Charaters")
            return 

    for c in inputString:
       
        if c == " ":
            space()
       
        elif c in converted:
            
            morseconverted = converted[c]
            
            for symbol in morseconverted:
                
                if symbol == "-":
                    Dash()
                    time.sleep(0.07)
                
                elif symbol == ".":
                    Dot()
                    time.sleep(0.07)
               
                else:
                    print ("Not a '-' or '.'")
            time.sleep(betweenCharTime)
        
        else:
            print ("'" + c + "'" + " is not a supported character")
   
    inputString = entry_1.get().lower()

def close():
    RPi.GPIO.cleanup()
    root.destroy()
                     


    
    
ledRedButton = Button(root, text = 'Start Conversion', font = myFont,command = ledToggle, bg = 'white' , height = 10, width = 54)
ledRedButton.grid(row = 2, column = 1)




exitButton = Button(root , text = 'Exit' , font = myFont , command = close, bg = 'white' , height = 10 , width = 50)
exitButton.grid(row = 4, column = 1)


root.protocol("WM_DELETE_WINDOW" , close)

root.mainloop()
