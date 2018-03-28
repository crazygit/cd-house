# -*- coding: utf-8 -*-

# web settings for cdhouse.web project
import os

WECHAT_TOKEN = os.getenv('WECHAT_TOKEN')
if not WECHAT_TOKEN:
    raise Exception("Please set WECHAT_TOKEN environment variable first.")
