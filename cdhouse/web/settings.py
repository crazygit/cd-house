# -*- coding: utf-8 -*-

# web settings for cdhouse.web project
import os
import re

from cdhouse.crawler.settings import (DATABASE_URL, WECHAT_APP_ID,
                                      WECHAT_APP_SECRET)

WECHAT_TOKEN = os.getenv('WECHAT_TOKEN')

assert WECHAT_TOKEN is not None
assert WECHAT_APP_ID is not None
assert WECHAT_APP_SECRET is not None
assert DATABASE_URL is not None

WECHAT_CUSTOM_MENU = {
    "button": [{
        "name":
        "区域",
        "sub_button": [{
            "type": "click",
            "name": "天府新区",
            "key": "天府新区"
        }, {
            "type": "click",
            "name": "高新南区",
            "key": "高新南区"
        }, {
            "type": "click",
            "name": "双流区",
            "key": "双流区"
        }]
    }, {
        "type": "view",
        "name": "成都房协",
        "url": "http://www.cdfangxie.com/"
    }]
}

REGIONS = [
    '锦江区', '青羊区', '金牛区', '武侯区', '成华区', '高新南区', '高新西区', '高新东区', '龙泉驿区', '青白江区',
    '新都区', '温江区', '金堂县', '双流区', '郫都区', '大邑县', '蒲江县', '新津县', '天府新区', '简阳市',
    '都江堰市', '彭州市', '邛崃市', '崇州市'
]

REGIONS_PATTERN = re.compile(f'({"|".join(REGIONS)})')

ECHO_SQL = False
