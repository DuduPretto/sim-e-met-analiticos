from Simulador import Simulador
from Fila import Fila

capacity = 3
servers = 2 
arrival_interval = (1, 4)
service_interval = (3, 4)

capacity2 = 5  
servers2 = 1 
service_interval2 = (2, 3)

fila1 = Fila(capacity, servers, arrival_interval, service_interval)

fila2 = Fila(capacity2, servers2, None, service_interval2)

simulador = Simulador()
simulador.fila1 = fila1
simulador.fila2 = fila2

simulador.run()