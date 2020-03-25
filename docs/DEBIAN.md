Running on Debian
==========

To make it work in realtime (Debian):

$ sudo apt-get install cutecom socat pygame python-serial

$ sudo gpasswd --add $USER dialout

Then logout / reboot

$ socat -d -d pty,raw,echo=0 pty,raw,echo=0

This will give you the two virtual serial port addresses. Set PORT in dashboard.py to one, and in cutecom the other. Also, in cutecom -> baud rate -> 9600.

$ python dashboard.py

In cutecom you should see FF FF EF - reply with 10 and the dashboard.py window should come to life. cutecom -> send file -> test_data.hex file.

Currently the data displayed is MPH, RPM (large centre arcs), AAC, MAF, temperature and battery voltage. The script is actually streaming 14 data values but these are the most useful to display. Pressing f will make it go fullscreen, w will make it revert back to windowed mode.
