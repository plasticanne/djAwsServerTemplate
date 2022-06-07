
*Set Beanstalk Configuration*  

**python37+nginx**  
Beanstalk platform: "python37 64bit Amazon Linux 2"  
RDS: postgresql 12  
Elasticache: redis  
***Container***:  
WSGIPath :  application  
Proxy server: Nginx  

***Structure***  
out of Beanstalk: port 80 nginx  
inner pass to docker container : file stream uwsgi_pass
systemctl with uwsgi
 

*Install*  
***0. compile to cython***  
****a. build docker compile env****  
build aws linux 2 compile env  
*****docker container*****  
```  
cd {your_path}\amazonLinux2\docker_compiler
docker run -it  -p 127.0.0.1:8000:8000 -v {your_path}\amazonLinux2:/code  -e IS_DOCKER=True --name compiler docker_compiler_django
```   
*****compile*****    
in container   
```
cd /code/dj_aws_template/dj_aws_template  
python3 make.py  
```  
The compiled files will be in /code/dj_aws_template/dist   

*****run server local*****    
```  
cd /code/dj_aws_template/dist 
python3 manage.py runserver  0.0.0.0:8000  
```   
 
***1. deploy codes***  
package dict to zip 
contain:
.ebextensions  (For ssh in to your EC2, you need install 02_export_aws_env.config  for access environment variables)
.platform  
Procfile  
uwsgi_py37.ini
wsgi.py

***2. check nginx.conf in ec2***  
ssh to ec2  
check .ebextensions,.platform,Procfile are all well set:    
- /etc/nginx/nginx.conf   


- *****a. First install(need with 02_export_aws_env.config)*****
To venv,    
`cd /var/app/current; source /var/app/venv/*/bin/activate;`
django DB makemigrate,  
` python3 manage.py makemigrate`  
django DB migrate,  
`python3 manage.py migrate`  
create superuser,  
`python3 manage.py createsuperuser`

- *****b. None first install*****  
check server running
systemctl status web.service


*local dev*  
**redis**  
`cd /usr/bin
./redis-server
`  


***Beanstalk Environment Variables***:  
ENV_MODE:1  
DEBUG:0  
API_DEBUG:1  
ADMIN_URL:admin  
ALLOWED_HOSTS:{beanstalk entrypoint}  
HOST_URL:www.demo.com  
CORS_ALLOW_CREDENTIALS:True  
CORS_ORIGIN_ALLOW_ALL:False  
CORS_ORIGIN_WHITELIST:https://www.demo2.com,{beanstalk entrypoint},{s3 website entrypoint}  

AWS_REDIS:xxxxxxxxx.cache.amazonaws.com:6379  
DATABASES_REDIS_TAG:my-redis-tag  
  
AWS_REGION_NAME:{your-region}  
AWS_DYNAMODB_TABLE_NAME:my-dydb-table  
  
AWS_STORAGE_BUCKET_NAME:my-s3-bucket  
   
RDS_DB_NAME:my-rdsdb  
RDS_HOSTNAME:xxxxxxx.rds.amazonaws.com  
RDS_PASSWORD:12345678  
RDS_PORT:5432  
RDS_USERNAME:my-name  



*issues and note*  

https://docs.aws.amazon.com/zh_tw/elasticbeanstalk/latest/dg/create-deploy-python-container.html#python-namespaces

https://serverfault.com/questions/398972/need-to-increase-nginx-throughput-to-an-upstream-unix-socket-linux-kernel-tun  
https://serverfault.com/questions/867866/11-resource-temporarily-unavailable-while-connecting-to-upstream-bad-gateway  

https://t.codebug.vip/questions-288387.htm
https://www.jianshu.com/p/09e47fb385c1
https://stackoverflow.com/questions/28267419/how-can-i-run-a-docker-container-in-aws-elastic-beanstalk-with-non-default-run-p