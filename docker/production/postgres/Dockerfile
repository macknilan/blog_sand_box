FROM docker.io/postgres:16

# Copiar el directorio `maintenance` del directorio local 'docker/local/postgres'
# al directorio '/usr/local/bin/maintenance' en la imagen.
# Este directorio contiene scripts que se utilizan para tareas de `maintenance` de bases de datos.
COPY ./docker/production/postgres/maintenance /usr/production/bin/maintenance
RUN chmod +x /usr/production/bin/maintenance/*
# Mueve todos los archivos del directorio '/usr/local/bin/maintenance' al directorio '/usr/local/bin'.
# Esto hace que los scripts estén disponibles en el PATH, para que puedan ejecutarse desde cualquier ubicación.
# Luego, elimine el directorio ahora vacío '/usr/local/bin/maintenance'.
RUN mv /usr/production/bin/maintenance/* /usr/production/bin \
  && rmdir /usr/production/bin/maintenance
