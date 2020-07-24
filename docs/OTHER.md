==========
Running Stream Live Data
==========

Launch ports script:

$ ./ports.sh

Start the script (this should open the display window):

$ python streamLiveData.py

The display should update to show a all dials.
Start minicom (e.g.):

$ minicom -b 9600 -D '/dev/pts/3' -H

Reply to the prompt to start data transfer (e.g.):

$ echo -ne '\x10' > /dev/pts/3

To send test_data.hex, in minicom hit 'Ctrl + A' then 'S' -> ascii -> path to test_data.hex


==========
Running Consult Serial Graphics to display single dial
==========

Launch ports script:

$ ./ports.sh

Start the script (this should open the display window):

$ python consultSerialGraphics.py

Start minicom (e.g.):

$ minicom -b 9600 -D '/dev/pts/3' -H

Reply to the prompt to start data transfer (e.g.):

$ echo -ne '\x10' > /dev/pts/3

The display should update to show a dial.
To send test_data.hex, in minicom hit 'Ctrl + A' then 'S' -> ascii -> path to test_data.hex


==========
Running Rotate Image to test dial/needle revolution
==========

Launch ports script:

$ ./ports.sh

Start the script (this should open the display window with dial and log values to cmd):

$ cd demos/
$ python rotateImage.py


==========
Running Open Port to print RPM
==========

Launch ports script:

$ ./ports.sh

Start the script (this should log values to cmd):

$ cd demos/
$ python openPort.py

Start minicom (e.g.):

$ minicom -b 9600 -D '/dev/pts/3' -H

Reply to the prompt to start data transfer (e.g.):

$ echo -ne '\x10' > /dev/pts/3

To send test_data.hex, in minicom hit 'Ctrl + A' then 'S' -> ascii -> path to test_data.hex


==========
Running Single Dial Demo to display single dial
==========

Launch ports script:

$ ./ports.sh

Start the script (this should open the display window):

$ cd demos
$ python singleDialDemo.py

Start minicom (e.g.):

$ minicom -b 9600 -D '/dev/pts/3' -H

Reply to the prompt to start data transfer (e.g.):

$ echo -ne '\x10' > /dev/pts/3

The display should update to show a dial.
To send test_data.hex, in minicom hit 'Ctrl + A' then 'S' -> ascii -> path to test_data.hex


==========
Other demos
==========
Follow process above for importDials and importSingleDial
