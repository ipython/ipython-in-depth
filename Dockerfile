FROM ubuntu:17.04

RUN apt-get update
RUN apt-get install --yes --no-install-recommends python3 python3-venv
RUN apt-get install --yes --no-install-recommends build-essential python3-dev
RUN apt-get install --yes r-base r-base-core r-recommended
RUN apt-get install --yes --no-install-recommends vim git
RUN apt-get purge && apt-get clean

RUN adduser --disabled-password --gecos "Default Jupyter user" jovyan

RUN mkdir -p /srv/venv && chown -R jovyan:jovyan /srv/venv

USER jovyan

RUN python3 -m venv /srv/venv
RUN /srv/venv/bin/pip3 install --upgrade pip wheel setuptools
RUN /srv/venv/bin/pip3 install --no-cache-dir notebook ipykernel jupyterhub
RUN /srv/venv/bin/pip3 install --no-cache-dir xonsh cffi_magic numpy pandas matplotlib
RUN /srv/venv/bin/pip3 install --no-cache-dir seaborn rpy2

ENV PATH /srv/venv/bin:$PATH

WORKDIR /home/jovyan
ADD . .
RUN rm -rf __pycache__
RUN rm -rf fabfile.py
RUN rm -rf pycon*

EXPOSE 8888

CMD jupyterhub-singleuser \
  --port=8888 \
  --ip=0.0.0.0 \
  --user="$JPY_USER" \
  --cookie-name=$JPY_COOKIE_NAME \
  --base-url=$JPY_BASE_URL \
  --hub-prefix=$JPY_HUB_PREFIX \
  --hub-api-url=$JPY_HUB_API_URL
