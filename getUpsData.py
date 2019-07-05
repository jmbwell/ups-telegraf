#!/usr/bin/env python3

import subprocess

cmd="upsc ups"
output=""
# only needed measurement
measurements=["battery.charge","battery.voltage","battery.runtime","input.voltage","ups.load",
            "ups.beeper.status", "ups.mfr","ups.model", "ups.serial", "ups.status", "ups.test.result"]
# text measurement
string_measurements=["battery.mfr.date", "battery.type", "battery.date", "device.mfr", "device.model","device.serial","device.type",
			"driver.name", "driver.paramter.port", "driver.parameter.synchronous", "driver.version", "driver.version.data", "driver.version.internal", "input.sensitivity",
			"ups.beeper.status", "ups.mfr","ups.model", "ups.serial", "ups.status", "ups.test.result", "ups.firmware", "ups.firmware.aux","ups.mfr.date", "ups.productid",
            "driver.parameter.port", "driver.parameter.syncronous"]

p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

for line in p.stdout.readlines(): #read and store result in log file
    line = line.decode("utf-8").rstrip()
    key = line[:line.find(":")]
    value = line[line.find(":")+2:]

    if key in measurements:
        if key in string_measurements:
            value = '"' + value + '"'
        measurement = key + "=" + value
        if output != "":
            measurement = "," + measurement
        output += measurement

output = "ups_nut " + output.rstrip()
print(output, end='')