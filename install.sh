#!/bin/bash
FILE="/tmp/out.$$"
GREP="/bin/grep"
clear

if [[ $EUID -ne 0 ]]
then
   clear
   echo -e "Zəhmət olmasa *root* icazəsi ilə yenidən yoxlayın!"
else
   clear
   echo -e "AzI Hash Tool yüklənir :)"
   apt install pip
   apt install python3
   python3 -m pip install --upgrade pip
   pip install hashlib
   pip install pyfiglet
   clear
   echo -e "AzI Hash Tool yükləndi. python3 azihashtool.py yazaraq proqramı başlada bilərsiniz :)"
fi
exit
