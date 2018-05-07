import wmi
import os, sys
import time
c = wmi.WMI ()
##get disk free
for interface in c.Win32_LogicalDisk ():
    tmpdict = {}
    tmplist = []
    tmpdict["a"] = interface.DeviceID
    tmpdict["Size"] = int(interface.Size) / 1024 / 1024 / 1024
    tmplist.append(tmpdict)
    print (tmplist)



