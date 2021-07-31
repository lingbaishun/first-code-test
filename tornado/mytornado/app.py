import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("base.html")

class baseHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("base1.html")

def make_app():
    return tornado.web.Application(
        [
        (r"/donglang", MainHandler),
        (r"/donglang/520", baseHandler),
        ],
        template_path = os.path.join(
            os.path.dirname(__file__),
            "templates"
        ),
        debug = True
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(5488)
    tornado.ioloop.IOLoop.current().start()