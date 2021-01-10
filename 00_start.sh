#/bin/bash

echo "Setting .env file [.env 파일을 생성합니다.]"
echo "DB_HOST=wants_database\nMYSQL_USER=root\nMYSQL_DATABASE=Wants\nMYSQL_ROOT_PASSWORD=Q&<f-xTQg4Z}y_6V" > .env
echo "\nCreate .env file [.env 파일이 생성 되었습니다.]\n"
echo "[.env file] \n$(cat .env)"

echo "\nVerify that the port used by Docker is in use. [도커에서 사용중인 포트를 확인합니다] \n"

PORTS=$(lsof -iTCP -sTCP:LISTEN -n -P | grep '3306\|5000\|80')

if [ -n "$PORTS" ]; then
  echo "Please stop the running port. [실핼중인 포트를 중지해야합니다]"
  lsof -iTCP -sTCP:LISTEN -n -P | grep '3306\|5000\|80'
else
  DOCKERS=$(docker ps -a | grep "wants_database\|wants_application\|wants_swagger")

  if [ -n "$DOCKERS" ]; then
    echo "Already Exists wants docker container [이미 도커 컨테이너가 존재합니다.]\n"
    echo "Start docker-compose down [실행중인 docker-compose를 중지합니다.]\n"
    docker-compose down
    echo "Start docker-compose up -d [docker-compose를 실행합니다.]\n"
    docker-compose up
  else
    echo "Start docker-compose up -d [docker-compose를 실행합니다.]\n"
    docker-compose up
  fi
fi