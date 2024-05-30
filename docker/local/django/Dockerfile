#
FROM python:3.12-slim-bookworm AS python

# ES UNA INSTRUCCIÓN DE DOCKER QUE INICIALIZA UNA NUEVA ETAPA DE CONSTRUCCIÓN Y ESTABLECE
# LA IMAGEN BASE PARA INSTRUCCIONES POSTERIORES.

# BUILD STAGE 1
FROM python AS python-build-stage

ARG BUILD_ENVIRONMENT=local

# SE INTALAN LAS DEPENDENCIAS APT DE PYTHON
RUN apt-get update && apt-get install --no-install-recommends -y \
  # DEPENDENCIES FOR BUILDING PYTHON PACKAGES
  build-essential \
  libpq-dev

# SE COPIAN Y CREA LA CARPETA DE LOS ARCHIVOS DE REQUERIMIENTOS AL CONTENEDOR
COPY ./requirements .

# SE INSTALAN PAQUETES PRECOMPILADOS DE PYTHON
RUN pip wheel --wheel-dir /usr/src/app/wheels  \
  -r ${BUILD_ENVIRONMENT}.txt


# BUILD STAGE 2
# PYTHON 'run' STAGE
FROM python AS python-run-stage

ARG BUILD_ENVIRONMENT=local
ARG APP_HOME=/app

# PYTHONUNBUFFERED 1: NO BUFFEREA LA SALIDA DE LA CONSOLA
ENV PYTHONUNBUFFERED 1
# PYTHONDONTWRITEBYTECODE 1: NO GENERA ARCHIVOS .PYC
ENV PYTHONDONTWRITEBYTECODE 1

ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

# SE INSTALAN LAS DEPENDENCIAS Y UTILS DE APT PARA EL CONTENEDOR
RUN apt-get update && apt-get install --no-install-recommends -y \
  sudo git bash-completion nano ssh

# SE CREA GRUPO Y USUARIO DE CONTENEDOR
# CREAR UN USUARIO NO ROOT CON PRIVILEGIOS DE SUDO
RUN groupadd --gid 1000 dev-user \
  && useradd --uid 1000 --gid dev-user --shell /bin/bash --create-home dev-user \
  && echo dev-user ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/dev-user \
  && chmod 0440 /etc/sudoers.d/dev-user

# INSTALAR DEPENDENCIAS DEL SISTEMA NECESARIAS
RUN apt-get update && apt-get install --no-install-recommends -y \
  # psycopg dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# All absolute dir copies ignore workdir instruction.
# All relative dir copies are wrt to the workdir instruction
# copy python dependency wheels from python-build-stage
COPY --from=python-build-stage /usr/src/app/wheels  /wheels/

# USE WHEELS TO INSTALL PYTHON DEPENDENCIES
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
  && rm -rf /wheels/


COPY ./docker/local/django/entrypoint /entrypoint
# ENSURE THAT THE FILE USES UNIX-STYLE LINE ENDINGS (LF) INSTEAD
# OF WINDOWS-STYLE LINE ENDINGS (CRLF).
RUN sed -i 's/\r$//g' /entrypoint
# ENSURE THAT THE FILE IS EXECUTABLE
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# SE COPIAN LOS ARCHIVOS DE LA APLICACIÓN AL CONTENEDOR
COPY . ${APP_HOME}

ENTRYPOINT ["/entrypoint"]