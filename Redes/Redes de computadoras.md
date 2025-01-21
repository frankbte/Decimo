
# Modelo TCP/IP

## Capa Host

## Capa Internet

* Permite que los hosts envíen paquetes por cualquier red y que viajen independientemente del destinatario
* No hay garantía de que se mantenga el orden
* Esta capa define el protocolo Internet y el formato del paquete que se intercambia es el paquete IP

## Capa Transporte
* Permite que las contrapartes conversen
* Se definen 2 protocolos: 
  * **Transmission control Protocol**: Protocolo confiable orientado a conexión y libre de errores.
  * **User datagram Protocol**: No confiable y orientado a sin conexión. No hay orden en le entrega y es muy útil en aplicaciones tipo request-reply