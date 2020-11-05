FROM mariadb:10.3

RUN apt update \
    && apt install --no-install-recommends -y tzdata \
    && apt clean

RUN touch /var/log/mysql/mysqld.log
