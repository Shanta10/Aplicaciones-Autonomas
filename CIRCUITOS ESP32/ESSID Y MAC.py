import network, ubinascii

ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)

print("ESSID:", ap_if.config('essid'))
print("Direccion MAC:", ubinascii.hexlify(ap_if.config('mac'), ':').decode())
