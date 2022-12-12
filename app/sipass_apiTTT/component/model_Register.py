from hyssop.project.component import Component

from . import HelloComponentTypes
#from .__init__ import LoginComponentTypes

from .singup_orm import hash_PWD ,create_session,Signup

#from component.singup_orm import hash_PWD ,create_session,Signup

from datetime import datetime
from aiohttp import web

    #from hyssop_aiohttp import AioHttpRequest, AioHttpView, routes, server


    #class HelloComponent(Component):
#    def init(self, component_manager, p1, *arugs, **kwargs) -> None:
#        print('init Hello component load from', __package__, 'and the parameters p1:', p1)
#
#    def hello(self):
#        return 'Hello World, This is hyssop generate hello component'
#    
#    def get_datas(self,datas):
#        return datas

class RegisterComponent(Component):
    def init(self, component_manager, p1, *arugs, **kwargs) -> None:
        print('init register component load from', __package__, 'and the parameters p1:', p1)
       
    def registerProcess(self,**datas):
        
        if  len(datas['username']) > 55 or len(datas['password']) > 55:
            return '{"註冊資訊":"密碼or帳號>55字元,請重新輸入"}'    
        else:
            datas['hash_password'] = hash_PWD(datas['password'])                  #接收username,password  
            datas['create_time'] = datetime.now()                                 #增加 create_time 欄位
            datas['update_time'] = datetime.now()                                 #增加 update_time 欄位 
            del datas['password']                                                 #刪除 password 欄位               

            session =  create_session()
            username_exist =  session.query(Signup).filter(Signup.username == datas['username'],).all() 
            if username_exist:  #確認有username = datas['username']的資料
                return  '{"註冊資訊":"已有此帳號"}'             
            else: #print("username_exist is empty.just singup to dataDB")   
                session.add(Signup(**datas))
                session.commit()
                session.close()
                username_exist = session.query(Signup).filter(Signup.username == (datas['username']),).all() 
                if username_exist:   #print("username_exist is not empty") 
                   return '{"註冊資訊":"'+datas["username"]+'註冊完成"}'+f"{datas}"     
                else:   
                   return  '{"登入資訊":"沒有此帳號"}'

 