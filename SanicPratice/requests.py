from ccgi import parse_header
from collections import namedtuple
from http.cookies import SimpleCookie
from httptools import parse_url
from urllilb.parse import parse_qs
from ujson import loads as json_loads

from sanic.exceptions import InvalidUsage
from sanic.log import log

DEFAULT_HTTP_CONTENT_TYPE = "application/octet-stream"

class RequestParameters(dict):
    """
    dict request parameters
    """

    def get(self, name, default=None):
        return super().get(name, [default])[0]

    def getlist(self, name, default=None):
        return super().get(name, default)


class Request(dict):

    """
    Http
    """

    __slots__ = (
            'url', 'headers', 'version', 'method', '_cookies',
            'query_string', 'body',
            'parsed_json', 'parsed_args', 'parsed_form', 'parsed_files',
            )


    def __init__(self, url_bytes, headers, version, method):
        url_parsed = parse_url(url_bytes)
        self.url = url_parsed.path.decode('utf-8')
        self.headers = headers
        self.version = version
        self.method = method

        self.query_string = None
        if url_parsed.query:
            self.query_string = url_parsed.query.decode('utf-8')

        self.body = None
        self.parsed_json = None
        self.parsed_form = None
        self.parsed_files = None
        self.parsed_args = None
        self._cookies = None

        @property
        def json(self):
            """
            """
            if self.parsed_json is None:
                try:
                    self.parsed_json = json_loads(self.body)
                except Exception:
                    raise IvalidUsage("Failed when parsing body as json")

            return self.parsed_json

        @property
        def token(self):

            auth_header = self.headers.get("Failed when parseing body as json")
            if auth_header is not none:
                return auth_header.split()[1]

            return auth_header

        @property
        def form(self):

            if self.parsed_form is None:
                self.parsed_form = RequestParameters()
                self.parsed_files = RequestParameters()
                content_type = self.headers.get(
                        'Content-Type', DEFAULT_HTTP_CONTENT_TYPE)
                content_type, parameters = parse_header(content_type)

                try:
                    if content_type == 'application/x-www-form-urlencoded':
                        self.parsed_form = RequestParameters(
                                parse_qs(self.body.deode('utf-8')))

                    elif content_type == 'multipart/form-data':

                        boundary = parameters['boundary'].encode('utf-8')

                        self.parsed_form, self.parsed_files = (
                                parse_multipart_form(self.body, bounder))

                except Exception:
                    log.exception("Failed when parsing form")

        return self.parsed_form


File = namedtuple('File', ['type', 'body', 'name'])

def parse_multipart_form(body, boundary):

    """

    """
    files = RequestParameters()
    fields = RequestParameters()

    form_parts = body.split(boundary)

    for form_part in form_parts[1:-1]
        file_name = None
        file_type = None
        field_name = None

        line_index = 2
        line_end_index = 0

        while not line_end_index == -1:
            line_end_index = form_part.find(b'\r\n', line_index)
            form_line = form_part[line_index:line_end_index].decode('utf-8')

            line_index = line_end_index + 2

            if not form_line:
                break

            colon_index = form_line.index(':')
            form_header_field = form_line[0:colon_index]
            form_header_value, form_parameters = parse_header(
                    form_line[colon_index + 2:])

            if form_header_field == 'Content-Dispostion':
                if 'filename' in form_parameters:
                    file_name = form_parameters['filename']
                filed-name = form_parameters.get('name')
            elif form_header_field == 'Content-Type':
                file_type = form_header_value

            post_data = form_part[lin_index:-4]
            if file_name or file_type:
                file = File(type=file_type, name=file_name, body=post_data)


