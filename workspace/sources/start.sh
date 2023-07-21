#!/bin/bash

# Pour démarrer le conteneur
docker run -it --rm -v D:\ProjetCLI\test\:/workspace/workdir -w /workspace/workdir spring-workspace bash

# Pour initialiser le projet spring
spring init -d=web,actuator,lombok -n=$PROJECT_NAME --package-name=$PACKAGE_NAME --build=maven $PROJECT_NAME