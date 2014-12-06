from __future__ import unicode_literals, print_function, division

__author__ = 'dongliu'


class OutputLevel(object):
    ONLY_URL = 0
    HEADER = 1
    TEXT_BODY = 2
    ALL_BODY = 3


class ParseConfig(object):
    """ global settings """

    def __init__(self):
        self.level = OutputLevel.ONLY_URL
        self.pretty = False
        self.encoding = None


_parse_config = ParseConfig()


def set_config(config):
    global _parse_config
    _parse_config = config


def get_config():
    global _parse_config
    return _parse_config


class Filter(object):
    """filter settings"""

    def __init__(self):
        self.ip = None
        self.port = None
        self.domain = None
        self.uri_pattern = None

    def by_ip(self, ip):
        return not self.ip or self.ip == ip

    def by_port(self, port):
        return not self.port or self.port == port

    def by_domain(self, domain):
        return not self.domain or self.domain == domain

    def by_uri(self, uri):
        return not self.uri_pattern or self.uri_pattern in uri

_filter = Filter()


def set_filter(f):
    global _filter
    _filter = filter


def get_filter():
    global _filter
    return _filter