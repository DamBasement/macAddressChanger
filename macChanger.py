#!/usr/bin/env python
import subprocess
import optparse
import re

#
# GETTING PARAMETERS
#####################
def getting_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC address")
    parser.add_option("-m","--mac",dest="macAddress",help="new MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface. Type --help for info")
    elif not options.macAddress:
        parser.error("[-] Please specify a new mac. Type --help for info")
    return options
#
# CHANGE MAC ADDRESS
#####################
def change_macAddress(interface, macAddress):
    print("[+] Changing Mac address to "+ macAddress +" for " + interface)

    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",macAddress])
    subprocess.call(["ifconfig",interface,"up"])
    subprocess.call(["ifconfig",interface])
#
# GETTING CURRENT MAC ADDRESS
#############################
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
    macAddressSearchResult = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if macAddressSearchResult:
        return (macAddressSearchResult.group(0))
    else:
        print("[-] cannot get MAC address!")
#
# CHECK CHANGES
###############
def check_changes():
    currentMac = get_current_mac(options.interface)
    if currentMac == options.macAddress:
        print("[+] MAC Address changed succesfully.")
    else:
        print("[-] MAC Address did not change.")

options = getting_arguments()
currentMac = get_current_mac(options.interface)
print ("Current MAC is " + str(currentMac))
change_macAddress(options.interface,options.macAddress)
check_changes()
