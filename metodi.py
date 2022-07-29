import socket

target = input('Inserisci l''ip da scansionare: ')
portrange = input('Inserisci l''intervallo della porta da scansionare: ')

lowport = int(portrange.split('-')[0])
highport = int(portrange.split('-')[1])

print('Scan di host ', target, ' dalla porta ', lowport, ' alla porta ', highport)

for port in range(lowport, highport +1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        status = s.connect_ex((target, port))
        if(status == 0):
                serviceName = socket.getservbyport(port)
                print('Porta', port, '- Aperta - Servizio:',serviceName)

        s.close()
