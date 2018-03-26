#!/usr/bin/env bash

export PATH="/usr/local/bin:$PATH"
export DATABASE_URL="sqlite:///$HOME/.house.sqlite"

proj_dir="$HOME/cd-house"
if [ ! -d $proj_dir ];then
    git clone https://github.com/crazygit/cd-house.git $proj_dir
else
    cd $proj_dir && git pull origin master
fi

cd $proj_dir && pipenv install && pipenv run scrapy crawl cdfangxie -L ERROR
