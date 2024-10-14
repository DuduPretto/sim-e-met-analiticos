from Simulador import Simulador
from Fila import Fila
import yaml

# capacity = 3
# servers = 2 
# arrival_interval = (1, 4)
# service_interval = (3, 4)

# capacity2 = 5  
# servers2 = 1 
# service_interval2 = (2, 5)

# fila1 = Fila(capacity, servers, arrival_interval, service_interval)

# fila2 = Fila(capacity, servers2, None, service_interval2)

# fila3 = Fila(capacity, servers2, None, service_interval2)

# fila4 = Fila(capacity, servers2, None, service_interval)
# simulador.filas = [fila1, fila2, fila3, fila4]

initialTime = 0
queues = []
network_transitions = {}

# simulador.run()

def fileReader():
    global initialTime, queues, network_transitions
    # Open the YAML file and load its content
    with open("model.yml", 'r') as file:
        data = yaml.safe_load(file)

    initialTime = data['arrivals']['Q1']

    for queue_name, attributes in data['queues'].items():
        servers = attributes.get('servers')
        capacity = attributes.get('capacity', None)  # Default to None if not available
        maxArrival = attributes.get('maxArrival', None)
        minArrival = attributes.get('minArrival', None)
        minService = attributes.get('minService')
        maxService = attributes.get('maxService')
        fila = Fila(queue_name, capacity, servers, (minArrival, maxArrival), (minService, maxService))
        queues.append(fila)

    for fila in queues:
        print("--------------------")
        fila.print()

    for transition in data['network']:
        source = transition['source']
        target = transition['target']
        probability = transition['probability']
        
        if source not in network_transitions:
            network_transitions[source] = {}
        
        network_transitions[source][target] = probability

    for queue in network_transitions.keys():
        sum = 0
        
        for target in network_transitions[queue]:
            sum += network_transitions[queue][target]
        if sum != 1:
            network_transitions[queue]["exit"] = 1 - sum

    print(network_transitions)
      

fileReader()

simulador = Simulador(queues, network_transitions, initialTime)

simulador.run()

