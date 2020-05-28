#!/bin/bash
docker build --squash -t jaramquest/api-core .
docker push jaramquest/api-core