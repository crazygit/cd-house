.PHONY: help, pip, test, clean, pep8, install-git-hooks, build, crawl, web

PRE_COMMIT_EXISTS := $(shell [ -f .git/hooks/pre-commit ] && echo 1 || echo 0)

default: help

install-git-hooks:
ifeq ($(PRE_COMMIT_EXISTS), 0)
	$(info install git hooks: .git/hooks/pre-commit.sh)
	curl -s -o .git/hooks/pre-commit https://raw.githubusercontent.com/google/yapf/master/plugins/pre-commit.sh && \
		chmod +x .git/hooks/pre-commit
	@echo "Success install yapf commit hook"
endif

pip:
	pipenv install --python=3.6.4 --dev

pep8: isort
	pipenv run yapf -ir --style=google cdhouse

test: clean
	pipenv run python -m pytest

clean:
	@echo "Clean ..."
	@find ./ -name '*.pyc' -exec rm -f {} +
	@find ./ -name '*.pyo' -exec rm -f {} +
	@find ./ -name '*~' -exec rm -f {} +
	@find ./ -name '__pycache__' -exec rm -rf {} +

crawl: clean
	pipenv run scrapy crawl cdfangxie

web: clean
	pipenv run gunicorn -b 0.0.0.0:5000 --worker-class gevent --workers=2 cdhouse.web.app:robot.wsgi

build: clean
	docker-compose build --force-rm

isort: clean
	isort -rc cdhouse

help:
	@echo "   \033[35mmake\033[0m \033[1m命令使用说明\033[0m"
	@echo "   \033[35mmake pip\033[0m\t\033[0m\t---  安装依赖"
	@echo "   \033[35mmake clean\033[0m\t\033[0m\t---  清理 Python 缓存文件"
	@echo "   \033[35mmake test\033[0m\t\033[0m\t---  运行测试用例"
	@echo "   \033[35mmake pep8\033[0m\t\033[0m\t---  格式化代码"
	@echo "   \033[35mmake install-git-hooks\033[0m\t\033[0m\t---  下载yapf commit hook"
	@echo "   \033[35mmake crawl\033[0m\t\033[0m\t---  运行爬虫"
	@echo "   \033[35mmake run\033[0m\t\033[0m\t---  运行web服务"
	@echo "   \033[35mmake build\033[0m\t\033[0m\t---  构建docker镜像"

