import time
from machine import Pin
import module

mycode = module.Module()
mycode.connect()

in26 = Pin(26, Pin.IN, Pin.PULL_UP)
in26_on_off = False
# mycode.send_cursor_request(in26_on_off)

while (True):
    if(in26.value() == 0):
        in26_on_off = not in26_on_off
        # mycode.send_cursor_request(in26_on_off)
    
    if(in26_on_off):
        mycode.mymain()

    time.sleep_ms(2000)