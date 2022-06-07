FROM amazonlinux:latest
#ADD al2022-container-2022.0.20220202.0-x86_64.tar.xz /
RUN yum update -y 
RUN yum install -y python3 python3-devel
RUN yum install -y amazon-linux-extras

RUN amazon-linux-extras install -y epel
RUN amazon-linux-extras enable postgresql9.6
RUN yum install -y postgresql-devel
RUN  yum install -y gcc.x86_64

RUN yum install -y net-tools
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
# ping
RUN yum install -y procps
RUN yum install -y  iputils  
EXPOSE 8000 
CMD ["/bin/bash"]

#  docker run -it  -p 127.0.0.1:8000:8000 -v D:\pyServer\dj_aws_template:/code  -e IS_DOCKER=True --name test3 docker_compiler_django  bash -c  "cd /code/dj_aws_template/dj_aws_template/ && python3 manage.py runserver  0.0.0.0:8000"
#  docker run -it  -p 127.0.0.1:5000:8000 -v D:\pyServer\django_example\django_example:/code  --name test4 docker_compiler_django  bash -c  "cd /code/ && python3 manage.py runserver  0.0.0.0:8000"