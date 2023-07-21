FROM maven:3.9.2-eclipse-temurin-20-alpine
WORKDIR /workspace

VOLUME /workspace/workdir

ENV SDKMAN_DIR=/root/.sdkman
ENV PATH="$PATH:$SDKMAN_DIR/bin"

RUN apk add zip unzip jq

COPY project_env.json project_env.json


RUN curl -s "https://get.sdkman.io" | bash && \
    echo "sdkman_auto_answer=true" > $SDKMAN_DIR/etc/config && \
    echo "sdkman_auto_selfupdate=false" >> $SDKMAN_DIR/etc/config

RUN PROJECT_CONFIG=$(cat /workspace/project_env.json) && \
    PROJECT_NAME=$(echo $PROJECT_CONFIG | jq -r '.projectName') && \
    PACKAGE_NAME=$(echo $PROJECT_CONFIG | jq -r '.packageName') && \
    bash -c "source $SDKMAN_DIR/bin/sdkman-init.sh && sdk install springboot && \
    source $SDKMAN_DIR/bin/sdkman-init.sh"

RUN mkdir workdir

ENTRYPOINT ["/bin/bash", "-c", "source $SDKMAN_DIR/bin/sdkman-init.sh && \"$@\"", "-s"]

CMD ["sdk", "help"]


