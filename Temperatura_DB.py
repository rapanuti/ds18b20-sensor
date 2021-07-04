#!/usr/bin/env python
import os
import glob
import time
import datetime
from datetime import date
import MySQLdb
import numpy
from numpy import *
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')



def sensor():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20

def sensor2():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20

def read(ds18b20):
    location = '/sys/bus/w1/devices/+direccion de carpeta+/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    farenheit = (celsius * 1.8) + 32
    return celsius, farenheit

def read2(ds18b20):
    location = '/sys/bus/w1/devices/+direccion de carpeta+/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    farenheit = (celsius * 1.8) + 32
    return celsius, farenheit

def loop(ds18b20):
    while True:
        if (ds18b20) != None:
            
                    
            db = MySQLdb.connect(host="localhost",user="usuario", passwd="contrasena",db="basededatos") #conecta con  MySQL/MariaDB
            cur = db.cursor() #crea el cursor para las peticiones de  MySQL/MariaDB            
            print ("Temperatura Actual 28-3c01d0758c8e : %0.3f C" % read(ds18b20)[0])
            print ("Temperatura Actual 28-3c01d0758ae7  : %0.3f C" % read2(ds18b20)[0])
           
            dato1 = array([read(ds18b20)[0]])
            dato2 = array([read2(ds18b20)[0]])
            #print("dato1 %0.3f" %dato1)
            #print("dato2 %0.3f" %dato2)

         
            cur.execute('''INSERT INTO data2(temperatura) VALUES(%s);''', dato1  )
            cur.execute('''INSERT INTO data3(temperatura) VALUES(%s);''', dato2  )
            db.commit()
            dato1 = array(0)
            dato2 = array(0)
            #print("dato1 %0.3f" %dato1)
            #print("dato2 %0.3f" %dato2)
            time.sleep(5)
  
      


    

def kill():
    quit()

if __name__ == '__main__':
    try:
        serialNum = sensor()
          loop(serialNum)

     
    except KeyboardInterrupt:
        kill()
