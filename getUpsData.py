#!/usr/bin/env python3

import subprocess

cmd="upsc Fortron@localhost"

output=""
tag_output=""

measurements=["battery.charge","battery.voltage","battery.voltage.high","battery.voltage.low","battery.voltage.nominal","device.type","driver.name","driver.parameter.pollinterval","driver.parameter.port","driver.parameter.productid",
              "driver.parameter.synchronous","driver.parameter.vendorid","driver.version","driver.version.internal","input.current.nominal","input.frequency","input.frequency.nominal","input.voltage","input.voltage.fault",
              "input.voltage.nominal","output.voltage", "ups.beeper.status", "ups.delay.shutdown","ups.delay.start","ups.load","ups.productid","ups.status","ups.temperature","ups.type","ups.vendorid"]

string_measurements=["device.type","driver.name","driver.parameter.port","driver.parameter.productid","driver.parameter.synchronous","driver.parameter.vendorid","driver.version","driver.version.internal",
                     "ups.beeper.status","ups.productid","ups.status","ups.type","ups.vendorid"]

p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

for line in p.stdout.readlines():
    line = line.decode("utf-8").rstrip()
    key = line[:line.find(":")]
    value = line[line.find(":")+2:]

    if key in measurements and key in string_measurements:
        value = value.replace(" ", "_")
        tag = key + "=" + value
        if tag_output != "":
            tag = "," + tag
        tag_output += tag
    if key in measurements and key not in string_measurements:
        measurement = key + "=" + value
        if output != "":
            measurement = "," + measurement
        output += measurement

output = "ups_nut," + tag_output.rstrip() + " " + output.rstrip()
print(output, end='')
