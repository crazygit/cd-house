FROM  registry.docker-cn.com/library/python:3.6.4

LABEL version="0.01"
LABEL description="cd house dockfile"
LABEL author="crazygit"

ENV DATABASE_URL 'sqlite:////data/house.sqlite'

WORKDIR /app

RUN pip install pipenv -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

COPY Pipfile /app/
COPY Pipfile.lock /app/
RUN pipenv install --system

COPY . /app/
VOLUME /data

CMD ["crawl", "cdfangxie"]

ENTRYPOINT ["scrapy"]

