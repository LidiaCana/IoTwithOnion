#!/usr/bin/python
#autor: Lidia Canales
import sys
import signal
import onionGpio
from Conexion import*
from Conexion1 import*
from Conexion2 import*
from Conexion3 import*
from Conexion4 import*
from Conexion5 import*

gpioObj = onionGpio.OnionGpio(1)
gpioObj1 = onionGpio.OnionGpio(45)
gpioObj2 = onionGpio.OnionGpio(2)
gpioObj3 = onionGpio.OnionGpio(11)
gpioObj4 = onionGpio.OnionGpio(0)
gpioObj5 = onionGpio.OnionGpio(3)

status  = gpioObj.setOutputDirection(0)
status1 = gpioObj1.setOutputDirection(0)
status2 = gpioObj2.setOutputDirection(0)
status3 = gpioObj3.setOutputDirection(0)
status4 = gpioObj4.setOutputDirection(0)
status5 = gpioObj5.setOutputDirection(0)


def procesa(respuesta):
    print respuesta

    if respuesta:
        #led.on()
        status  = gpioObj.setValue(1)
        #print "Encendido"
    else:
        #led.off()
        status  = gpioObj.setValue(0)
        #print "Apagado"
    sys.stdout.flush()

def procesa1(respuesta1):
    print respuesta1
 if respuesta1:
        #led.on()
        status1 = gpioObj1.setValue(1)
        #print "Encendido_1"
    else:
        #led.off()
        status1 = gpioObj1.setValue(0)
        #print "Apagado_1"
    sys.stdout.flush()

def procesa2(respuesta2):
    print respuesta2

    if respuesta2:
        #led.on()
        status2 = gpioObj2.setValue(1)
        #print "Encendido_2"
    else:
        #led.off()
        status2 = gpioObj2.setValue(0)
        #print "Apagado_2"
    sys.stdout.flush()

def procesa3(respuesta3):
    print respuesta3

    if respuesta3:
        #led.on()
        status3 = gpioObj3.setValue(1)
        #print "Encendido_3"
    else:
        #led.off()
        status3 = gpioObj3.setValue(0)
        #print "Apagado_3"
    sys.stdout.flush()

def procesa4(respuesta4):
    print respuesta4

    if respuesta4:
        #led.on()
        status4 = gpioObj4.setValue(1)
 #print "Encendido_4"
    else:
        #led.off()
        status4 = gpioObj4.setValue(0)
        #print "Apagado_4"
    sys.stdout.flush()

def procesa5(respuesta5):
    print respuesta5

    if respuesta5:
        #led.on()
        status5 = gpioObj5.setValue(1)
        #print "Encendido_5"
    else:
        #led.off()
        status5 = gpioObj5.setValue(0)
        #print "Apagado_5"
    sys.stdout.flush()

try:
        print "Inicio"
        t = Conexion(procesa)
        t.daemon=True
        t.start()

        #t1 = Conexion1(procesa1)
        #t1.daemon=True
        #t1.start()

        #t2 = Conexion2(procesa2)
        #t2.daemon=True
        #t2.start()

        #t3 = Conexion3(procesa3)
        #t3.daemon=True
        #t3.start()

        #t4 = Conexion4(procesa4)
        #t4.daemon=True
        #t4.start()
  #t5 = Conexion5(procesa5)
        #t5.daemon=True
        #t5.start()
        signal.pause()

except (KeyboardInterrupt, SystemExit):
        raise
        print "Salida"
