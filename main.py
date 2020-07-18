import tkinter as tk
from tkinter import *
import urllib.request
import hashlib
import os, ssl

root = tk.Tk()
root.title('Password Cracker 9000')

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)): # Solves an SSL error I was getting
    ssl._create_default_https_context = ssl._create_unverified_context

HEIGHT = 500
WIDTH = 500
GRAY = '#302F32'
DARKGRAY = '#32322F'

COMMON_PASS = str(urllib.request.urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

def crackpass(event):
    
    hash_function = clicked.get() # This will pass into the crackpass funtion as whatever you selected to crack in (aka what crypto you want)
    sha1hash = hash_entry.get()
    md5hash = hash_entry.get()

    if hash_function == option[0]:
        for guess in COMMON_PASS.split('\n'):
            guesses = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest() # Digests the regular password and converts it to a SHA-1 hash
            label3 = tk.Label(frame, bg=DARKGRAY, text='The Password is: ' + str(guess), fg='#E5E5E5')

            if guesses == sha1hash: # if the digested password = the hash from input - pack the output
                    label3.pack(side='bottom')
                    return

    if hash_function == option[1]:
        for guess in COMMON_PASS.split('\n'):
            guesses = hashlib.md5(bytes(guess, 'utf-8')).hexdigest()
            label8 = tk.Label(frame, bg=DARKGRAY, text='The Password is: ' + str(guess), fg='#E5E5E5')

            if guesses == md5hash: # if the digested password = the hash from input - pack the output
                label8.pack(side='bottom')
                return

    else:
        label4 = tk.Label(frame, bg=DARKGRAY, text='That Password is not in this database', fg='red')
        label4.pack(side='bottom')


''' Start of the GUI -- Canvas is outer box, frame is the inner box where widgets are applied to
    lebel2 is an empty label for space between packs() hash_entry is key-binding to enter key so wither the button or enter can
    be pressed to submit the hash to the crackpass funtion, passing in <event> as the keybind '''

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg=GRAY)
canvas.pack()

frame = tk.Frame(root, bg=DARKGRAY)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = tk.Label(frame, bg=DARKGRAY, text='--- Import a Hashed Password ---', fg='#E5E5E5')
label.pack(side='top')


option = ['SHA-1','MD5'] # dropdown menu options
clicked = StringVar()
clicked.set(option[0])
drop = OptionMenu(frame, clicked, *option)
drop.pack(side='top')


label4 = tk.Label(frame, bg=GRAY) # spacer
label4.pack(side='top')

hash_entry = tk.Entry(frame, bg='white',)
hash_entry.bind('<Return>', crackpass)
hash_entry.pack(side='top')

label2 = tk.Label(frame, bg=GRAY) # spacer
label2.pack(side='top')

button = tk.Button(frame, text='Crack Password')
button.bind('<Button-1>', crackpass)
button.pack(side='top')

labelb = tk.Label(frame, bg=DARKGRAY)
labelb.pack(pady=10, side='bottom')

root.mainloop()
