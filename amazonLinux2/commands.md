# commands  
sudo docker ps
sudo docker exec -ti contanterName  /bin/bash


sudo systemctl status web.service
sudo systemctl stop web.service
sudo systemctl start web.service

sudo service status nginx
sudo service nginx -s reload
sudo service nginx start
sudo service nginx stop
sudo service nginx restart

test dynamodb access
https://docs.aws.amazon.com/zh_tw/amazondynamodb/latest/developerguide/Query.html
aws dynamodb query --table-name my-table --region ap-southeast-1   --key-condition-expression "puuid = :hkey"  --expression-attribute-values '{":hkey":{"S":"xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx_1969-12_v0"}}'