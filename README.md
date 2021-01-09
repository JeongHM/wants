### Technology Stack
Component         | Technology
---               | ---
Backend           | Python 3.7 / Flask
Database          | Mysql
API Documentation | Swagger-UI
Container         | Docker-compose

### File Structure
```markdown
├── controllers
│   └── 컨트롤러 관련 파일
├── models
│   └── 모델 관련 파일
├── services
│   └── 비지니스 로직 관련 파일
├── swagger
│   └── 스웨거
├── testcases
│   └── 테스트 케이스 스크립트
├── utils
│   └── API 내 공통으로 사용 관련 파일
├── validator
│   └── API body, request 검증 로직
│
├── .env # 환경변수
├── .gitignore
├── application.py
├── docker-compose.yaml
├── Dockerfile
├── requirements.txt
├── README.md
└── requirements.txt

```


### How to Start
1. Clone repository
    - git 원격 저장소 가져오기
    ```shell script
    git clone https://github.com/JeongHM/wants.git
    ```
   
2. Set .env
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
   
3. Start docker-compose
    - docker-compose 실행
    ```shell script
    docker-compose up -d    
    ```

4. If you get same local database volume name
    - docker-compose 의 mysql 볼륨은 local로 저장하고있으므로 만약 사용하는 볼륨의 값이랑 같은 경우 삭제해주시고 다시 실행 해주어야 합니다.
    ```shell script
    docker volumn rm wants_database
    ```
5. Start Swagger
    - swagger (API Docs) 를 실행시켜주시면 보다 편하게 볼 수 있습니다
    ```shell script   
    $ docker exec -it wants_application /bin/bash
    $ npm install swagger/ # npm 라이브러리 설치
    $ node swagger/index.js # 스웨거 실행
   
    http://127.0.0.1:3000/docs # 접속
    ```
