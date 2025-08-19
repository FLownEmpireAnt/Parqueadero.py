from datetime import datetime

vehiculos = []
capacidad_maxima = 10
tarifas = {'carro':3000, 'moto':2000}

def hay_espacio():
    return len(vehiculos) < capacidad_maxima
def esta_registrado(placa):
    return any(v['placa'] == placa for v in vehiculos)

def registrar_entrada():
    if not hay_espacio():
        print("EL parqueadero no tiene espacio")
        return
    placa = input("Placa: ").upper()
    if esta_registrado(placa):
        print("Vehículo ya registrado")
        return
    tipo = input("Tipo (Carro/Moto): ").lower()
    hora_entrada = input("Hora entrada (HH:MM): ")
    vehiculos.append({
        "placa": placa,
        "tipo": tipo,
        "hora_entrada": hora_entrada,
        "hora_salida": None
    })
    print("Vehículo registrado con éxito")

from datetime import datetime

def registrar_salida():
    placa = input("Placa salida: ").upper()
    for v in vehiculos:
        if v["placa"] == placa:
            hora_salida = input("Hora salida (HH:MM): ")
            fmt = "HH:MM"
            t1 = datetime.strptime(v["hora_entrada"], fmt)
            t2 = datetime.strptime(hora_salida, fmt)
            horas = max(int((t2 - t1).total_seconds() // 3600), 1)
            tarifa = tarifas.get(v["tipo"], 0) * horas
            print(f"Tiempo: {horas} hora(s), Tarifa: ${tarifa}")
            vehiculos.remove(v)
            return
    print("Vehículo no encontrado")

def mostrar_vehiculos():
    if not vehiculos:
        print("No hay vehículos estacionados.")
        return
    for v in vehiculos:
        print(f"{v['placa']} - {v['tipo']} - Entrada: {v['hora_entrada']}")

def menu():
    while True:
        print("\n1. Registrar entrada\n2. Registrar salida\n3. Mostrar vehículos\n4. Salir")
        opc = input("Opción: ")
        if opc == "1":
            registrar_entrada()
        elif opc == "2":
            registrar_salida()
        elif opc == "3":
            mostrar_vehiculos()
        elif opc == "4":
            break
        else:
            print("Opción inválida")

menu()

