#!/usr/bin/python
import time
from MCP342X import *
adc = MCP342X()
while True:
    print (adc.read(0))
    time.sleep(0.1)
