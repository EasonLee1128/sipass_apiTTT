from hyssop.project.component import ComponentTypes, ConfigComponentValidator

from hyssop.project.config_validator import ConfigContainerMeta, ConfigElementMeta

# add hello validator to component config validator
ConfigComponentValidator.set_cls_parameters(
    ConfigContainerMeta('Register', False,
        ConfigElementMeta('p1', str, True) # validate HelloComponent's 'p1' argument is required and string type
    )
)  #驗證格式用的

class HelloComponentTypes(ComponentTypes):
    Hello = ('hello', 'hello', 'HelloComponent')
    
    Register = ('Register', 'model_Register', 'RegisterComponent') 
    Login = ('Login', 'Login.modeloo_login', 'LoginComponent') #'Login.modeloo_login' 這樣可抓Login目錄下的modeloo_login
    

#class LoginComponentTypes(ComponentTypes): #這樣寫也可以, project_config.yml component 要有Login
#        Login = ('Login', 'modeloo', 'LoginComponent')