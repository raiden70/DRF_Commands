from django.core.management.base import BaseCommand
from django.conf import settings
import os
from pathlib import Path
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("AppName",type=str)
        parser.add_argument("viewName",type=str)

    def handle(self, *args, **options):
            BASE_DIR = settings.BASE_DIR
            CURRENT_DIR = Path(__file__).resolve().parent

            skull=open(CURRENT_DIR/"APIView.txt","r")
            if(not os.path.isfile(str(BASE_DIR/options["AppName"])+"/views/"+options["viewName"].capitalize()+'.py')):
                with open(str(BASE_DIR/options["AppName"])+"/views/"+options["viewName"].capitalize()+'.py','w') as f:
                    s=skull.read().replace("{{className}}",options['viewName'].capitalize())
                    f.write(s)
                    f.close()
                with open(str(BASE_DIR / options["AppName"]) + "/views/__init__.py",'a+') as f:
                    f.write("from ."+options['viewName'].capitalize()+ " import "+options['viewName'].capitalize()+"List\n")
                    f.write("from ."+options['viewName'].capitalize()+ " import "+options['viewName'].capitalize()+"Detail\n")
                    f.close()
                    skull.close()
                with open(str(BASE_DIR / options["AppName"]) + "/urls.py",'a+') as f:
                    p0="\nurlpatterns+=[path('"+options['viewName']+"/',views."+options['viewName'].capitalize()+"List.as_view(),name='list-"+options['viewName']+"'),]"
                    p1="\nurlpatterns+=[path('"+options['viewName']+"/<int:pk>',views."+options['viewName'].capitalize()+"Detail.as_view(),name='detail-"+options['viewName']+"'),]"
                    f.write(p0)
                    f.write(p1)
                    f.close()
            else:
                print("The file "+ options["viewName"].capitalize()+".py already exists !")
