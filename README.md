### Technology Stack
Component         | Technology
---               | ---
Backend           | Python 3.7 (Flask)
Database          | Mysql
API Documentation | Swagger-UI (Node.js)
Proxy             | Nginx
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
├── Dockerfiles
│   └── Dockerfile 파일
├── nginx
│   └── nginx config 파일
│
├── .env # 환경변수
├── .gitignore
├── 00_start.sh # 프로젝트 실행 쉘 스크립트
├── 01_stop.sh # 프로젝트 중지 쉘 스크립트
├── application.py
├── docker-compose.yaml
├── README.md
└── requirements.txt

```


### How to Start
1. Clone Repository
    - git 원격 저장소 가져옵니다.
    ```shell script
    git clone https://github.com/JeongHM/wants.git
    ```
   
2. Start Project
    - shell 을 사용하여 프로젝트를 실행합니다.  
    ```shell script
    $ sh ./00_start.sh
    # 1. .env 파일을 생성합니다.
    # 2. 프로젝트에서 사용할 포트를 확인합니다.
    # 3. 도커 컴포즈를 실행합니다.
    ```
   
   1. 프로젝트가 정상 실행되지 않는 경우
        1. 프로젝트에서 사용할 포트가 겹치는 경우 -> 해당 포트를 사용하고있는 어플리케이션을 중지 시켜주셔야됩니다.
        2. 도커 볼륨의 이름이 같은 경우 
           ```shell script
           docker volume rm wants_mysql_volumes
           ```
        
   
3.  Application List
    - 실행되는 컨테이너 확인
    1. API : http://127.0.0.1/api/auto-complete?company_name=wan
    2. Swagger : http://127.0.0.1/swagger/
    
    
