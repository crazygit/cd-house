[toc]

## 成都商品房摇号楼盘爬虫

定期从[成都房协](http://171.221.172.13:8888/lottery/accept/projectList)抓取发布的楼盘信息，当发现有新的楼盘发布或有楼盘信息发生更新的时候，通过Slack或微信公众号将信息推送给关注着

## 使用说明

运行项目前, 有四个环境变量需要配置

### 必须配置的环境变量

* `DATABASE_URL`: 设置保存数据的数据库路径，比如: `sqlite:////path/to/db.sqlite`

### 可选环境变量

* `SLACK_WEBHOOK_URL`: Slack的`web hook url`, 用于通过slack来推送房源信息

* `WECHAT_APP_ID`: 微信公众号的`appid`, 用于通过微信公众号来推送房源信息
* `WECHAT_APP_SECRET`: 微信公众号的`appsecret`
用于通过微信公众号来推送房源信息


## 运行代码

下载代码后，可以在本地配置开发环境运行项目，也可以通过docker-compose运行。

### 下载代码

```bash
$ git clone https://github.com/crazygit/cd-house.git
```

### 直接运行

确定本地python版本为3.6+, 开发使用的python版本为

```bash
$ python --version
Python 3.6.4
```

安装依赖管理工具

```
$ pip3 install pipenv
```

运行代码

```bash
# 配置保存爬取数据的数据库地址
$ export DATABASE_URL='sqlite:////data/house.sqlite'

# slack和微信公众号可以任意选择需要配置哪一种，也可以都配置，也可以都不配置
$ export SLACK_WEBHOOK_URL='xxxxxxxxxxxxxxxxxxxxx'
$ export WECHAT_APP_ID='xxxxxxxxxxxxxxxxxxxxx'
$ export WECHAT_APP_SECRET='xxxxxxxxxxxxxxxxxxxxx'

# 安装依赖
$ pipenv install --python 3.6.4

# 运行爬虫
$ pipenv run scrapy crawl cdfangxie
```

### 以docker的方式运行

```bash
# 配置保存爬取数据的数据库地址
$ export DATABASE_URL='sqlite:////data/house.sqlite'
# slack和微信公众号可以任意选择需要配置哪一种，也可以都配置，也可以都不配置
$ export SLACK_WEBHOOK_URL='xxxxxxxxxxxxxxxxxxxxx'
$ export WECHAT_APP_ID='xxxxxxxxxxxxxxxxxxxxx'
$ export WECHAT_APP_SECRET='xxxxxxxxxxxxxxxxxxxxx'

# 构建docker镜像
$ docker-compose build --force-rm

# 运行爬虫服务
$ docker-compose run -e DATABASE_URL=${DATABASE_URL} -e SLACK_WEBHOOK_URL=${SLACK_WEBHOOK_URL} -e WECHAT_APP_ID=${WECHAT_APP_ID} -e WECHAT_APP_SECRET=${WECHAT_APP_SECRET} crawler
```

**注意**:

可以根据自己的需要，周期性运行爬虫

## 效果图

![微信公众号效果图](screenshots/wechat-demo.jpeg)

## Todo List

* [ ] 自定义爬虫命令, 当有异常时，返回正常的exit_code
* [ ] 添加微信公众号自定义菜单，方便按照区域查询在售楼盘信息
* [ ] 集成[Dash](https://plot.ly/products/dash/), 展示一些有用的数据图表
