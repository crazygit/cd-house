# -*- coding: utf-8 -*-

import logging

import requests
from requests.exceptions import RequestException
from retrying import retry

from cdhouse.utils.client import Client

logger = logging.getLogger(__name__)


class SendError(Exception):
    """send message failed error"""
    pass


def retry_if_network_error(error):
    logger.debug(f'send message failed: {error}, retry ...')
    return isinstance(error, RequestException)


class SlackClient(Client):

    def __init__(self, web_hook_url, timeout=3):
        self.web_hook_url = web_hook_url
        self.timeout = timeout

    @classmethod
    def get_client(cls, crawler):
        if crawler.settings.get('SLACK_WEBHOOK_URL', None):
            return cls(crawler.settings['SLACK_WEBHOOK_URL'])

    @retry(retry_on_exception=retry_if_network_error, stop_max_attempt_number=2)
    def send(self, msg):
        self.logger.debug(f"> {msg}")
        response = requests.post(
            self.web_hook_url, json={'text': msg}, timeout=self.timeout)
        if response.status_code != 200:
            raise SendError(response.text)
