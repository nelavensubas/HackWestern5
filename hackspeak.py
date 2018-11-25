import requests
import serial
from time import sleep

# Use as default
PORT = "/dev/tty96B0"
API_WRITE_KEY = "0O4P5J4011DLCGJ9"

def set_serial(port):
    try:
        comm = serial.Serial(port, 9600,timeout=0, parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
        print 'Serial Connection Established'
    except:
        print 'Serial Connection Failed'
    return comm

def prepare_data(raw):
    # split frames such that we discard incomplete frames
    if "\r\n" in raw:
        raw = raw.split("\r\n")
        print 'raw: '
        print raw[0]
                print raw[1]
        try:
                        print 'Preparing URL'
            url = 'https://api.thingspeak.com/update?api_key=0O4P5J4011DLCGJ9&field1=%s&field2=%s' % (raw[0],raw[1])
                        print 'Sending GET'
                r=requests.get(url)
            print 'Sent to ThingSpeak'
        except:
            print 'Failed to send to ThingSpeak'
            return

if __name__ == '__main__':

    serial = set_serial(PORT)

    while True:
        queue = serial.inWaiting()
        if queue > 0:
            data = serial.read(1000)
            prepare_data(data)
        sleep(5)
