from Simulador import Simulador
from Fila import Fila

capacity = 3
servers = 2 
arrival_interval = (1, 4)
service_interval = (3, 4)

capacity2 = 5  
servers2 = 1 
service_interval2 = (2, 5)

fila1 = Fila(capacity, servers, arrival_interval, service_interval)

fila2 = Fila(capacity, servers2, None, service_interval2)

fila3 = Fila(capacity, servers2, None, service_interval2)

fila4 = Fila(capacity, servers2, None, service_interval)

simulador = Simulador()
simulador.filas = [fila1, fila2, fila3, fila4]

simulador.run()