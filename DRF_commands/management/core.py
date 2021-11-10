from django.conf import settings
import os

def generate(appName,viewName,postfix,skullTextfile,optURL):
    BASE_DIR = settings.BASE_DIR
    skull = open(skullTextfile, "r")
    if (not os.path.isfile(str(BASE_DIR / appName) + "/views/" + viewName.capitalize() + '.py')):
        with open(str(BASE_DIR / appName) + "/views/" + viewName.capitalize() + '.py', 'w') as f:
            s = skull.read().replace("{{className}}", viewName.capitalize())
            f.write(s)
            f.close()
        with open(str(BASE_DIR / appName) + "/views/__init__.py", 'a+') as f:
            f.write("from ." + viewName.capitalize() + " import " + viewName.capitalize() +postfix+"\n")
            f.close()
            skull.close()
        with open(str(BASE_DIR / appName) + "/urls.py", 'a+') as f:
            p0 = "\nurlpatterns+=[path('" + viewName + "/',views." + viewName.capitalize() +postfix+".as_view(),name='"+postfix+"-" + viewName + "'),]"
            p1 = "\nurlpatterns+=[path('" + viewName + "/<int:pk>',views." + viewName.capitalize() +postfix+".as_view(),name='"+postfix+"-pk-" + viewName + "'),]"
            if(optURL==1):
                f.write(p0)
            if(optURL==2):
                f.write(p1)
            if(optURL==3):
                f.write(p0)
                f.write(p1)
            f.close()
    else:
        print("The file " + viewName.capitalize() + ".py already exists !")