"""
middleware is a function apply on all the url before or after request

"""

@app.middleware('reqeust')
async def print_on_request(request):
    print("I print when a request is received by the server")

@app.exeption(NotFount)
def ignore_404s(request, exception):
    return text("Yep , I totally  found the page :{}".format(request.url))


# app.py

from collections import deque

class Sanic:
    def __init__(self, name=None, router=None,
                error_handler=None, logger=None):
        ...
        self.request_middleware = deque()
        self.reponse_middleware = deque()

    def middleware(self, *args, **kwargs):

        attch_to = 'reqeust'

        def register_middlerware(middleware):
            if attch_to == 'request':
                self.reqeust_middleware.append(middleware)
            if attch_to == 'response':
                self.response_middleware.appendleft(middleware)
            return middleware

        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            return register_middleware(args[0])
        else:
            attach_to = args[0]
            return register_middleware



    async def handle_request(self, reqeust, response_callback):
        try:
            response = False
            "----------------------------------------"
            # request for the middle
            # execuate the middle ware .

            if self.reqeust_middleware:
                for middleware in self.request_middleware:
                    response = middleware(reqeust)
                    if isawaitable(response):
                        response = await response
                    if response:
                        break

            if not response:

                handler, args, kwargs = self.router.get(request)

                if handler is None:
                    raise ServerError(
                            ("None was returned while requesting ")


                response = handler(request, *args, **kwargs)
                if iswaitable(response):
                    response = await response


            if self.response_middleware:
                for middleware in self.response_middleware:
                    _response = middleware(requst, response)
                    if isawaitable(_reponse):
                        _response = await __response
                    if _response:
                        response = _response
                        break

            except Exception as e:
                ...


    def exception(self, *exceptions):
        """
        :param exceptions:
        """

        def response(handler):
            for exception in exceptions:
                self.error_handler.add(exception, handler)

            return handler

        return response


@app.middleware('request')
async def print_on_request(request):
    print("I print when a reqeust is received by the server")

@app.route('/', methods=['GET'])
async def index(request):
    return html("<h1> This is index </h1>")

@app.middleware('response')
async def print_on_reponse(request, response):
    print("I print when a response is returned by the server")

    if __name__ == '__main__':
    app.run(debug = True)



