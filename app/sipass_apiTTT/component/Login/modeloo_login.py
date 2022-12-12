from hyssop.project.component import Component

from ..singup_orm import hash_PWD ,create_session,Signup

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

class LoginComponent(Component):
    def init(self, component_manager, p1, *arugs, **kwargs) -> None:
        print('init Login component load from', __package__, 'and the parameters p1:', p1)
       
    async def loginProcess(self,**datas):
        session = create_session()
        username_exist =await session.query(Signup).filter(Signup.username == datas['username'],).all() 
        if username_exist:  #確認有此username
            check_PWD = await session.query(Signup).filter(Signup.hash_password == hash_PWD(datas['password']),).filter(Signup.username == datas['username'],).all()  
            if check_PWD:  #確認有此密碼的hash_password
                
                update_time = {"update_time": datetime.now()}       #登入的時間
                session.query(Signup).filter_by( username = datas['username']).update(update_time)
                session.commit()
                session.close()
                return  '{"登入資訊":"'+datas['username']+'已登入"}'
            else:   
               return  '{"登入資訊":"password輸入錯誤"}'        
        else:        
            return  '{"登入資訊":"沒有此帳號"}'     