from __future__ import print_function

import time
import datetime
import grove_2smpb_02e
from light_progress.commandline import ProgressBar
from light_progress import widget

Pground = 1010.3
P0 = 1013.25
pow = 1.0 / 5.256

sensor = grove_2smpb_02e.Grove2smpd02e()

widgets = ['..HP..', widget.Num(), widget.Bar()]
hitpoint = ProgressBar(100, widgets=widgets)

def cal_height():
  press, temp = sensor.readData()
  height = ((P0 / press)**pow - (P0 / Pground)**pow) * (temp + 273.15) / 0.0065

  return height

def cal_damage(height):
  if height < 9:
    damage = 0
  elif height < 10:
    damage = 12
  elif height < 11:
    damage = 17
  elif height < 12:
    damage = 21
  elif height < 13:
    damage = 36
  elif height < 14:
    damage = 44
  elif height < 15:
    damage = 52
  elif height < 16:
    damage = 77
  elif height < 17:
    damage = 91
  else:
    damage = 100

  return damage

def HitpointBar(damage):
  hitpoint.start()
  hitpoint.update(100 - damage)
  hitpoint.finish()

def main():
    print("start")
    while True:
        height = cal_height()
        # print("height = %.1f[m]" % (height))
        damage = cal_damage(height)
        HitpointBar(damage)
        time.sleep(1)

if __name__ == '__main__':
  main()
