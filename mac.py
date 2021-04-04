#!/usr/bin/env python
import subprocess#тут импортируется модуль


subprocess.call("sudo ifconfig eth0 down", shell=True)#это подменяет mac-адрес сетевого интерфейса eth0
subprocess.call("sudo ifconfig eth0 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("sudo ifconfig eth0 up", shell=True)


subprocess.call("sudo ifconfig wlan0 down", shell=True)#это подменяет mac-адрес сетевого интерфейса wlan0
subprocess.call("sudo ifconfig wlan0 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("sudo ifconfig wlan0 up", shell=True)


subprocess.call("sudo ifconfig usb0 down", shell=True)#это подменяет mac-адрес сетевого интерфейса usb0
subprocess.call("sudo ifconfig usb0 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("sudo ifconfig usb0 up", shell=True)

