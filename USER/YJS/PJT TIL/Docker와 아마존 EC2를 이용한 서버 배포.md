1. ec2 인스턴스에 접근하는 방법 (PUTTY, pem 파일 키만 있을 경우)

   - puttygen을통해 private key 생성
     - Conversions 탭에서 import key를 한뒤 바로 Save private key (RSA 방법으로, 추가 암호화하면 보안에 더좋음) (절대 Generate 키를 누르면 안된다.)
     - 마우스 움직여주면 빠르게 랜덤시드 생성해서 빨리됨
     - 그렇게 생긴 pkk를 putty.exe의 Connection -> SSH-> Auth  탭의 private key file for authenticatino 폼에 넣는다.
     - Session 탭에 Host Name(Ip주소나 Host Name)을 올바른 포트와 함께 넣고 open한 뒤 설정된 유저 이름으로 로그인하면 된다. (보통 root, ubuntu, ec2-user가 기본 설정 유저 이름)

2. docker로 ubuntu 가상화해보기

   - docker run ubuntu:원하는 버전으로 하면 바로 꺼짐 여튼됨

3. ec2에 docker, docker-composer 깔기

   - 공식 홈페이지의 우분투에서 도커 까는법 참고함 https://docs.docker.com/engine/install/ubuntu/

   ```
    sudo apt-get update
   
   $ sudo apt-get install \
       apt-transport-https \
       ca-certificates \
       curl \
       gnupg-agent \
       software-properties-common
       
   $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   
   $ sudo add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) \
      stable"
      
   $ sudo apt-get update
   $ sudo apt-get install docker-ce docker-ce-cli containerd.io
   
   $ sudo docker run hello-world //확인용
       
   ```

   > Docker-compose 깔기

   ```
   sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   
   sudo chmod +x /usr/local/bin/docker-compose
   ```

   

4. 내 flask 프로젝트 docker image화하고 ec2 ubuntu에 배포해보기

   - 출처 : https://yvvyoon.github.io/python/deployment-flask-app-with-docker/

   - $ pip install pipreqs (requirements.txt 생성 위한 모듈)

   - $ pipreqs ./ --encoding=utf8 (내가 해당 프로젝트에 필요한 모듈들을 적어줌)

   - app.py 같은 경로에 Dockerfile 생성, (""만쓰자, ''를 linux에서 못알아봄!)

     ```dockerfile
     FROM python:3.7.4
     
     COPY . /app
     
     WORKDIR /app
     
     RUN pip install -r requirements.txt
     
     ENTRYPOINT ["python"]
     
     CMD ["app.py"]
     
     
     나중에 안되서
     
     FROM python:3.7.4
     
     COPY . /app
     
     WORKDIR /app
     
     RUN pip install -r requirements.txt
     
     # ENTRYPOINT ["python"]
     
     # CMD ["app.py"]
     
     ENTRYPOINT [ "flask" ]
     
     CMD ["flask", "run", "--host", "0.0.0.0"]
     
     이렇게 바꿨다.
     그리고 또 다시 위로 환복됨
     
     ```

   - docker build -t [docker Hub Id]/[생성한 repo 이름]:[태그] . (점 중요! 현재 위치를 의미)

     - 포트를 설정해줘야하므로 app.py 파일의 app.run을

       ```
       if __name__ == "__main__":
           app.run(debug=False, host="0.0.0.0", port="5001")
       ```

     - 이런식으로 바꿔줬다.

     - 참고로 [Repository]:[태그]로 저장됨
     - 여기서 Repository는 보통 docker Hub Id/생성한 repo 이름 으로 저장한다.

   - docker images 로 test Repository 이미지 확인

   - docker login -u \<ID\>로 로그인

   - $ docker [docker Hub Id]/[생성한 repo 이름]:[태그] [dockerhub ID]/[dockerhub repository] => 안해도됨

     - 생성 확인 후 

   - $ docker push  [dockerhub ID]/[dockerhub repository]:[push할 태그명]

   - 이후 ubunt ec2에서 docker login -u [id]

     - 로그인이 안된다면

     - ```
       sudo apt install gnupg2 pass
       ```

   -  docker pull [Id]/[repo]:[tag]

   - 이후 docker run --rm -d [imageID] (-rm을 안붙이면 컨테이너가 지워지지 않아서 최신화가 안되는 듯?, -d를 안붙이면 서버를 백그라운드에 실행하는 detached 모드가 실행 안된다.) 

   - 만약 permission deny가 뜨면 앞에 sudo를 붙여서 관리자 권한으로!

