### Technology Stack
Component         | Technology
---               | ---
Backend           | Python 3.7 / Flask
Database          | Mysql
API Documentation | Swagger-UI
Container         | Docker-compose


### How to Start
1. clone repository
    - git 원격 저장소 가져오기
    ```shell script
    git clone https://github.com/JeongHM/wants.git
    ```
   
2. set .env
    - docker-compose.yaml 에서 `.env` 의 값을 참조하므로 아래와 같이 셋팅해주셔야 합니다. 
    ```shell script
    # ~ <your_path>/wants
    
    $ nano (or vim) .env
    
   # ~ ~ <your_path>/wants/.env
    DB_HOST=wants_database
    MYSQL_USER=root
    MYSQL_DATABASE=Wants
    MYSQL_ROOT_PASSWORD=Q&<f-xTQg4Z}y_6V
    ```
   
3. start docker-compose
    - docker-compose 실행
    ```shell script
    docker-compose up -d    
    ```

4. if you get same local database volume name
    - docker-compose 의 mysql 볼륨은 local로 저장하고있으므로 만약 사용하는 볼륨의 값이랑 같은 경우 삭제해주시고 다시 실행 해주어야 합니다.
    ```shell script
    docker volumn rm wants_database
    ```
  