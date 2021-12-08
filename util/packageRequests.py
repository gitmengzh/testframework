import json
import requests

# 参考封装requests  https://testerhome.com/articles/31956   https://www.cnblogs.com/df888/p/12365710.html   封装 requests


class  HttpRequest(object):

    def __init__(self, baseUrl: str ):
        """
        :param baseUrl: 接口基础路径
        """
        self.url = baseUrl

    # 封装一个post
    def basePost(self, data, interface=None, method=None, app_type='json'):
        """
            :param  data: 请求数据
            :param  interface:  具体接口
            :param  method： 具体方法，主要用在是否是session
            :param  app_type:   请求数据类型，默认为json
        """
        if not interface:
            url = self.url + interface
        else:
            url = self.url

        if app_type == 'json':
            sendData = json.dumps(data)
        else:
            return '该类型数据暂不支持'

        if method == 'session':
            r = requests.session()
        else:
            r = requests
        req = r.post(url, sendData)
        result = req.json()
        return result

    # 封装一个get
    def baseGet(self, data=None, interface=None, type=None, token=None, code='json'):
        if not interface:
            url = self.url + interface
        else:
            url = self.url
        if token:
            header = {"Authorization": token}

        if type == 'session':
            r = requests.session()
        else:
            r = requests
        if not data:
            req = r.get(url, params=data)
        else:
            req = r.get(url)
        # result = req.json()
        return req

    # 文件上传
    def upload(self, interface: str, filepath):

        url = self.baseUrl + interface
        if filepath:
            files = {'file': open('report.xls', 'rb')}
            r = requests.post(url, files=files)
            if r.status_code == '200':
                return 'upload success'
            else:
                return 'upload failed'
        else:
            return "上传文件不能为空"









"""
requests.post
requesta.get
requests.session
# 请求
    1. 定制请求头
        *   header = {'user-agent': 'my-app/0.0.1'，'content-type': 'application/json'}
        *   cookie = {'key':'value'}
        r = requests.get/post('your url',headers=header,cookies=cookie) 
        
    2. 获取头信息  
        r.headers                                  #返回字典类型,头信息
        r.requests.headers                         #返回发送到服务器的头信息
        r.cookies                                  #返回cookie
        
        
    3. 会话对象，能够跨请求保持某些参数
        s = requests.Session()
        s.auth = ('auth','passwd')
        s.headers = {'key':'value'}
        r = s.get('url')
    3. 设置超时    
        r = requests.get('url',timeout=1)           #设置秒数超时，仅对于连接有效
        
    4. post&&get请求
        # 1、基本POST实例
  
            import requests
              
            payload = {'key1': 'value1', 'key2': 'value2'}
            ret = requests.post("http://httpbin.org/post", data=payload)
              
            print(ret.text)
              
              
            # 2、发送请求头和数据实例
              
            import requests
            import json
              
            url = 'https://api.github.com/some/endpoint'
            payload = {'some': 'data'}
            headers = {'content-type': 'application/json'}
              
            ret = requests.post(url, data=json.dumps(payload), headers=headers)
              
            print(ret.text)
            print(ret.cookies)
   
         # 2、有参数实例
          
         payload = {'key1': 'value1', 'key2': 'value2'}
         ret = requests.get("http://httpbin.org/get", params=payload)
         
        print(ret.url)
         print(ret.text)
            
    5. 其他请求
    requests.put(“http://httpbin.org/put”)                        # PUT请求
    requests.delete(“http://httpbin.org/delete”)                  # DELETE请求
    requests.head(“http://httpbin.org/get”)                       # HEAD请求
    requests.options(“http://httpbin.org/get” )                   # OPTIONS请求
    
    6. 文件上传
    url = 'http://m.ctrip.com'
    files = {'file': open('report.xls', 'rb')}
    r = requests.post(url, files=files)
    
        
        

# 响应
        r.encoding                       #获取当前的编码
        r.encoding = 'utf-8'             #设置编码
        r.text                           #以encoding解析返回内容。字符串方式的响应体，会自动根据响应头部的字符编码进行解码。
        r.content                        #以字节形式（二进制）返回。字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩。
        r.headers                        #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
        r.status_code                     #响应状态码
        r.raw                             #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read()   
        r.ok                              # 查看r.ok的布尔值便可以知道是否登陆成功
        #*特殊方法*#
        r.json()                         #Requests中内置的JSON解码器，以json形式返回,前提返回的内容确保是json格式的，不然解析出错会抛异常
        r.raise_for_status()             #失败请求(非200响应)抛出异常



# 方法



https://www.cnblogs.com/lanyinhao/p/9634742.html

"""