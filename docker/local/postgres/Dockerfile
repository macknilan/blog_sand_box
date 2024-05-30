FROM docker.io/postgres:16

# Copiar el directorio 'mantenimiento' del directorio local 'docker/local/postgres'
# al directorio '/usr/local/bin/maintenance' en la imagen.
# Este directorio contiene scripts que se utilizan para tareas de mantenimiento de bases de datos.
COPY ./docker/local/postgres/maintenance /usr/local/bin/maintenance
RUN chmod +x /usr/local/bin/maintenance/*
# Mueve todos los archivos del directorio '/usr/local/bin/maintenance' al directorio '/usr/local/bin'.
# Esto hace que los scripts estén disponibles en el PATH, para que puedan ejecutarse desde cualquier ubicación.
# Luego, elimine el directorio ahora vacío '/usr/local/bin/maintenance'.
RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
  && rmdir /usr/local/bin/maintenance
