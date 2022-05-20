# GPS-tracker-RaspberryPi
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Description
A Raspberry-pi based GPS tracking device allows users to have pin point tracking device with python3 script. (accuracy will be depending on the GPS module you choose)

# Hardware requrement list
1)- Raspberry-Pi (3/3b/4/4b/Zero W 2)

2)- GPS module (With USB connectivity)

3)- Power bank battery pack (with 5volt output)

# Preparing Raspberry-PI envoirment
Preperation in steps as following: 

Step1: Install Oprating system for your raspberry-pi (raspbian lite is recommended, However, any linux based system is fine too)

step2: Install required libraries and update Operating System. (command to install all libraries requred: sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y && sudo apt clean && sudo apt install python3 -y && sudo -H pip3 install gps3 && sudo pip install ubidots==1.6.6 && pip install requests && sudo apt install time -y)

Step3: Test your raspberry-pi and GPS module make sure its running before you start coding (link to test your USB based GPS module https://wiki.52pi.com/index.php?title=EZ-0048). make sure to update your Oprating system (command to update your Operating System: sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y && sudo apt clean)

step4:

step5: Creating python 3 script (find script in a project folder named: tracker_Script)
