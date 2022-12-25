
import json
import time
from datetime import datetime
from aiohttp import web
from hyssop_aiohttp import routes, AioHttpView
#from .__init__ import BBBControllerTypes


'''
class AppInfo(Base):
    __tablename__ = 'app_info'
    id = Column('id', Integer, primary_key=True)
    name = Column(String)
    version = Column(String)
    author = Column(String)
    date = Column(Integer)
    remark = Column(String)
    def __init__(self, name, version, author, date, remark):
        self.name = name
        self.version = version
        self.author = author
        self.date = date
        self.remark = remark

    def __str__(self):
        return """
        app_id => {},
        app_name => {},
        app_version => {},
        app_author => {},
        app_date => {},
        app_remark => {}
        """.format(self.id, self.name, self.version, self.author, self.date, self.remark)
'''

class KKView(AioHttpView): #http://localhost:4444/haha_worldxxxwww
    async def get(self):
        """
        ---
        tags:
        - hello view
        summary: hello world view get
        description: simple test controller
        produces:
        - text/html
        responses:
            200:
                description: return hello view message
        """
        phone_no = await self.get_argument('kkk',default='預設參數值') #如果沒有kkk的參數 ,則帶入預設參數值
        return web.Response(text="Hello, world_KKView"+f'{phone_no}'+str(type(phone_no))) 
        return web.Response(text="Hello, world view KKView")
    
    async def post(self):
  
        phone_no = await self.get_arguments_dict(['ccc','password'])
                
        return web.Response(text="Hello, world_KKView"+f'{phone_no}'+str(type(phone_no))) 
        return web.Response(text="Hello, world view ")

class okok(AioHttpView):
    async def get(self):
        """
        ---
        tags:
        - hello view
        summary: hello world view get
        description: simple test controller
        produces:
        - text/html
        responses:
            200:
                description: return hello view message
        """
        phone_no = await self.get_argument('kkk',default='預設參數值') #如果沒有kkk的參數 ,則帶入預設參數值
        
        return web.Response(text="Hello, world111111"+f'{phone_no}'+str(type(phone_no))) 
        return web.Response(text="Hello, world view")
    
    async def post(self):
  
        phone_no = await self.get_arguments_dict(['ccc','password'])
                            
        return web.Response(text="Hello, world111111"+f'{phone_no}'+str(type(phone_no))) 

'''     
@routes.post('/api/singup/user/sql')
async def hello(request): #AioHttpRequest
    #async def hello(request): 

    engine = create_engine( # 改成 mysql 的連線方式
        'mysql+pymysql://root:111111@127.0.0.1:3306/dataDB', echo=False)
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()

    appDesc = """
    Please input action code :

    1 - Insert Data
    2 - Update Data
    3 - Delect Date
    --- --- ---
    0 - exit

    """
    isRun = True

    while(isRun):
        result = session.query(AppInfo).all()
        for row in result:
            print(row)

        ctrl = input(appDesc)
        if ctrl == "0":
            isRun = False
        elif ctrl == "1":
            appInfo = AppInfo('App', '1.0.1', 'DevAuth', # 宣告 AppInfo 物件
                              datetime(2021, 11, 8, 12, 30, 10), 'App-v1.0.1')
            session.add(appInfo) # add() 方法，參數帶入目標物件
            session.commit() # 新增的操作必須要加上提交的方法
        elif ctrl == "2":
            row_id = input("id = ? ")
            appInfo = session.query(AppInfo).filter_by(id=row_id).first() # 先查詢出目標物件
            appInfo.name = "AppNew" # 直接修改物件的參數
            appInfo.version = "1.0.2"
            appInfo.remark = "App-v1.0.2"
            session.commit() # 更新的操作必須要加上提交的方法
        elif ctrl == "3":
            row_id = input("id = ? ")
            appInfo = session.query(AppInfo).filter_by(id=row_id).first() # 先查詢出目標物件
            session.delete(appInfo) # delete 方法，參數帶入目標物件
            session.commit() # 刪除的操作必須要加上提交的方法

    dict = await request.get_arguments_dict(['k1', 'k2','k3'])  

    return web.Response(text="Hello, world111111"+f'{dict}'+str(type(dict))) 
'''
from component.__init__ import HelloComponentTypes 


