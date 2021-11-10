from django.core.management.base import BaseCommand
from ..core import generate
from pathlib import Path
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("AppName",type=str)
        parser.add_argument("viewName",type=str)

    def handle(self, *args, **options):
        CURRENT_DIR=Path(__file__).resolve().parent
        generate(options["AppName"],options["viewName"],"Retrieve",CURRENT_DIR/"RetrieveAPIView.txt",2)
