FROM jupyterhub/jupyterhub

ARG PASSWORD="devops"
ARG USER="admin"

RUN conda install -y notebook
RUN useradd -m -s /bin/bash "${USER}" && \
    echo "${USER}:${PASSWORD}"|chpasswd

WORKDIR /srv/jupyterhub/

RUN jupyterhub --generate-config

CMD ["jupyterhub","-f","/srv/jupyterhub/jupyterhub_config.py"]
