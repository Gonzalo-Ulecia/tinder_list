# Tinder List

## Descripción

Tinder List Checker es una herramienta de código abierto basada en OSINT que permite verificar la existencia de usuarios en Tinder utilizando un diccionario de nombres de usuario. Esta herramienta está diseñada con fines educativos y se debe utilizar de manera ética y legal. El autor de la herramienta no asume ninguna responsabilidad por su mal uso.

**Responsabilidad del Usuario:**
- Este programa es solo para fines educativos.
- El autor del programa no se hace responsable del mal uso.
- Cada usuario es responsable de sus propias acciones al ejecutar este código.

## Instalación

Antes de usar la herramienta, asegúrate de tener la biblioteca `requests` instalada. Puedes instalarlo ejecutando el siguiente comando:

```bash
pip install requests
```

## Modo de Uso

Para utilizar Tinder List Checker, sigue estos pasos:

1. Clona el repositorio o descarga el archivo `tinder_list.py` en tu máquina.

2. Abre una terminal y navega al directorio donde se encuentra el archivo `tinder_list.py`.

3. Ejecuta el siguiente comando para iniciar la búsqueda de usuarios en Tinder:

```bash
python3 tinder_list.py <wordlist>
```

## Nota Importante

El uso de Tinder List Checker es responsabilidad de cada usuario. Asegúrate de cumplir con las leyes y regulaciones locales, así como con las políticas de uso de Tinder. No utilices esta herramienta para violar la privacidad de otras personas sin su consentimiento.


## Ejemplo de uso (Entorno controlado)

### Entorno
Imaginemos que queremos recopilar informacion sobre una persona llamada Gonzalo.
Le gusta la ciberseguridad y creemos que esta involucrado con estafas usando redes sociales como instagram, twitter, tinder ...

### Creamos una cuenta en tinder para realizar la prueba
![Creación de una cuenta en tinder](/img/imagen1.jpg)

### Usamos tinder_list para verficar las cuentas
    Elaboramos un diccionario en un fichero llamado diccionario.txt

    ```bash
	gonzalo
	gonzalo_01
	gonzalo_02
	gonzalo1
	gonzalo2
	gonzalo3
	gonzalo4
	gonzalociberseguridad
	gonzalociber
	gonzalo_ciberseguridad
	...
	```
![Diccionario](/img/imagen2.jpg)
Ejecutamos tinder_list:
![Ejecución de tinder_list](/img/imagen3.jpg)

### Obtenemos información publica de la cuenta en tinder.com
![Verificamos informacion en tinder](/img/imagen4.jpg)