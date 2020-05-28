docker buildx build --platform linux/arm64 -t jaramquest/api-core:arm64-latest .
docker buildx build --platform linux/amd64 -t jaramquest/api-core:amd64-latest .
docker manifest create --amend jaramquest/api-core jaramquest/api-core:amd64-latest jaramquest/api-core:arm64-latest
docker manifest annotate jaramquest/api-core jaramquest/api-core:arm64-latest --arch arm --variant v8 --os linux
docker manifest push jaramquest/api-core
