FROM mcr.microsoft.com/devcontainers/miniconda:1-3

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends python3-dev python3-pip default-libmysqlclient-dev build-essential

# Copy environment.yml (if found) to a temp location so we update the environment.
COPY .devcontainer/environment.yml* /tmp/conda-tmp/
RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yml; fi \
    && rm -rf /tmp/conda-tmp

# [Optional] Uncomment to install a different version of Python than the default
RUN conda install -y python=3.10 \
    && pip install --no-cache-dir pipx \
    && pipx reinstall-all

