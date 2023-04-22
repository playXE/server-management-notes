#!/usr/bin/python
# Forwards host port to VM port, specify VM address and port through command line: 
# python forward_host_to_vm.py <interface> <VM address> <host port> <VM port> 
# Uses iptables to forward host port to VM port

import sys
import os

if len(sys.argv) != 5:
    print("Usage: python forward_host_to_vm.py <VM address> <VM port>")
    sys.exit(1)

interface = sys.argv[1]
vm_address = sys.argv[2]
host_port = sys.argv[3]
vm_port = sys.argv[4]


os.system("iptables -A PREROUTING -t nat -i " + interface + " -p tcp --dport " + host_port + " -j DNAT --to-destination " + vm_address + ":" + vm_port)
os.system("iptables -A FORWARD -p tcp -d " + vm_address + " --dport " + vm_port + " -j ACCEPT")
