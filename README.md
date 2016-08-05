# myRuneRadio
Everything you need to upcycle an antique radio into a streaming music player
Intended as a basic one button functionality radio. Keep it simple. You can easily add more functionality.
This will only work using runeaudio and a ky040 rotary encoder in conjunction with a Hifiberry AMP+

##Instructions
Download and flash runeaudio to a raspberry pi
Install the amp hat
install the ky040 rotary encoder, and hook up to gpio pins (BCM mode)
+3 volts
common
###Clock Pin - gpio 5
###Data Pin - gpio 6
###Switch Pin - gpio 13
these pins are very easy to locate, if you don't understand where they are, simply 
hold the raspberry pi in your hand with the USB slots facing the ceiling.
count 1,2,3,4 pins up on the left side.
the 4th pin is 13, the one above that is 6, and the one above that is 5

boot it up
once booted pull this mother

thenrun:
[code]
sudo cp /path-where-this-repo-is-saved-on-your-pi/knob.py /var/www/command/knob.py

sudo cp /path-where-this-repo-is-saved-on-your-pi/knob.service /usr/lib/systemd/system/knob.service

"""start the service for testing"""
systemctl start knob.service

"""if it works as expected"""
systemctl enable knob.service

""" if not: """
systemctl stop knob.service
""" and figure out what you're doing wrong."""
[/code]
