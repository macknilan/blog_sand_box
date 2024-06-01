#!/usr/bin/env bash

# FUNCIÓN PARA SOLICITAR CONFIRMACIÓN

yes_no(){
  # SE DECLARA LA VARIABLE `desc` PARA ALMACENAR EL MENSAJE DE CONFIRMACIÓN
  declare desc="Solicitud de confirmation. \$\"\{1\}\": mensaje de confirmation"
  # Se declara una variable local 'arg1' y se le asigna el primer argumento pasado a la función.
  local arg1="${1}"
  # Se declara una variable local 'response' y se utiliza el comando 'read' para obtener la entrada del usuario.
  # El comando 'read' se utiliza con la opción '-r' para evitar que se interpreten las barras invertidas.
  # La opción '-p' se utiliza para mostrar un mensaje al usuario antes de leer la entrada.
  local response= read -r -p "${arg1} (y/[n])? " response
  # Uso de la sentencia `if` para verificar si la respuesta del usuario coincide con 'Y' o 'y'.
  if [[ "${response}" =~ ^[Yy]$ ]]

  then
    exit 0
  else
    exit 1
  fi
}