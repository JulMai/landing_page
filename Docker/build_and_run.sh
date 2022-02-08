# /bin/bash

DOCKERFILE=./Dockerfile
if test -f "$DOCKERFILE"; then
    echo "$DOCKERFILE exists"
else
    echo -e "$DOCKERFILE is missing.\nScript stopped"
fi

cp Dockerfile ../Dockerfile
cd ..

echo "building docker image"
docker build . -t "landing_page:latest"

rm -rf Dockerfile
cd Docker
docker-compose up -d