import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import sys
import time

head = """                                   ||                                   
                                   ||                                   
                                   ||                                   
                                   ||                                   
                                   ||                                   
                              .    ||    .                              
                            ..     ||     ..                            
                          .:       ||       :.                          
                        .::        ||        ::.                        
                        ::         ||         ::                        
                       .:      ....::....      :.                       
                       ::     ::::::::::::     ::                       
                   .   ::    ::::::::::::::    ::   .                   
                  .    ::   ::::::''''::::::   ::    .                  
                 :     ::   :::::: :: ::::::   ::     :                 
                :'     ::   :::::: :: ::::::   ::     ':                
               ::      ::.  ::::::....::::::  .::      ::               
                :.      '::::::::::::::::::::::'      .:                
                ::          '::::::::::::::'          ::                
                 ::.          ::::::::::::          .::                 
                  ::. ......:''::::::::::'':...... .::                  
                   ':::''''' ...::::::::... ''''':::'                   
                        ....''''::::::::''''....                        
                    ...'''   .::'::::::'::.   '''...                    
                   ::'      .::  ':'':'  ::.      '::                   
                   ::      :::            :::      ::                   
                   :      ::'              '::      :                   
                   ::    ::                  ::    ::                   
                    '.  .:                    :.  .'                    
                     :. ::                    :: .:                     
                        :'                    ':                        
                       .:                      :.                       
                       ::                      ::                       
                       ::                      ::                       
                        ::                    ::                        
                         ':                  :'                         
╭──────────────────────────────────────────────────────────────────────╮
│ ╭──────────────────────────────────────────────────────────────────╮ │
│ │     ______   ______    ________   _______     _____   ______     │ │
│ │    /  ____| |   _  \  |__    __| |       \   |   __| |   _  \    │ │
│ │   |  |___   |  | |  |    |  |    |  |‾‾\  \  |  |__  |  | |  |   │ │
│ │    \___  \  |   ‾  /     |  |    |  |   |  | |   __| |   ‾  /    │ │
│ │        |  | |  |‾‾‾      |  |    |  |__/  /  |  |__  |  |\  \    │ │
│ │   |‾‾‾‾  /  |  |      |‾‾    ‾‾| |       /   |     | |  | \  \   │ │
│ │    ‾‾‾‾‾‾    ‾‾        ‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾     ‾‾‾‾‾   ‾‾   ‾‾‾   │ │
│ │                                                                  │ │
│ │             _______    ______     ______    ___    ___           │ │
│ │            /  _____|  |   _  \   /  __  \  |   \  /   |          │ │
│ │           /  /  ____  |  │ │  | |  |__|  | |    \/    |          │ │
│ │          |  |  |__  | |   ‾  /  |   __   | |          |          │ │
│ │           \  \___/  / |  |\  \  |  |  |  | |  |\__/|  |          │ │
│ │            \       /  |  | \  \ |  |  |  | |  |    |  |          │ │
│ │             ‾‾‾‾‾‾‾    ‾‾   ‾‾   ‾‾    ‾‾   ‾‾      ‾‾           │ │
│ ╰──────────────────────────────────────────────────────────────────╯ │
╰──────────────────────────────────────────────────────────────────────╯"""

# Determine if the application is running as a bundled executable
if getattr(sys, 'frozen', False):
    # If bundled, set the base path to the temporary directory
    base_path = sys._MEIPASS
else:
    # If not bundled, set the base path to the directory containing the script
    base_path = os.path.dirname(__file__)

# Construct the full path to the audio file
audio_file_path = os.path.join(base_path, "bonelordvoice_calm#1.wav")

pygame.mixer.init()
pygame.mixer.music.load(audio_file_path)

def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        pygame.mixer.music.play()
    print()  # Move to the next line after finishing

#"""

type_text("<WARNING: Incoming Spidergram | (TAX: 5 q-bits) | >")

def spinning_cursor():
    spinner = ['-', '\\', '|', '/']
    for _ in range(20):  # Loop for a while
        for symbol in spinner:
            sys.stdout.write(f"\r<WARNING: Incoming Spidergram | (TAX: 5 q-bits) | > {symbol}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r<WARNING: Incoming Spidergram | (TAX: 5 q-bits) | >   \n")  # Clear the line

sys.stdout.write(f"\033[F\033[K")
spinning_cursor()


def print_fall_down(heading_lines, delay=1.0):
    nn = len(heading_lines) # line count
    blank_line = " " * len(heading_lines[0]) # requires that all lines be the same length

    # print all of the blank lines
    for __ in range(nn):
        print(blank_line)

    sys.stdout.flush()
    time.sleep(delay)

    for ii in range(nn+1):
        # go to the top line
        sys.stdout.write(f"\033[{nn}F")

        # rewrite each line
        for jj in range(nn):
            line = blank_line
            if jj < ii:
                line = heading_lines[nn-ii+jj]
            sys.stdout.write("\033[K")
            print(line)

        sys.stdout.flush()
        time.sleep(delay)

head_lines = head.splitlines()
spider_body = head_lines[0:36]

print_fall_down(spider_body, 0.015)

# PRINT UP

blank_line = " " * len(head_lines[0]) # requires that all lines be the same length

for ii in range(36):
    # Move the cursor up 36 (length of spider body)
    sys.stdout.write(f"\033[36F")

    # rewrite each line
    for (jj) in range(36):
        line = blank_line
        if ii + jj + 1 < 55:
            line = head_lines[ii+jj+1]
        sys.stdout.write("\033[K")
        print(line)
    
    sys.stdout.flush()
    time.sleep(0.05)

"""   

# print all of the blank lines
for __ in range(36):
    print()

"""

# Go up 16 lines
sys.stdout.write(f"\033[16F")

type_text("<in>: This is a welcome letter brought to you by Spider Telegrams <STOP>")
time.sleep(5)

# Go Down 1 line
sys.stdout.write(f"\033[E")

type_text("<in>: The funds for this message will be removed from your account<STOP>")

# Go Down 1 line
sys.stdout.write(f"\033[E")

type_text("<in>: Aerospace Industries has been made aware of your interests  <STOP>")
time.sleep(3)

# Go Down 1 line
sys.stdout.write(f"\033[E")

type_text("<in>: This mission is a dangerous one ~ It will take many efforts <STOP>")

# Go Down 1 line
sys.stdout.write(f"\033[E")

type_text("<in>: Do you wish to proceed? Place forehead to screen and decide <STOP>")
time.sleep(11)

# Go Down 1 line
sys.stdout.write(f"\033[E")

type_text("<in>: Failure to comply will result in expulsion from the mission <STOP>")
time.sleep(7)

# Go Down 1 line
sys.stdout.write(f"\033[E")

type_text("<in>: Neural-sensor TCP error: failed to get response from reader <STOP>")

# Go Down 1 line
sys.stdout.write(f"\033[E")

type_text("<in>: I am sorry you have wasted our time. Please do not reach out<STOP>")
time.sleep(2)

