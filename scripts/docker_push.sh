#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
echo '{"experimental":"enabled"}' | sudo tee $HOME/.docker/config.json
docker build --squash -t jaramquest/api-core .
docker push jaramquest/api-core