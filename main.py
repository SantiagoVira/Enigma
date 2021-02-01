#importing modules
import pygame
from string import ascii_lowercase as lowercase, whitespace
from time import sleep as delay

#preparing the pygame screen
pygame.init()
screen=pygame.display.set_mode((800, 500))

#Declaring Global variables
run=True
PlugScreen=False
pressed=None
MouseData=[False]
CanClick=True
final=None

#Making an alphabet list for the logic of the encoding
alphabet=list(lowercase)

#Making lists to help organize the Plugboard
keyboard=[['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],[ 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],['z', 'x', 'c', 'v', 'b', 'n', 'm']]
keyletters=[item for sublist in keyboard for item in sublist]
PlugPositions={
    1:[(-50, 0),(-50, 0)],
    2:[(-50, 0),(-50, 0)],
    3:[(-50, 0),(-50, 0)],
    4:[(-50, 0),(-50, 0)],
    5:[(-50, 0),(-50, 0)],
    6:[(-50, 0),(-50, 0)],
    7:[(-50, 0),(-50, 0)],
    8:[(-50, 0),(-50, 0)],
    9:[(-50, 0),(-50, 0)],
    10:[(-50, 0),(-50, 0)],
    }
Plugs={}

#Declaring variables to style Pygame
black=(0,0,0)
white=(255, 255, 255)
gray=(125, 125, 125)
gold=(255, 194, 64)
DarkGray=(30, 30, 30)
font = pygame.font.Font('freesansbold.ttf', 32)
Rotorfont=pygame.font.Font('freesansbold.ttf', 20)

#Rotor old logic
##Rotor1=['p', 'e', 'z', 'u', 'o', 'h', 'x', 's', 'c', 'v', 'f', 'm', 't', 'b', 'g', 'l', 'r', 'i', 'n', 'q', 'j', 'w', 'a', 'y', 'd', 'k']
##Rotor2=['z', 'o', 'u', 'e', 's', 'y', 'd', 'k', 'f', 'w', 'p', 'c', 'i', 'q', 'x', 'h', 'm', 'v', 'b', 'l', 'g', 'n', 'j', 'r', 'a', 't']
##Rotor3=['e', 'h', 'r', 'v', 'x', 'g', 'a', 'o', 'b', 'q', 'u', 's', 'i', 'm', 'z', 'f', 'l', 'y', 'n', 'w', 'k', 't', 'p', 'd', 'j', 'c']
##Rotor4=['i', 'm', 'e', 't', 'c', 'g', 'f', 'r', 'a', 'y', 's', 'q', 'b', 'z', 'x', 'w', 'l', 'h', 'k', 'd', 'v', 'u', 'p', 'o', 'j', 'n']
##Rotor5=['q', 'w', 'e', 'r', 't', 'z', 'u', 'i', 'o', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'p', 'y', 'x', 'c', 'v', 'b', 'n', 'm', 'l']
##All=[Rotor1,Rotor2,Rotor3,Rotor4,Rotor5]
##
##Rotors=[Rotor1, Rotor2, Rotor3]
##RotorAlphabets=[]
##for i in range(5):
##    a=alphabet
##    RotorAlphabets.append(a)
##RotorNames=[1, 2, 3]
##Usable=[Rotor4, Rotor5]
##UsableNames=[4,5]
##Rotations=0

#Rotor working logic variables
rotors=[0, 0, 0]
reflector = [leter for leter in reversed(alphabet)]

#Rotor working logic functions
def permutate(rotor):
    new_alphabet = ''.join(alphabet)
    new_alphabet = list(new_alphabet)
    for iter in range(rotor):
        new_alphabet.insert(0, new_alphabet[-1])
        new_alphabet.pop(-1)
    return new_alphabet
def inverse_permutation(rotor):
    new_alphabet = ''.join(alphabet)
    new_alphabet = list(new_alphabet)
    for iter in range(rotor):
        new_alphabet.append(new_alphabet[0])
        new_alphabet.pop(0)
    return new_alphabet

#Main loop
while run:

    ########################### Main Screen #######################################################
    if not PlugScreen:

        #Check for events
        for event in pygame.event.get():
            
            #If the window is closed, quit the program
            if event.type==pygame.QUIT:
                run=False

            if event.type==pygame.KEYDOWN:
                pressed=event.unicode.lower()

            if event.type==pygame.KEYUP:
                final=None
                pressed=None
                # turning the rotors
                rotors[0] += 1
                if rotors[0] % len(alphabet) == 0:
                    rotors[1] += 1
                    rotors[0] = 0
                if rotors[1] % len(alphabet) == 0 and rotors[0] % len(alphabet) != 0 and rotors[1] >= len(alphabet) - 1:
                    rotors[2] += 1
                    rotors[1] = 1
            #if the mouse is clicked
            if event.type==pygame.MOUSEBUTTONDOWN:

                #Check if it is asking to go to the plugscreen
                if event.pos[1]>400:
                    PlugScreen=True
                MouseData=[True, event.pos]
                
            #if the mouse isn't being clicked, allow the user to click again
            #this CanClick variable tells the program that the user only clicked once, so it doesn't register one click as a bunch
            else:
                MouseData=[False]
                CanClick=True

##        #Get the presed keys
##        keys=list(pygame.key.get_pressed())
##
##        #If a key is being pressed
##        if 1 in keys:
##            
##            #And it is a letter key
##            if alphabet[keys.index(1)-4]:
##                
##                #Set the pressed variable equal to the letter of that key
##                pressed=alphabet[(keys.index(1))-4]

        #Fill in background
        screen.fill(black)

        #Draw the background of the rotors
        for i in range(2,5):
            pygame.draw.rect(screen, gray, (100*i, 40, 25, 90))

        pygame.draw.line(screen, black, (0, 70), (550, 70), 2)
        pygame.draw.line(screen, black, (0, 100), (550, 100), 2)


        #Draw the current, previous, and next letter on each rotor
        RotorPos=[210, 310, 412]
        for i, Rotor in enumerate(rotors):
            if Rotor>23:
                Shown=alphabet.copy()[Rotor:]+alphabet.copy()[:len(alphabet)-Rotor+1]
            else:    
                Shown=alphabet.copy()[Rotor:Rotor+3]
            for place, showing in enumerate(Shown):
                Ltext = Rotorfont.render(showing.upper(), True, DarkGray)  
                LtextRect = Ltext.get_rect()  
                LtextRect.center = (RotorPos[i], 55+place*30)
                screen.blit(Ltext, LtextRect)

#--------------------------------------------------------------------------------
        #if a letter is being pressed
        if pressed:
            #Check if it is in the Steckerbrett, and replace it if it is
            if pressed in Plugs:
                    # If it is, the we encrypt it as it's pair
                    final=Plugs[pressed]

            else:
                    
                # Encrypting through rotors
                temp_letter = permutate(rotors[0])[alphabet.index(pressed)]
                temp_letter = permutate(rotors[1])[alphabet.index(temp_letter)]
                temp_letter = permutate(rotors[2])[alphabet.index(temp_letter)]
                temp_letter = reflector[alphabet.index(temp_letter)]
                temp_letter = inverse_permutation(rotors[2])[alphabet.index(temp_letter)]
                temp_letter = inverse_permutation(rotors[1])[alphabet.index(temp_letter)]
                temp_letter = inverse_permutation(rotors[0])[alphabet.index(temp_letter)]
                final=temp_letter

#--------------------------------------------------------------------------------

        #Draw the keyboard and make the final letter result glow
        for rowV, row in enumerate(keyboard):       
            for lettV, letter in enumerate(row):
                delay(0.001)
                if letter==final:
                    color=gold
                else:
                    color=gray
                    
                x=lettV*75+50+10*(3**rowV)
                y=rowV*75+200
                
                pygame.draw.circle(screen, color, (x, y), 30)
                
                
                Ltext = font.render(letter.upper(), True, DarkGray)  
                LtextRect = Ltext.get_rect()  
                LtextRect.center = (x-1, y)
                screen.blit(Ltext, LtextRect)


        #make an area to detect if the rotor is being clicked on              
        changers=[pygame.Rect(100*(i-int(i/3)*3)+200, int(i/3)*62+40, 25, 30) for i in range(6)]
        
        #Swap Rotors out
        #--------------------------Not possible in new layout-------------------
##        swappers=[]
##        for i in range(3):
##            #make areas to detect if the rotor is being swapped
##            x, y=i*100+212, 20
##            changer=pygame.Rect(0,0, 25, 30)
##            changer.center=(x,y)
##            swappers.append(changer)
##
##            #Draw the rotor numbers above each rotor
##            Rtext = Rotorfont.render(str(RotorNames[i]), True, white)  
##            RtextRect = Rtext.get_rect()  
##            RtextRect.center = (210+i*100,20)
##            screen.blit(Rtext, RtextRect)
        #--------------------------Not possible in new layout-------------------

        #if the user clicked
        if MouseData[0] and CanClick:

            #limit it to detect only one click
            pos=MouseData[1]
            CanClick=False

            #For each change-the-rotor-position area
            for val, rect in enumerate(changers):

                #Check if the mouse is clicking the area
                if rect.collidepoint(pos):

                    #Get the direction (up or down) based on the position of the rectangle
                    #And get the rotor being changed
                    Di=int((rect.y-40)/40)
                    index=int((rect.x-200)/100)

                    #move the rotor down
                    if Di==1:
                        rotors[index]= (rotors[index]-1) % len(alphabet)
                    #move the rotor up
                    else:
                        rotors[index]= (rotors[index]+1) % len(alphabet)


            #For each swap-the-rotor-in-use area
            #--------------------------Not possible in new layout-------------------
##            for val, rect in enumerate(swappers):
##
##                #Check if the mouse is clicking the area
##                if rect.collidepoint(pos):
##
##                    #Get the next usable rotor in the list and swap it for the one being clicked on
##                    old=RotorNames[val]
##                    new=UsableNames[0]
##                    RotorNames[val]=new
##                    UsableNames.remove(new)
##                    UsableNames.append(old)
##
##                    old=Rotors[val]
##                    new=Usable[0]
##                    Rotors[val]=new
##                    Usable.remove(new)
##                    Usable.append(old)
            #--------------------------Not possible in new layout-------------------

        #Update the display
        pygame.display.update()

##########################         Plugscreen    #############################################################################################################
    else:
        for event in pygame.event.get():
            
            #Quit the program if the window gets closed
            if event.type==pygame.QUIT:
                run=False
                
            #Check if the user clicked
            if event.type==pygame.MOUSEBUTTONDOWN:
                
                #Change back to the main screen
                if event.pos[1]>350:
                    PlugScreen=False

                #Check for left click
                if event.button == 1:

                    #For each plug port, check if the mouse clicked it
                    for PortNumber, port in enumerate(ports):
                        if port.collidepoint(event.pos):

                            #A variable to help break out of the loops
                            found=False

                            #The position of the port in question          
                            PortPos=(port.x+20, port.y+20)

                            #For each pair of plugs
                            for num in PlugPositions:

                                #poslist is the 2 (x,y) pairings of the plugs
                                poslist=PlugPositions[num]

                                #for each plug in the number pairings
                                for i, pos in enumerate(poslist):
                                    
                                    #if the plug is on a port don't do anything
                                    if PortPos==pos:
                                        found=True
                                        break
                                    
                                    #Find the first numbered plug that is available (not in use, which means it is off the screen at (-50, 0))
                                    elif pos==(-50, 0) :

                                        #Set that first available plug's position to the new port position
                                        PlugPositions[num][i]=PortPos

                                        #If it is the first plug in the pair
                                        if i==0:
                                            #the variable 'pair' is equal to the letter at the index of the port that was clicked on
                                            pair=keyletters[PortNumber]

                                            #prevent a bug that occurs when you remove the first connection in a pair
                                        
                                            for k in Plugs:
                                                v=Plugs[k]
                                                if k==v:
                                                    Plugs[k]=keyletters[PortNumber]
                                                    Plugs[keyletters[PortNumber]]=k

                                                    alphabet=list(lowercase)
                                                    for letter in list(Plugs.keys()):
                                                        if letter in alphabet:
                                                            alphabet.remove(letter)
                                                    break
                                                    
                                            
                                        #If it is the second plug in the pair
                                        elif i==1:

                                            #Set the pairing of the first letter clicked and the second letter clicked
                                            Plugs[pair]=keyletters[PortNumber]
                                            Plugs[keyletters[PortNumber]]=pair

                                            #prepare the alphabet for the change in the Plugs
                                            
                                            alphabet=list(lowercase)
                                            for letter in list(Plugs.keys()):
                                                if letter in alphabet:
                                                    alphabet.remove(letter)
                                            
                                        #break
                                        found=True
                                        break
                                    
                                if found:
                                    break

                #Otherwise, if it is a right click
                elif event.button==3:

                    #For each plug port
                    for PortNumber, port in enumerate(ports):
                        found=False
                        if port.collidepoint(event.pos):

                            #for each plug, check if the mouse clicked it
                            for PLUG in PlugPositions:
                                PLUGS=PlugPositions[PLUG]
                                for i, plugpos in enumerate(PLUGS):
                                    if port.collidepoint(plugpos):

                                        #Return the plug back offscreen and delete its reference in the plug system
                                        PlugPositions[PLUG][i]=(-50, 0)
                                        letter_to_delete=Plugs[keyletters[PortNumber]]
                                        del Plugs[keyletters[PortNumber]]
                                        Plugs[letter_to_delete]=letter_to_delete


                                        alphabet=list(lowercase)
                                        for letter in list(Plugs.keys()):
                                            if letter in alphabet:
                                                alphabet.remove(letter) 

                                        #break
                                        found=True
                                        break
       
                                if found:
                                    break

                        if found:
                            break

        #Create the plugscreen visuals
        screen.fill(white)
        ports=[]

        #for each letter in each row, draw a port and a letter underneath the port
        for rowV, row in enumerate(keyboard):       
            for lettV, letter in enumerate(row):
                
                x=lettV*75+50+10*(3**rowV)
                y=rowV*125+100

                port=pygame.draw.circle(screen, black,(x, y-50), 20)
                ports.append(port)
                pygame.draw.circle(screen, gray, (x, y-50), 20, 2)
                
                Ptext = font.render(letter.upper(), True, DarkGray)  
                PtextRect = Ptext.get_rect()  
                PtextRect.center = (x-1, y)
                screen.blit(Ptext, PtextRect)

        #draw each plug wether it is onscreen or off
        for num in PlugPositions:
            poslist=PlugPositions[num]
            for pos in poslist:
                if pos[0]>0:
                    Pltext = font.render(str(num), True, white)  
                    PltextRect = Pltext.get_rect()  
                    PltextRect.center = pos
                    screen.blit(Pltext, PltextRect)
                    
        pygame.display.update()

#safely quit the program
pygame.quit()
