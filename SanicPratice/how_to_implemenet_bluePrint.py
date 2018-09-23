
class BlueprintSetup:

    def  __init__(self, blueprint, app, options):
        self.app = app
        self.blueprint = blueprint
        self.options = options

        url_prefix = self.options.get('url_prefix')
        if url_prefix is None:
            url_prefix = self.blueprint.url_prefix

        self.url_prefix = url_prefix



    def add_route(self, handler, uri, methods):

        if self.url_prefix:
            uri = self.url_prefix + uri

        self.app.route(uri=uri, methods=methods)(handler)

    def add_exception(self, handler, *args, **kwargs):

        self.app.exception(*args, **kwargs)(handler)

    def add_middleware(self, middleware, *args, **kwargs):
        """
        """

        if args or kwargs:
            self.app.middleware(*args, **kwargs)(middleware)
        else:
            self.app.middleware(middleware)

from collections import defaultdict

class Blueprint:

    def __init__(self, name, url_prefix=None):

        self.name = name
        self.url_prefix = url_prefix
        self.deferred_functions = []


    def make_setup_state(self, app, options):

        return BlueprintSetup(self, app, options)

    def record(self, func):

        self.deferred_functions.append(func)

    def register(self, app, options):

        state = self.make_setup_state(app, options)
        for deferred in self.deferred_functions:
            deferred(state)

    def route(self, uri, methods=None):

        def decorator(handler):
            self.record(lambda s:s.add_route(handler, uri, methods))

            return handler
    return decorator
s
    def add_route(self, handler, uri, methods=None):

        self.record(lambda s:s.add_routeE(handler, uri, methods))

        return handler

    def middleware(self, *args, **kwargs):

        def register_middleware(middleware):
            self.record(
                    lambda s: s.add_middleware(middlewar, *args, **kwargs))
            return middleware

        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            middleware = args[0]
            args = []

            return register_middlerware(middleware)
        else:
            return register_middleware

    def exception(self, *args, **kwargs):

        def decorator(handler):
            self.record(lambda s: s.add_exception(handler, *args, **kwargs))
            return handler
        return decorator



