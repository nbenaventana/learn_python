from scapy.all import sniff, Dot11, Dot11ProbeReq

#def procesar_paquete(paquete):
#    paquete.show()  # Muestra detalles completos del paquete
#
## Sniff (captura) de paquetes en la red local
#sniff(filter="", prn=procesar_paquete)




def procesar_paquete(paquete):
    if paquete.haslayer(Dot11ProbeReq):
        mac_cliente = paquete.addr2
        ssid = paquete.info.decode("utf-8")
        print(f"Probe Request capturado de MAC: {mac_cliente} con SSID: {ssid}")

# Sniff (captura) de paquetes Wi-Fi en la red local
sniff(iface="wlp0s20f3", prn=procesar_paquete)
