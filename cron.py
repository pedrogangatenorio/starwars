import os
from django.core.wsgi import get_wsgi_application
os.environ['DJANGO_SETTINGS_MODULE'] = 'starwars.settings'
application = get_wsgi_application();

from films.services import filmservice
from starwars.settings import FILMENTITY, PEOPLENTITY
import schedule
import time

def my_scheduled_job():
	filmservice.getEntityModel(FILMENTITY);
	filmservice.getEntityModel(PEOPLENTITY);

schedule.every(24).hours.do(my_scheduled_job) ;

while True: 
    schedule.run_pending();
    time.sleep(1);

