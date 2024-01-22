import os
def checkpacketloss(destination_ip):
    packetloss = os.popen ("ping -c 5 " +destination_ip+ " | grep -oP '\d+(?=% packet loss)' ").read()
    return packetloss
print (checkpacketloss("192.168.111.235"),'is packet loss value')  