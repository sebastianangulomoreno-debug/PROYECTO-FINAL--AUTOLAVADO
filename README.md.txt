# Autolavado y Detallado "Rápido y Limpio"

Este proyecto es una aplicación de escritorio interactiva desarrollada en **Python** utilizando **Tkinter** para la interfaz gráfica. El sistema permite gestionar los registros de los vehículos atendidos en un autolavado durante el día, calcular los costos acumulados, evitar registros duplicados por placa y generar reportes financieros al cerrar la jornada.

## Integrantes del Proyecto
* Karoll Daniela Monsalve Grajales
* Sebastian Angulo Moreno
## Curso:
* Programación imperativa
## Institución:
* Universidad del Valle - Sede Buga

---

## Requisitos de Diseño Avanzados

Para cumplir de forma estricta con las pautas académicas del curso, la arquitectura del software se divide bajo reglas rigurosas:

1. Ausencia Absoluta de Ciclos (`for` / `while`): Todo el procesamiento de los datos acumulados se realiza bajo el paradigma de programación funcional y recursividad pura.
2. Rebanado de Listas (`[1:]`): Las funciones recursivas procesan de forma unitaria el primer elemento de la base de datos temporal en memoria y avanzan dividiendo el resto de la lista hasta alcanzar la condición de parada (Caso Base).
3. Estructuras Flexibles: La base de datos local funciona mediante una lista dinámica compuesta por diccionarios para modelar las propiedades individuales de cada vehículo.

---

## Estructura del Núcleo Recursivo

El archivo contiene tres algoritmos principales de recursión que puedes defender ante cualquier evaluación:

1. calcular_recaudo_diario(lista): Suma de forma recursiva la tarifa base y los adicionales aplicados a cada vehículo. Devuelve 0 si la lista está vacía.

2. buscar_vehiculo_por_placa(lista, placa): Recorre la pila de datos comparando las cadenas de texto. Si encuentra coincidencia retorna True inmediatamente deteniendo el flujo, evitando que ingresen placas duplicadas a la bahía de lavado.

3. contar_vehiculos_categoria(lista, categoria): Filtra y añade 1 al contador interno de la función cada vez que detecta un tipo específico de vehículo ("Automóvil", "Camioneta" o "Moto")

---

## Requisitos del Sistema y Dependencias

El sistema utiliza componentes nativos del lenguaje, pero requiere una librería externa exclusivamente para el procesamiento y conversión del archivo gráfico (`.jpeg` a `.png`) en sistemas operativos Linux o macOS:

* Python 3.10 o superior
* Pillow (PIL): Librería para el tratamiento automatizado de imágenes en Python.

---

## 💻 Instrucciones de Instalación y Ejecución (Multiplataforma)

El sistema es totalmente compatible con Windows, macOS y Linux. Asegúrate de abrir la terminal o el símbolo del sistema en la carpeta exacta del proyecto (`/proyectoFinal`) donde conviven tu script `Autolavado.py` y el logo `logoAutolavado.jpeg`.

### 1. Preparar el Entorno (Paso Único)
Para garantizar que el logotipo se procese de forma nativa en cualquier sistema operativo, abre tu terminal y ejecuta el comando correspondiente a tu entorno:

* En Windows (CMD / PowerShell):
  ```cmd
  pip install pillow

* En macOs / Linux (terminal):

  pip install pillow

---

## Métodos de Ejecución

Elige el método que te resulte más cómodo según tu sistema operativo:

* Método Universal (Desde la Terminal)
Es el método más seguro para ingenieros. Escribe el comando adecuado y presiona Enter:

1. En Windows:

python Autolavado.py

2. En macOS / Linux:

python3 Autolavado.py

* Método Rápido (Doble Clic - Sin Consola)
Si no quieres escribir comandos cada vez que uses la aplicación, puedes lanzarla directamente de forma visual:

1. En Windows: Haz doble clic directamente sobre el archivo Autolavado.py. Si tienes Python bien configurado, la ventana del autolavado se abrirá inmediatamente.

2. En macOS: Puedes hacer clic derecho sobre Autolavado.py, seleccionar Abrir con y elegir Python Launcher.

3. En Linux: Asegúrate de dar permisos de ejecución al archivo (chmod +x Autolavado.py), haz clic derecho y selecciona Ejecutar como un programa.

---

## Análisis de Flujo y Mecánica de la Lógica Recursiva

El diseño del sistema sustituye por completo los paradigmas iterativos tradicionales mediante una estrategia de control basada en la pila de llamadas (Call Stack) de Python. Su funcionamiento se rige bajo los siguientes pilares de la ciencia de la computación:

1. Mecanismo de Reducción por Rebanado (Splitting): En lugar de utilizar punteros o índices incrementales, cada llamada recursiva consume la cabeza de la estructura (lista_vehiculos[0]) y le delega el resto del cuerpo (lista_vehiculos[1:]) a la siguiente instancia de la misma función. Esto garantiza una reducción progresiva del tamaño de los datos en cada paso del ciclo recursivo.

2. Evaluación Cortocorticuitada en Búsquedas: La función buscar_vehiculo_por_placa implementa dos casos base. Si el elemento inspeccionado coincide con la placa buscada, la función retorna True inmediatamente. Esto destruye la pila de llamadas pendientes y detiene el recorrido sin necesidad de evaluar el resto de la lista, optimizando el tiempo de ejecución en memoria.

3. Doble Ramificación Condicional en Conteo: A diferencia de una suma simple, la función contar_vehiculos_categoria evalúa el estado del vehículo actual antes de decidir su siguiente paso en la pila. Si el tipo coincide, la función se autoevalúa sumando un 1 al retorno (1 + función(...)); si no coincide, se salta el elemento actual y continúa el flujo directo hacia los elementos restantes en el array.

4. Garantía de Finalización (Caso Base): Para prevenir desbordamientos de memoria (Stack Overflow), todas las funciones del núcleo lógico validan como primera instrucción si la longitud de la lista ha llegado a cero (len(lista_vehiculos) == 0). Al cumplirse esta condición, la función retorna un valor neutro (0 o False), permitiendo que todas las llamadas acumuladas en la pila se resuelvan en cascada de manera limpia y segura.