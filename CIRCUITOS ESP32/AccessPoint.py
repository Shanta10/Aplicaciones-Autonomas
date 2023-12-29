import network

ap_if = network.WLAN(network.AP_IF)
ap_if.config(essid="Santiago")
ap_if.config(authmode=2, password="LazoMelendres1")
ap_if.config(max_clients=2)
ap_if.config(channel=10)
ap_if.config(hidden=0)
ap_if.active(True)

print("ESSID:", ap_if.config('essid'))
print("Configuracion de red (IP/netmask/gw/DNS):", ap_if.ifconfig())
print("Modo de autentificacion:", ap_if.config("authmode"))
print("Nº maximo de clientes:", ap_if.config("max_clients"))
print("Canal:", ap_if.config("channel"))
print("Oculta (True=Si / False=No):", ap_if.config("hidden"))
print("Activa (True=Si / False=No)", ap_if.active())