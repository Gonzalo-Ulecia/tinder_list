
# -------------------------
# Responsabilidad del Usuario:
# - Este programa tiene un propósito educativo.
# - El autor del programa no se hace responsable del mal uso.
# - Cada usuario es responsable de sus propias acciones al ejecutar este código.
# -------------------------

# -------------------------
# User Responsibility:
# - This program is for educational purposes.
# - The creator of the program is not responsible for misuse.
# - Each user is responsible for their own actions when running this code.
# -------------------------
#
# Author: Gonzalo Ulecia
# _________________________


import requests
import threading
import sys
import signal

NUM_THREADS = 4 #NUMERO DE HILOS (MODIFICAR A GUSTO DEL CONSUMIDOR ;) )

#request_get: Realiza GET request a tinder.com/@{username} <--- Usuario pasado por parámetro 
def request_get(username):
	try:
		url = f"https://www.tinder.com/@{username}"
		get_request = requests.get(url)
		return get_request.text
	except Exception as e:
		print(f"Error durante la peticion")

#search_username: llama a request_get recupera la respuesta y busca la cadena "search" dentro de la respuesta
def search_username(username):
	response = request_get(username) #Realiza la petición get y recupera la respuesta

	search ='"@type":"Person","name":"'   #Cadena dentro de las respuestas con usuario válido (usuario en tinder)

	if search in response: #Si se encuentra la cadena dentro de la respuesta recogida en el GET (es porque el usuario es válido)
		#Buscamos el nombre asociado al username
		position_name = response.find(search)+len(search)
		position_name_end = 0
		for i in range(50):
			if response[position_name+i] == '"':
				position_name_end = position_name+i
				break
		#Imprimimos el username y el nombre
		print("-----------------------------------------------------------------")
		print("\t@"+username+": "+response[position_name:position_name_end])


run = True #Flag que nos permitirá finalizar el hilo
run_lock = threading.Lock()  #Bloqueo para sincronizar el acceso a memoria compartida entre hilos ;)

#thread_search: inicializa las peticiones en un rango (esto nos permitirá lanzar varios hilos simultaneos)
def thread_search(names):
	for name in names:
		#Sincronizando el acceso comprobamos que el flag no sea False
		#si es False terminamos la ejecución del bucle y del hilo de forma ordenada
		with run_lock:
			if not run:
				break
		search_username(name.strip())

threads = [] #Array que contendrá los hilos

#Cerrada del programa Ctrl + C
def close_program(sig,frame):
	global run
	run = False
	sys.exit(0)
signal.signal(signal.SIGINT, close_program)


#Start point del programa

#Cabecera---------------------------------------------------------
tinder_list_header = """
  _______             __                 ___   _   __________
 |__   __(_)         / / ____            | |  (_) _|___   ___|
    | |   _______ ___| |/  _ `1_____     | |   _ / ___|| |
    | |  | / ___ /  _  |  |_| / ___| __  | |  | || \\__ | |
    | |  | | | ||  |_| |  ===| /    |__| | |__|_|_\\__ \\| |
    |_|  |_| | ||______|_____|_|         |_____||_____/|_|

_______________________________________\033[94mAuthor: Gonzalo Ulecia

"""

print("\033[95m"+tinder_list_header+"\033[00m")
print("\033[94mSearching users in tinders using wordlist...\033[00m")
#------------------------------------------------------------------

# Validar la cantidad de argumentos
if len(sys.argv) != 2:
	print("Uso: python3 programa.py [wordlist]")
	print("Ejemplo: python3 programa.py diccionario.txt")
	sys.exit(1)

#Abrimos el diccionario
lines = []
with open(str(sys.argv[1]),'r',encoding='utf-8', errors='ignore') as wordlist:
        lines = wordlist.readlines()


#Calculamos cuantos nombres procesará cada hilo
list_size = len(lines) // NUM_THREADS
names_div = [lines[i:i+list_size] for i in range(0, len(lines), list_size)]

#Iniciamos los hilos
for names in names_div:
	thread = threading.Thread(target=thread_search, args=(names,))
	thread.start()
	threads.append(thread)
#Esperamos q que terminen los hilos
for thread in threads:
	thread.join()
#Final del programa
print("FINALIZADO")
