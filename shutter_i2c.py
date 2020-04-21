import time
import board
import busio
import digitalio

from adafruit_mcp230xx.mcp23017 import MCP23017


class ShuttersController:

    i2c = None
    mcp0 = None
    mcp1 = None

    shutters = [
        {"name": "Volet 1", "id": 1, "pin_up": 1, "pin_down": 0, "group": False},
        {"name": "Volet 2", "id": 2, "pin_up": 3, "pin_down": 2, "group": False},
        {"name": "Volet 3", "id": 3, "pin_up": 5, "pin_down": 4, "group": False},
        {"name": "Volet 4", "id": 4, "pin_up": 7, "pin_down": 6, "group": False},
        {"name": "Volet 5", "id": 5, "pin_up": 9, "pin_down": 8, "group": True, "group_name": "Group 1"},
        {"name": "Volet 6", "id": 6, "pin_up": 11, "pin_down": 10, "group": False},
        {"name": "Volet 7", "id": 7, "pin_up": 13, "pin_down": 12, "group": False},
        {"name": "Volet 8", "id": 8, "pin_up": 15, "pin_down": 14, "group": False},
        {"name": "Volet 9", "id": 9, "pin_up": 17, "pin_down": 16, "group": True, "group_name": "Group 2"},
        {"name": "Volet 10", "id": 10, "pin_up": 19, "pin_down": 18, "group": False},
        {"name": "Volet 11", "id": 11, "pin_up": 21, "pin_down": 20, "group": False},
        {"name": "Volet 12", "id": 12, "pin_up": 23, "pin_down": 22, "group": False},
        {"name": "Volet 13", "id": 13, "pin_up": 25, "pin_down": 24, "group": False},
        {"name": "Volet 14", "id": 14, "pin_up": 27, "pin_down": 26, "group": False},
        {"name": "Volet 15", "id": 15, "pin_up": 29, "pin_down": 28, "group": False},
        {"name": "Volet 16", "id": 16, "pin_up": 31, "pin_down": 30, "group": False},
    ]

    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.mcp0 = MCP23017(self.i2c)
        self.mcp1 = MCP23017(self.i2c, address=0x21)
        for i in range(16):
            pin = self.mcp0.get_pin(i)
            pin.direction = digitalio.Direction.OUTPUT
            pin.value = False
            pin = self.mcp1.get_pin(i)
            pin.direction = digitalio.Direction.OUTPUT
            pin.value = False

    def get_pin(self, pinid):
        if pinid < 16:
            return self.mcp0.get_pin(pinid)
        return self.mcp1.get_pin(pinid % 16)

    def get_shutters(self):
        return self.shutters

    def push_button(self, pinid):
        pin = self.get_pin(pinid)

        pin.value = True
        time.sleep(1)
        pin.value = False

    def push_two_buttons(self, pinid1, pinid2):
        pin1 = self.get_pin(pinid1)

        pin2 = self.get_pin(pinid2)

        pin1.value = True
        pin2.value = True
        time.sleep(1)
        pin1.value = False
        pin2.value = False

    def shutter_up(self, shutterid):
        for shutter in self.shutters:
            if shutter['id'] == shutterid:
                self.push_button(shutter['pin_up'])

    def shutter_down(self, shutterid):
        for shutter in self.shutters:
            if shutter['id'] == shutterid:
                self.push_button(shutter['pin_down'])

    def shutter_group_up(self, shutterid):
        for shutter in self.shutters:
            if shutter['id'] == shutterid and shutter['group']:
                self.push_two_buttons(shutter['pin_up'], shutter['pin_down'])
                self.push_button(shutter['pin_up'])

    def shutter_group_down(self, shutterid):
        for shutter in self.shutters:
            if shutter['id'] == shutterid and shutter['group']:
                self.push_two_buttons(shutter['pin_up'], shutter['pin_down'])
                self.push_button(shutter['pin_down'])

    def shutter_all_up(self):
        for shutter in self.shutters:
            pin = self.get_pin(shutter["pin_up"])
            pin.value = True
        time.sleep(1)
        for shutter in self.shutters:
            pin = self.get_pin(shutter["pin_up"])
            pin.value = False

    def shutter_all_down(self):
        for shutter in self.shutters:
            pin = self.get_pin(shutter["pin_down"])
            pin.value = True
        time.sleep(1)
        for shutter in self.shutters:
            pin = self.get_pin(shutter["pin_down"])
            pin.value = False
