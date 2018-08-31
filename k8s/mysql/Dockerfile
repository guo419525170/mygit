FROM mysql:5.7
#定义时区参数
ENV TZ=Asia/Shanghai

#设置时区
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo '$TZ' > /etc/timezone

#设置环境变量

ENV MYSQL_ALLOW_EMPTY_PASSWORD yes
COPY setup.sh /mysql/setup.sh
COPY schema.sql /mysql/schema.sql
COPY privileges.sql /mysql/privileges.sql
CMD ["sh", "/mysql/setup.sh"]
