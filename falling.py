from __future__ import print_function

import time
import datetime
import grovepi
import grove_2smpb_02e

Pground = 1010.3
P0 = 1013.25
pow = 1.0 / 5.256

sensor = grove_2smpb_02e.Grove2smpd02e()
ledbar = 5

grovepi.pinMode(ledbar, "OUTPUT")
time.sleep(1)

def cal_height():
  press, temp = sensor.readData()
  height = ((P0 / press)**pow - (P0 / Pground)**pow) * (temp + 273.15) / 0.0065

  return height

def main():

    print("start")
    grovepi.ledBar_init(ledbar, 0)

    while True:
        height = cal_height()
        print(height = %.1f[m]" %(height))
        time.sleep(1)

if __name__ == '__main__':
  main()
