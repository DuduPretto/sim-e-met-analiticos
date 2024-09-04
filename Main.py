from Simulador import Simulador
from Fila import Fila

capacity = 2  
servers = 2 
arrival_interval = (2, 5)
service_interval = (3, 5)

fila = Fila(capacity, servers, arrival_interval, service_interval)

simulador = Simulador()
simulador.fila = fila

simulador.run()