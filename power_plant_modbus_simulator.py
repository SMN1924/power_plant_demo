#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 09:54:56 2021

@author: qqdq
"""

#!/usr/bin/env python
from pymodbus.version import version
from pymodbus.server.sync import StartTcpServer
from pymodbus.server.sync import StartTlsServer
from pymodbus.server.sync import StartUdpServer
from pymodbus.server.sync import StartSerialServer

from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSparseDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

from pymodbus.transaction import ModbusRtuFramer, ModbusBinaryFramer
import time
from threading import Thread
import random
# --------------------------------------------------------------------------- #
# configure the service logging
# --------------------------------------------------------------------------- #
import logging
FORMAT = ('%(asctime)-15s %(threadName)-15s'
          ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)



def data_change(name,s):
    a = 0
    while True:
        data = [a]*150
        for k in range(0,6,1):
            #voltage 1-16
            data[0+20*k] = int(315 + random.random()*30)
            data[1+20*k] = int(315 + random.random()*30)
            data[2+20*k] = int(315 + random.random()*30)
            data[3+20*k] = int(315 + random.random()*30)
            data[4+20*k] = int(315 + random.random()*30)
            data[5+20*k] = int(315 + random.random()*30)
            data[6+20*k] = int(315 + random.random()*30)
            data[7+20*k] = int(315 + random.random()*30)
            data[8+20*k] = int(315 + random.random()*30)
            data[9+20*k] = int(315 + random.random()*30)
            data[10+20*k] = int(315 + random.random()*30)
            data[11+20*k] = int(315 + random.random()*30)
            data[12+20*k] = int(315 + random.random()*30)
            data[13+20*k] = int(315 + random.random()*30)
            data[14+20*k] = int(315 + random.random()*30)
            data[15+20*k] = int(315 + random.random()*30)
            #operating voltage, temperature, open circuit voltage, status
            data[16+20*k] = int(330 + random.random()*20)
            data[17+20*k] = int(2000 + random.random()*100)
            data[18+20*k] = int(350 + random.random()*20)
            data[19+20*k] = int(random.random())
        for m in range(0,2,1):
            #status, manual voltage
            data[120+10*m] = int(20 + random.random()*2)
            data[121+10*m] = int(20 + random.random()*2)
            data[122+10*m] = int(10 + random.random()*2)
            data[123+10*m] = int(random.random())
            data[124+10*m] = int(220 + random.random()*20)
            data[128+10*m] = int(0)
            data[129+10*m] = int(0)
        s.setValues(3,0,data)
        time.sleep(1)

def run_server():
    slave1 = ModbusSlaveContext(hr=ModbusSequentialDataBlock(0, [0]*150))
    slaves = {}
    for i in range(1,2):
        slaves[i] = slave1
    context = ModbusServerContext(slaves=slaves, single=False)
    t1 = Thread(target=data_change,args=("thread-1",slave1))
    t1.start()
    StartTcpServer(context, address=("", 505))
    t1.join()


if __name__ == "__main__":
    run_server()
