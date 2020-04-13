from lib.db_manager import db_manager
from lib.settings import *
__URL = "https://api.covid19api.com/summary"
db_object = db_manager(host, user, passwd, database, __URL)
covid_19_data = db_object.get_all_data()
db_object.save_all_data(covid_19_data)
