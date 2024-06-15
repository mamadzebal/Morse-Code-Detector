import network, socket
import urequests
import _thread
import time
import MyModel
from lsm6dsox import LSM6DSOX
from machine import Pin, I2C, SoftI2C
import ssd1306
import time


class Module:
    def __init__(self):
        """
        Constructor
        """
        self.thread_data = {
            'thread_running': False,
            'should_stop': [False],
            'thread_id': None
        } 

        self.ssid = "Mohammad"
        self.password = "12345678"

        self.array_values = []
        self.alphabet_string = []
       
        self.SERVER_ADDRESS = "http://192.168.137.1:5000"

        self.i2c = SoftI2C(scl=Pin(13), sda=Pin(12))
        # self.oled_width = 128
        # self.oled_height = 32  # Adjusted for 128x32 OLED display
        # self.oled = ssd1306.SSD1306_I2C(self.oled_width, self.oled_height, self.i2c)
        # self.devices = self.i2c.scan()
        
    def connect(self):
        self.initNet(self.ssid, self.password)

    def initNet(self, ssid, passwd=None):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if not wlan.isconnected():
            print('connecting to network...')
            if passwd == None:
                wlan.connect(ssid)
            else:
                wlan.connect(ssid, passwd)
            while not wlan.isconnected():
                pass
        print('network config:', wlan.ifconfig())

    def send_get_request(self, string_data, should_stop = False):
        url = "{}/string?data={}".format(self.SERVER_ADDRESS, string_data)

    
        try:
            response = urequests.get(url)
            if response.status_code == 200:
                print("GET request successful. Response:")
                print(response.text)
            else:
                print("Failed to send GET request. Status code:", response.status_code)
        except Exception as e:
            print("Error:", e)
            

    def send_request_async(self, string_data): 
        self.thread_data['thread_id'] = _thread.start_new_thread(self.send_get_request, (string_data, self.thread_data['should_stop']))

    def send_cursor_request(self, start):
        # if(not start):
        #     self.update_display("")
        string = "True" if(start) else "False"
        url = "{}/cursor?data={}".format(self.SERVER_ADDRESS, start)
        
        try:
            response = urequests.get(url)
            if response.status_code == 200:
                print("GET request successful. Response:")
                print(response.text)
            else:
                print("Failed to send GET request. Status code:", response.status_code)
        except Exception as e:
            print("Error:", e)
            

    def detect_alphabet(self, morse_array):
        morse_code_dict = {
            '01': 'A', '1000': 'B', '1010': 'C', '100': 'D', '0': 'E', '0010': 'F', '110': 'G', '0000': 'H',
            '00': 'I', '0111': 'J', '101': 'K', '0100': 'L', '11': 'M', '10': 'N', '111': 'O', '0110': 'P',
            '1101': 'Q', '010': 'R', '000': 'S', '1': 'T', '001': 'U', '0001': 'V', '011': 'W', '1001': 'X',
            '1011': 'Y', '1100': 'Z', '01111': '1', '00111': '2', '00011': '3', '00001': '4', '00000': '5',
            '10000': '6', '11000': '7', '11100': '8', '11110': '9', '11111': '0'
        }
        # Convert the array of 0s and 1s to a string
        morse_string = ''.join(map(str, morse_array))
        
        # Look up the Morse code string in the dictionary
        return morse_code_dict.get(morse_string, '')

    def show_output(self, out_array):
        combined_string = ''.join(out_array)
        # self.update_display(combined_string)
        should_stop = self.send_request_async(combined_string)


    def update_display(self, state):
        self.oled.fill(0)  # Clear the display
        self.oled.text(state, 0, 0)
        self.oled.show()  # Update the display

    def mymain(self):
        lsm = LSM6DSOX(self.i2c)
        clf = MyModel.RandomForestClassifier()
        accel_data = lsm.accel() 
        gyro_data = lsm.gyro()
        x = [accel_data[0], accel_data[1], accel_data[2], gyro_data[0], gyro_data[1], gyro_data[2]]
        y = clf.predict(x)
        print(y)
        if(y == 3):
            self.alphabet_string.append(' ')
            # self.show_output(self.alphabet_string)
            self.send_request_async(' ')
            self.array_values = []
        elif(y == 2):
            alphabet = self.detect_alphabet(self.array_values)
            if(alphabet != ''):
                self.alphabet_string.append(alphabet)
                # self.show_output(self.alphabet_string)
                self.send_request_async(alphabet)
                print(alphabet)
            self.array_values = []
        else:
            self.array_values.append(y)