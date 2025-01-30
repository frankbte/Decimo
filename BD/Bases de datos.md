
# Abstracción de datos

## Nivel físico:
- Describe como se almacena los datos en la memoria secundaria
## Nivel Lógico:
* Describe que datos ser almacenados en la base de datos y como se relacionan entre ellos.
## Nivel de vistas
* Describe las parte de la base de datos que es de interés para cierto topo de usuarios.

# Ejemplares y esquemas (diferencia)

### La información en una base de datos cambia a lo largo del tiempo

## Ejemplar de la base de datos
* Colección de información almacenada de la base de datos en un momento particular
## Esquema de la base de datos
* Es el diseño completo de la base de datos
* Esquema físico
* Esquema lógico
* Subesquemas

# Independencia física de los datos
* Los programas de aplicación muestran la independencia física de los datos si no dependen del esquema físico.
* Trabajamos en la capa lógica, el sistema de base de datos decide la manera en la que guarda los datos. 

# Modelo de los datos

## Colección de herramientas conceptuales para describir
* Los datos
* Las relaciones
* Las restricciones
## Categorías
* Modelos lógicos basados en registros
	* Modelo entidad - relación
	* Modelo relacional
* Modelos lógicos basados en objetos
* Modelos físicos


# Modelo entidad-relación

El mundo real que será implementado en el sistema se percibe como un conjunto de entidades de sus relaciones.

**Entidad** 
* Una cosa u objeto del mundo real que es distinguible de otros objetos: alumnos, profesores, salón de clase , etc.
* Las entidades se describen en una base de datos mediante un conjunto de atributos
	* Alumno
	* Profesor
	* Asignatura
**Relaciones**
* Describen una asociación entre entidades
	* Profesor imparte asignatura
	* Alumno toma asignatura