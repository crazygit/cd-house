# -*- coding: utf-8 -*-

import logging

import requests
from requests.exceptions import RequestException
from retrying import retry

logger = logging.getLogger(__name__)


class SendError(Exception):
    """send message failed error"""
    pass


def retry_if_network_error(error):
    logger.debug(f'send message failed: {error}, retry ...')
    return isinstance(error, RequestException)


class SlackSender(object):
    def __init__(self, web_hook_url, timeout=3):
        self.web_hook_url = web_hook_url
        self.timeout = timeout

    @retry(
        retry_on_exception=retry_if_network_error, stop_max_attempt_number=7)
    def send(self, data):
        logger.debug(f"> {data}")
        response = requests.post(
            self.web_hook_url, json={'text': data}, timeout=self.timeout)
        if response.status_code != 200:
            raise SendError(response.text)
