Running on Linux/Centos/Fedora
==========

To make it work in Linux/Centos/Fedora distros:

Note: EPEL repository is required to fetch pygame

$ sudo yum install minicom socat python2-pygame pyserial

$ sudo gpasswd --add $USER dialout

Then logout / reboot

$ socat -d -d pty,raw,echo=0 pty,raw,echo=0

This will give you the two virtual serial port addresses. Set PORT in dashboard.py to one of them, the other virtual port is used by minicom.

$ minicom -b 9600 -D <second_virtual_port> -H

$ python dashboard.py

This will launch the dashboard window. In minicom you should see FF FF EF, reply with 10 and the dashboard.py window should come to life.

$ echo -ne '\x10' > <second_virtual_port>

To send test_data.hex, in minicom hit 'Ctrl + A' then 'S' -> ascii -> path to test_data.hex

Currently the data displayed is MPH, RPM (large centre arcs), AAC, MAF, temperature and battery voltage. The script is actually streaming 14 data values but these are the most useful to display. Pressing f will make it go fullscreen, w will make it revert back to windowed mode.
