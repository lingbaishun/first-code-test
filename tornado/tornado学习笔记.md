### tornado学习笔记

**Tornado Web 主要模块**

- tornado.web Application和RequestHandler类处理http请求
- tornado.template模板渲染
- tornado.routing处理路由



**模板渲染：**

- 在主文件(app.py)目录下建立templates文件夹

- 在templates文件夹下面建立html文件(base.html)进行渲染

- 将self.write改成self.render("base.html")

- tornado.web.Application中添加
	```
	template_path=os.path.join(os.path.dirname(__file__),"templates"),
	debug = ture #这里是为了支持代码在线改动
	```

**异步：**可以处理多个客户端请求

- tornado.httpserver非阻塞http服务器

  ```
  import tornado.gen
  import tornado.httpserver
  import tornado.ioloop
  import tornado.web
  
  class sleephandler(tornado.web.RequestHandler):
  	@tornado.gen.coroutine #协程
  	def get(self):
  		yield tornado.gen.sleep(5) #异步的sleep
  		self.write(str(dt.datetime.now()))
  ...
  ...
  	
  ```

- tornado.httpclient异步http客户端
```
  import tornado.gen
  import tornado.httpclient
  import tornado.ioloop
  from tornado import gen
  
  N=10
  URL = ''
  
  @gen.coroutine
  def main():
  	http_client = tornado.httpclient.AsyncHTTPClient()
  	responses = yield [
  		http_client.fetch(URL) for i in range(N)
  	]
  
  beg1 = time.time()
  tornado.ioloop.IOLoop.current().run_sync(main)
  print(time.time()-beg1)
```