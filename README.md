# sparkfunOledBlock
Sample Programs for using the Sparkfun OLED Block

There are three files here, the first two lcdWakeUp.py and lcdWakeUp.service will display your Edison's IP on boot. The third is an example of reading the buttons on the Sparkfun OLED Block and display on the OLED screen. 

#lcdWakeUp
To use this copy lcdWakeUp.py in to /home/root on your edison, next copy lcdWakeUp.service in to /lib/systemd/system. Run the command "systemctl enable lcdWakeUp.service" after to have this run on boot. 

#OLED.py 
This example script will read the 7 buttons on the OLED shield and display the output on the Edison. Simply run ./oled.py to execute. The only option is --debug which will display inputs on the terminal. 

    root@edison1:~# ./oled.py -h
    usage: oled.py [-h] [--debug] [--version]
     
     Demo App for Sparkfun OLED Edison Shield
     
     optional arguments:
      -h, --help  show this help message and exit
      --debug     Display button readings on terminal
      --version   show program's version number and exit
