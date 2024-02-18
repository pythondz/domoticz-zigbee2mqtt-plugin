import json

import domoticz
from adapters.base_adapter import Adapter
from devices.sensor.smoke import SmokeSensor
from devices.sensor.co2 import CO2Sensor


class TS0601SmartCOAirBox(Adapter):
    def __init__(self):
        super().__init__()

        self.devices.append(CO2Sensor('co',
                                        'co',
                                        '(Carbon Monoxyde value)'))