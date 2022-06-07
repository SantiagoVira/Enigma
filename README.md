# Enigma

Simulator based on the original [Enigma Machine](https://en.wikipedia.org/wiki/Enigma_machine) from WWII created using python.

Before running the program, install pyperclip through `pip install pyperclip`

Start up the project by simply running the `main.py` file.


# Instructions

**Setting Up The Plugborad**

To access the plugboard, click on the bottom of the screen, on the handlebar below the letters. This will bring up another screen with 26 ports and a sidebar displaying any current connections. To connect two letters together, simply left click on the letters you would like to connect. To remove plugs, left click again on any letter in a pair to disolve the connection.

**Setting Up The Rotors**

You can click the top of the screen (where the handle has moved) to switch back to the main view. Above all of the letters, you will see 3 rectangles each with 3 letters. These are the rotors, and changing their positions before the Encryption is another step to prevent the message from being decrypted. To turn them, click on the top section of the rectangle to turn the rotor up, and the bottom section to rotate it down.

**Encryption Time**

- _Saving your setup_

  - To ensure someone else can decrypt your message properly, make sure to press the "Export setup" button to save your rotor positions and plugboard connections for easier sharing.
  - Test that this has worked by pasting what has been copied somewhere. The code will be in the format `0,0,0,ABCD` where 0s are your rotor positions and letters are your plugboard connections (There can be anywhere from 0-26 letters in this code)
  - If the copying has not worked and continues to not work, find a way to share your rotor letters and plugboard connections in a way that works for whoever may decrypt your message.

- _Creating Your Message_
  - On the main screen, simply start typing your message from your physical keyboard and take note of which letters on the screen shine (Each input and output pair will be printed to the console if that is an easier method of collecting the message)

**Decrypting!!**

- _Loading your setup_

  - If you recieved a code in the format mentioned above, copy that code to your clipboard and press the "Import setup button"
  - If this does not change anything on the rotors or plugboards, or you did not recieve a code but rather instructions, make sure to set up your machine exactly as the encrypter set theirs up, otherwise the message will not come through

- _Retrieving your message_
  - On the main screen, simply start typing your message from your physical keyboard and take note of which letters on the screen shine (Each input and output pair will be printed to the console if that is an easier method of collecting the message)

# Example

```
Setup code: 22,23,8,CORNEY
Message: ESWTCJTEDEFHIEPZWDV
```

# Misc.

- If at any point you mistype a letter, rotating the rotors back to their positions (the rotors rotate down for every letter you type) before you typed the wrong letter will fix the issue. If you cannot remember what the rotors looked like, you may be safer off importing the setup again and re-typing the message.

# Enjoy!
