from db_manager import DBManager
from weather import Weather
import create_csv
from squirrel_db_manager import SquirrelDBManager

db = DBManager.get_instance()
data = db.get_weathers()

for w in data:
    print(f"DAY={w.day}, TEMP={w.temp}, CONDITION={w.condition}")

print(db.get_average_temp)

print(db.get_max_temp)
# convert from numpy.int64 to int
print(type(db.get_max_temp.item()))

print(db.get_monday)

print(db.get_max_temp_data)

create_csv.create_csv_v1()
create_csv.create_csv_v2()

squ_db = SquirrelDBManager.get_instance()
squ_db.create_csv_for_fur_colors()

