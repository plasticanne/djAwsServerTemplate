FROM python:3.6.8-stretch

RUN apt-get update && \
    apt-get upgrade -y && \ 	
    apt-get install -y \
	supervisor \
	sqlite3 && \
	pip install -U pip setuptools && \
    rm -rf /var/lib/apt/lists/*

# install uwsgi now because it takes a little while
RUN pip install uwsgi

# setup all the configfiles
#RUN echo "daemon off;" >> /etc/nginx/nginx.conf
#COPY nginx-app.conf /etc/nginx/sites-available/default

#RUN mkdir -p /etc/nginx/log/

# Install PostgreSQL dependencies
RUN apt-get update && \
    apt-get install -y postgresql libpq-dev && \
    rm -rf /var/lib/apt/lists/
# Add sample application


# RUN sysctl -w net.core.somaxconn=32768
# RUN sysctl -w net.core.netdev_max_backlog=32768

#COPY requirements.txt /home/docker/code/
#COPY mysite /home/docker/code/
RUN mkdir -p /home/docker/code
WORKDIR /home/docker/code
COPY . /home/docker/code
COPY supervisor-app.conf /etc/supervisor/conf.d/
RUN pip install --upgrade pip
RUN pip install -r /home/docker/code/requirements.txt
#ADD app.py /tmp/app.py
EXPOSE 8000

# Run it

#CMD uwsgi --ini uwsgi.ini
CMD supervisord -n