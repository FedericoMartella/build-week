import http.client


host = input('Inserisci IP del sistema target: ')
port = input(' Inserisci la porta del sistema target: ')

if(port == ""):
	port=80

try:
	print(" ")
	connection1 = http.client.HTTPConnection(host, port)
	connection1.request('OPTION','/phpMyAdmin/phpMyAdmin.html')
	response1 = connection1.getresponse()
	print('I metodi HTTP abilitati sono: ',response1.getheader('allow'))
	print(" ")
	connection1.close()

except ConnectionRefusedError:
	print("Connesione fallita")
