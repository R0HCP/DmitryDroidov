from telethon import TelegramClient, events, sync
 # if u clone this repo u have to create config.py by yourself
from bard import answer
from config import api_id, api_hash, konstantin, igor, google_api_key, me
import texting
from texting import dm
import subprocess
import os


if os.path.isfile('config.py'):

    client = TelegramClient('test', api_id, api_hash)
    texting.dm(client)

else:
    print ("""
                                                                                                                                                                      
                                                                                                                                                           
                                         @@@                            @@@%....  =@@@@                                                                    
                                        @. .@@                      @@@.    .....     .@                                                                   
                                        @     @@                   @.   :.:.....    .. %                                                                   
                                       ..     ..@@                @. .........  .@@@  .%                                                                   
                                       @         .@@               @........  :@    @ =@                                                                   
                                       @            @@              @ .:... .@       -@                                                                    
                                     .@             .@@@             @ ....-@        #                                                                     
                                     .@               ..@@           @@ ..@@                                                                               
                                     .                   .@@@@@@@@%...@  .@@                                                                               
                                  +:.@@@@@@@@@@@@@@@@@@#*-.         .. @  @  @@@@@@@@@@@@                                                                  
                                    .@. .             ................  @.:+              :@@@                                                             
                                       @@+*=:................................:............     .@@                                                         
                                   @.       :.:.:..............................................    @@                                                      
                                   @. .    =%.:...................................................  .@@                                                    
                                   @.    @++..:....................................................:  .@@                                                  
                                   @.  @*-........................................................:-+*=..@                                                 
                                    %-@.........................................................::.       %@@@@                                            
                                    @  .:..........................................................@@              @@@                                     
                                  @:  .:........................................................... @@  .   .  ..        @@@                               
                                 @. ...::..:......................................................:. @@          ..           @@                           
                                @  ..::........   ....   ............................................ @@          ...             @@@                      
                               @. .....::...   @@@ .  -@@ :........................................... @           ....              .@@@                  
                           @@@. ..::::......@@@@@@@@@@@@... ............:..          .:::.............. @        ....                    .@@@              
                       **..           .....:...           @ ..........:... @@@@@@@@@@    ..............  @     ...                           .@@           
                            @@@@@@@@@@%.-=*#              @ ............@=::.        +@@   ............. @.    .                                .@         
                               @                        . @ :...........:.+  :@@@@@.    @@  ............. @    .....                           @@          
                              @..:.   @@@          @@@ .. @ ..........:-:+          @@*.  @  ...........: -@        ....                     @.            
                             @.    @@@@@  .       @@@@ .   @ ........ @ --             #@  @ .:........... @      ......                   @@              
                            @. .@@    @.     ..  @@@@-     @ .......: @ +       .   .    .- @ ...:......... @   ....                     @.                
                           @#.@@@@@@@@@    @  . @@@@@       @ ....... @    @@             @  @...:......... .@*                        @.                  
                           #@   @.      @  @    @@@@         @ ...... @   @@@@ .          @:.....:.......  .. @@                     @=                    
                                 @@    %@@      @@.           @..... @   @@@@@ .          .%.::..........@@%.   @                  @@                      
                            @@@@@@   @%   ......               @:... @  @@@@@  ...         @ .:::.......%-  @@@@-@              .@@                        
                            .          @                        .@==:@  @@@@    ........   @ ...:.......@         @          ..@                           
                            @.      %   @% .       .     .......   @.  -@@@             .. @ .........@@            ....  ..@@                             
                            @@     @%   . @..........@@@ ..                           @@   @ ....:.. @         .....    .@@                                
                             @     .@           . *+                               @@     @@ ......%@        ...    ..@@                                   
                              @.    @                                                  @@  :..:...@%  @@  ....   ..@@                                      
                               @@   .@                                                     :@....@    @@ ...   .@                                          
                                @@.   @                                  @                  @ ..@   @@          @@                                         
                                  @.      @@@@@= @@                   @@.@                  @.@@      #@+   .   .@@                                        
                                   @@.        %...:+#@@@:    @@@######+-@                    @           @@@+   ..@                                        
                                     @@.      @*.:   @*.*####*-:-===+++-                                @*.@@                                              
                                       @@      @#+.@   .:::--=====-::*.                               @  @   .@                                            
                                          %@     :@  :::.::::::. .-@@                               @@@@@@ ..  .%                                          
                         @@@@@               @@   #-=:....    =#@@.                              @@..        +@@                                           
                        @@.  @                 @@@..=##@@@@@@@*                           -@@@@  @@@@@+=.@.#@                                              
                @@@@   @@.   .@                   @@@.             @@@@             @ .....   @@#.   .:: @@                                                
            @@ . .. @  @..     @                   @@@@@-     @@@@         .....+@@@@@@     @@   ::::::: @                                                 
          @..       .@ @.     .@                 @@..   .*@                 ..            @#  .::::::-:::@                                                 
          @         ..@@.      @                @ .  %@@@                    ....      @@:  :::::::::::: .@@                                               
          @.         .@.       @                @@. .@                               @@+  :::::::::::::::   @@                                             
     @@   .=                   @                @@@  @@                        .   @@   ::::::::::::::::::.  =@                                            
    %@..@@@@.                  @@            @@@    . @@                    ..   @@   :::::::::::::::::::::: .@                                            
     @                        .@@...@        @   ::::. @@                  .   @#  .:::::::::::::::::::::::: %@                                            
     @.                      +@     .@      @@@@  .-::. @@              ..   @*. .::::::::::::::.    +*+=:-. @%                                            
     @                     .@       .#      @.  @@  :::. @@            .   @*  .::::::::::::   :=@@@@   #**.:@                                             
      @.                            @     @@.   .:@-  ::. =@             @@  ::::::::-:    -@@@@            @@                                             
       .@               +          @     @@    .=  -@   :: @@          %@  .:::::::    +@@@       .    .     @                                             
         @%           :@          @     @-     :=::  @@     @         @@  ::--:    +@@@           .           @                                            
           @.         @         @@.@   @       ..:::.  @@    @       @  .::    +@@+                           .@                                           
            @         @             @ @.       @ :::::.   @@  @    @@.     @@@:    :.@  .                     .@                                           
            @%        @           =--..=+@@    @ ::::::::   @@%@ *@+ ..@@@.    ::::: @% .                      @@                       @@@@@@@=.#         
            @@.                .@**-:::-: @    @ ::::::::::.   =+=: :::    :-::::::: #@ .                      @@                 @@@          .%          
             @@              @@=-.:::::::- @   @ :::::::::::::::::::::::::::::::::::: @                       ..@             @@@.            @            
               @          *@%+::::::::-:-* @.  @ :::::::::::::::::::::::::::::::::::: @                        .@          @@.              +-             
                 @@@@@@@@#-  :::::::::::-*  @  @ ::::::::::::::::::::::::-::::::::::: @                        .@        @.                #.              
                  @.     .::::::::::::::=:  @  @ .-:::::::::::::::::::::::::::::::::: @#                       .@      +  :@#@            ::               
                  @ ::::::::::::::::::--#    @ @+ ::::::::::::::::::::::::::::::::::: :@                       .@   . @=@=. @            .@                
                  @ :::::::::::::::::-+#        @ :::-:::::::::::::::::::::::::::::::: @                        @@ ..--     @           .@                 
                 ##.:::::::::::::::-+#.         @%.=--:::::::::::::::::::::::::::::-=+.@:                        @.::..:...@           .@                  
                  @. :::::::::::-=+#.            @  +*####***+=+=====+++**#######*+:    @  @@@@@:                @ ::..... @         . =@                  
                  +@ ::::::--=+#**                @           :::-::::             @@@@@@@%       @@             @ ...... @   .        @                   
                   @.:*****#*-                    @                                         @@+      @           @ ......:@          .@                    
                    @                              @                     @@@@##+@@             @       @  .      @+.:....@--:         @                    
                     @                             @                  +@-    .:   @@            @-      @ .     . @ :......-=-=@@   .@                     
                      @                            @@     .          @    ::::-::.  @@           @                @ :.......  @     @@                     
                       @                          .@@              @@  @@  .:::::::  #@                           @ ........ @      @                      
                        @.                       @@ @@           @@      @@  :::::::. :@                          @ .......:@      +@                      
                          @                    .@@   @:        -@          @-::::::::: @@                       . @ ......=@       @                       
                           .              .    @@     @       @@                                                  %       *       .@  
-hiiiiiiiii, i see u don't have config? no worriers let's create it! + Style.RESET_ALL                     
           """)
    
    