ARG BASE_CONTAINER=spark:4.0.0-scala2.13-java17-python3-r-ubuntu
FROM $BASE_CONTAINER as spark
FROM spark as delta

USER root
ARG DELTA_SPARK_VERSION="4.0.0"
ARG DELTALAKE_VERSION="1.1.2"
ARG JUPYTERLAB_VERSION="4.4.5"
ARG PANDAS_VERSION="2.3.1"

RUN pip install --quiet --no-cache-dir delta-spark==${DELTA_SPARK_VERSION} \
deltalake==${DELTALAKE_VERSION} jupyterlab==${JUPYTERLAB_VERSION} pandas==${PANDAS_VERSION}
