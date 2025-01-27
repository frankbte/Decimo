
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