5. 가상화한 환경에 추가로 doccano 배포해보기

   - 만약 permission deny가 뜨면 앞에 sudo를 붙여서 관리자 권한으로!

   - doccano 공식 github의 https://github.com/doccano/doccano 참조함

   - ```
     $ git clone https://github.com/doccano/doccano.git
     $ cd doccano
     ```
     

     ```
     $ docker-compose -f docker-compose.prod.yml up -d (-d를 붙이면 detach 모드로 background에서 실행됨)
     ```
     
   - 만약 버전관련 문제 생기면 docker-compose의 공식홈페이지의 curl을 이용한 설치 방법 뒤 권한을 추가해서 해결할 수 있다.

     ```
     sudo apt install curl 
     //curl 다운로드
     
     sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
     //1.24.0 대신 최신버전의 composer를 쓰면 된다.
     
     sudo chmod +x /usr/local/bin/docker-compose 
     // 해당 루트에 관리자 권한 주기, 안하면 오류남
     ```

   - 다른 자잘한 오류들은 container 들과 image들을 지워서 해결해보자!

     - sudo docker image prune : 사용하지 않고 있는(관련 컨테이너가 없는?)  이미지들 삭제
     - sudo docker container prune : 중지된(exit) container들 삭제 -f 를 뒤에 붙여 강제 삭제 가능
     - sudo docker images : 현재 모든 이미지들 확인
     - sudo docker ps -a : 현재 모든 컨테이너들 확인, -a는 중지된것도 포함해서 보여줌
     - sudo docker stop [container ID] : 해당 container 중단

   - 기본적인 linux 명령어: 폴더 지우기 sudo rm -rf [폴더명]

   - sudo rm [파일명], sudo mkdir [만들 폴더명], 

6. doccano 배포 파일 받아보기

7. 위 설정을 dockerfile로 만들기

8. dockerfile 포함해서 docker image 만들기

9. docker image로 기존의 ec2 인스턴스에 환경설정

10. 퍼블릭으로 접근 가능한지 확인해보기

11. 예시 및 디버깅 
    - flask 서버 응답 확인
    - doccano 회원가입 및 데이터 처리
    - 처리한 데이터 다운받아보기
    - doccano 회원 관리

12. ec2 인스턴스 종료후 자동화 배포 해보기

13. frontend server 배포

    - 대체로 flask 배포 때와 비슷하다.
    - 우리 frontend 서버는 create-react-app을 통해 만들었으므로 미리 정의된 Dockerfile을 활용했다.

> .dockerignore

```
node_modules
npm-debug.log
```

>Dockerfile

```dockerfile
FROM mhart/alpine-node:11 AS builder
WORKDIR /app
COPY . .
RUN npm install react-scripts -g --silent
RUN yarn install
RUN yarn run build

FROM mhart/alpine-node
RUN yarn global add serve
WORKDIR /app
COPY --from=builder /app/build .
CMD ["serve", "-p", "22", "-s", "."]doc

```

- 서버 포트부분은 조금 바꿔주었다.
- 이후 이미지 생성 후 컨테이너를 배포하여 배포성공하였다.

먼저 기본 주소창 입력으로 포트번호 미입력하고 들어가면 80포트로 자동으로 들어가진다. 하지만 우리 80포트는 annotation tool이 차지하고 있으므로 기본 포트번호를 바꿔주거나 해당 툴을 꺼야한다.

현재 annotation tool은 더이상 이용하지 않고 있으며, 무엇보다 ssh 설정을 바꿔주는 방법에 생소해 돌이킬 수 없을 까봐 annotation tool을 끄고 하기로 했다.