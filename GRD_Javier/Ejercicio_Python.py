# Ejercicio 1.4 - Encontrar nombre del servicio por puerto y protocolo

import socket

def find_service_name():
    print("🔹 Servicios TCP:")
    protocolname = 'tcp'
    for port in [80, 25, 143]:
        try:
            service = socket.getservbyport(port, protocolname)
            print(f"Puerto: {port} => Servicio: {service}")
        except OSError:
            print(f"Puerto: {port} => Servicio no encontrado")

    print("\n🔹 Servicios UDP:")
    protocolname = 'udp'
    for port in [53, 110, 443]:
        try:
            service = socket.getservbyport(port, protocolname)
            print(f"Puerto: {port} => Servicio: {service}")
        except OSError:
            print(f"Puerto: {port} => Servicio no encontrado")

if __name__ == '__main__':
    find_service_name()