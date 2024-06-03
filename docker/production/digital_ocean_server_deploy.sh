#!/bin/bash

if [ -z "$DIGITAL_OCEAN_IP_ADDRESS" ]
then
  echo "DIGITAL_OCEAN_IP_ADDRESS not defined"
  exit 0
fi

# El comando 'git archive' se utiliza para crear un archivo de los archivos de la rama,
# que en este caso es 'main'. La opción '--format' se utiliza para especificar el formato del
# archivo resultante, en este caso 'tar'. La opción '--output' se utiliza para especificar
# el nombre del archivo al que se escribirá el archivo, en este caso './project.tar'.
git archive --format tar --output ./project.tar main

echo 'SUBIENDO PROYECTO        ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===>'

# El comando 'rsync' se utiliza para sincronizar archivos y directorios de una ubicación a otra minimizando la
# transferencia de datos utilizando codificación delta cuando es apropiado.

# Una característica importante de rsync es que funciona con el "algoritmo de transferencia delta", lo que significa
# que solo enviará las diferencias entre los archivos fuente y los archivos existentes en el destino.

# './project.tar' es el archivo fuente en la máquina local.
# 'root@$DIGITAL_OCEAN_IP_ADDRESS:/tmp/project.tar' es el destino en la máquina remota.
# 'root@$DIGITAL_OCEAN_IP_ADDRESS' es el usuario y el host de la máquina remota.
# '/tmp/project.tar' es la ruta donde se copiará el archivo fuente en la máquina remota.
rsync ./project.tar root@$DIGITAL_OCEAN_IP_ADDRESS:/tmp/project.tar

echo ',.-~*´¨¯¨`*·~-.¸-(_    CARGA COMPLETADA    _)-,.-~*´¨¯¨`*·~-.'

echo 'CONSTRUCCIÓN DE LA IMAGEN ∙∙∙∙∙·  •͡˘㇁•͡˘'

ssh -i ~/.ssh/lab_to_do -o StrictHostKeyChecking=no root@$DIGITAL_OCEAN_IP_ADDRESS << 'ENDSSH'
  mkdir -p /app
  rm -rf /app/* && tar -xf /tmp/project.tar -C /app
  docker compose -f /app/production.yml up --build -d --remove-orphans
ENDSSH

echo 'Build completed successfully  \m/_(>_<)_\m/'