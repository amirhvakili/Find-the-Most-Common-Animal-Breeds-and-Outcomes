FROM apache/airflow:latest

USER airflow

RUN curl -fL https://github.com/coursier/coursier/releases/latest/download/cs-x86_64-pc-linux.gz | gzip -d > /home/airflow/cs \
    && chmod +x /home/airflow/cs \
    && /home/airflow/cs setup --yes --jvm temurin:17 \
    && echo 'export PATH="$HOME/.local/share/coursier/bin:$PATH"' >> ~/.profile

ENV PATH="/home/airflow/.local/share/coursier/bin:$PATH"
ENV JAVA_HOME="/home/airflow/.cache/coursier/arc/https/github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.19%252B10/OpenJDK17U-jdk_x64_linux_hotspot_17.0.19_10.tar.gz/jdk-17.0.19+10"