@routes.post('/api/singup/user')
async def aaa(request): #AioHttpRequest
    
    now = lambda: time.time()
    start = now()  
    
    datas = await request.get_arguments_dict(['username', 'password'])  #接收username,password
    registerObj =  request.app.component_manager.get_component(HelloComponentTypes.Register)       #ok  #Register = enum_key:               
    response = registerObj.registerProcess(**datas)                     #ok                
    
    timeDuration = now() - start
    return  web.Response (text= response + str(timeDuration))

@routes.post('/api/singin/user')
async def singin(request): 
    now = lambda: time.time()
    start = now()  
    
    datas = await request.get_arguments_dict(['username', 'password'])  #接收username,password
    registerObj =  request.app.component_manager.get_component(HelloComponentTypes.Login)       #ok  #Register = enum_key:               
    response = registerObj.loginProcess(**datas)                     #ok                
    
    timeDuration = now() - start
    return  web.Response(text= response + str(timeDuration))
    
@routes.post('/api/singinpost/user')
async def kkkhello(request): #AioHttpRequest
    #async def hello(request):
           
    dict = await request.get_arguments_dict(['k1', 'k2','k3'])  
    return web.Response(text="Hello, world111111"+f'{dict}'+str(type(dict))) 

@routes.get('/gettt')
async def kkhello(request): #AioHttpRequest
    #async def hello(request):  
    phone_no = await request.get_argument('yyy')
    return web.Response(text="Hello, world111111"+f'{phone_no}'+str(type(phone_no))) 

@routes.post('/dict')
async def kkhello(request): #AioHttpRequest
    #async def hello(request):       
    dict = await request.get_arguments_dict(['k1', 'k2','k3'])  
    return web.Response(text="Hello, world111111"+f'{dict}'+str(type(dict))) 

@routes.get('/api/{key}')
async def OKOKOK(request): #AioHttpRequest
    #async def hello(request):
        #await request.get_argument('phone_no')      
    restful = request.match_info.get('key') 
    return web.Response(text="Hello, world111111"+f'{restful}'+str(type(restful))) 

@routes.post('/api/{key}')
async def kkhello(request): #AioHttpRequest
    #async def hello(request):
        #await request.get_argument('phone_no')      
    restful = request.match_info.get('key') 
    return web.Response(text="Hello, world111111"+f'{restful}'+str(type(restful))) 

@routes.post('/api/yahoo/{key}')
async def yahoo(request): #AioHttpRequest
    #async def hello(request):
        #await request.get_argument('phone_no')      
    restful = request.match_info.get('key') 
    return web.Response(text="Hello, world111111"+f'{restful}'+str(type(restful))) 


    
@routes.post('/hello')
async def kkhello(request): #AioHttpRequest
    #async def hello(request):
        #await request.get_argument('phone_no')
    """
    ---
    tags:
    - hello
    summary: hello world get
    description: simple test controller
    produces:
    - text/html
    responses:
        200:
            description: return hello message
            
            +"f'{dblist}'"
            
            我有包兩種我用起來比較方便的，
            一種是取單個 await request.get_argument('role'), 
            一種是多個會幫你把要的挑出來弄成 dict, 
            await request.get_arguments_dict(['arg1', 'arg2', 'arg3'])
            不過這是取body 的參數
            
            ，你的情況 get 是用 query 取 參數
            如果是 restful 要用  request.match_info.get('key')
    """


    columnDict = await request.get_arguments_dict(['name', 'version','author','date','remark'])  

    return web.Response(text="Hello, world111111"+f'{columnDict}'+str(type(columnDict)))


@routes.get('/haha')
async def kkhello(request):
    """
    ---
    tags:
    - hello
    summary: hello world get
    description: simple test controller
    produces:
    - text/html
    responses:
        200:
            description: return hello message
            
            +"f'{dblist}'"
    """
    
    import pymongo
    from pymongo import MongoClient
    
    return web.Response(text="haha, world99999")

    myclient = pymongo.MongoClient("mongodb://username:pw@localhost:27017")
    dblist = myclient.list_database_names()




