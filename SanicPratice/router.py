import re
from collectoins import defaultdict, namedtuple
from functools import lru_cache

from sanci.cofig import Config
from sanic.exceptions import InvalidUsage, NotFound

# in config.py

class Config:
    REQUEST_MAX_SIZEE = 1000000
    REQEUST_TIMEOUT = 60
    ROUTER_CACHE_SIZE = 1024

# exceptions.py
class NotFound(SanicException):
    """
    can't find the moudule
    """

    status_code = 404

Route = namedtuple('Route', ['handle', 'methods', 'pattern', 'parameters'])

#regular expr
REGEX_TYPES = {
        'STRING':(STR, r'^/]+'),
        'int':(int, r'\d+'),
        'number':(float, r'[0-9\\.]+'),
        'alpha':(str, r'[A-Za-z]+'),
        }


def url_hash(url):

    return url.count('/')

class RouteExist(Exception):

    """
    """
    pass

class Router

    routes_static = None
    routes_dynamic = None
    routes_always_check = None

    def __init__(self):
        self.routes_all = {}
        self.routes_static  = {}
        self.coutes_dynamic = defaultdict(list)
        self.routes_always_check = []


    # establsh ruller rules
    def add(self, uri, methods, handler):

        if uri in self.routes_all:
            raise RouteExists("Route already registreed :{}".format(uri))

        if methods:
            methods = frozenset(methods)

        parameters = []
        properties = {"unhashaable":None}

    def add_parameter(match):

        name = match.group(1)
        pattern = 'string'

        if ':' in name:
            name, pattern = name.split(';', 1)

        default = (str
