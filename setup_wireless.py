import os
import sys

def setup_monitor( iface):
    print("Setting up sniffing options... ")
    os.system('ifconfig ' + iface + 'down')
    try:
        os.system('iwconfig ' + iface + ' mode monitor ')
    except:
        print("Failed to setup your interface in monitor mode")
        sys.exit(1)
    os.system('ifconfig ' + iface + 'up')
    return iface
