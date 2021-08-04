# MASS (Mr. Adasko's Security System)

The program is capable of detecting faces using camera vision.
Furthermore, the socket server can be hosted on an external circuit board such as Raspbery Pi. 
This way it is possible to connect to the monitoring system remotely.

## Table of Contents

### [ **1. Introduction** ](#1-introduction)
### [**2. Set-up**](#2-set-up)
### [**3. Usage**](#3-usage)

---

# 1. Introduction
This system could be implemented to monitor the entry door of the house.
It would monitor the people moving near the entry, which could potentially
recognize suspicious people. Additionally, in case of the thieves breaking in
the system would notify the user by sending an email with pictures of the thieves.

# 2. Set-up
In order to use the program, some basic set up procedures have to be done:
- In server.py files the local IP address has to written in line 6
- In network.py files the local IP address has to written in line 8
- In detect_faces.py the email addresses have to be written in line 16 and 17
- The images folder must include at least one picture of a person in jpg format.
You can add pictures of your family members, friends, girlfriend, boyfriend, etc.
  
After these steps the program is operational.

# 3. Usage
First the server.py file has to be run on the external circuit board/computer, then the 
detec_faces.py also has to be run. The user.py can be run on the user computer to connect
to the local socket server.