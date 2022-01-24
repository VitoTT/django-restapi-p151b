# p151b

# Linux
sudo apt-get install python3-venv    # If needed  
python3 -m venv .venv  
source .venv/bin/activate  

# macOS
python3 -m venv .venv  
source .venv/bin/activate  

# Windows
py -3 -m venv .venv  
.venv\scripts\activate  

# run the below lines
python -m pip install --upgrade pip  
pip install -r requirements.txt  
python manage.py makemigrations    # uncomment sqlite DB settings in 'settings.py' if postgres is not available  
python manage.py migrate  

# REST API endpoints
accounts:  
    /accounts/api/users/  
    /accounts/api/users/{id}/  
cars:  
    /cars/api/carbrands/  
    /cars/api/carbrands/{id}/  
    /cars/api/carmodels/  
    /cars/api/carmodels/{id}/  
    /cars/api/usercars/  
    /cars/api/usercars/{id}/  

example requests:
    $ curl http://localhost:8000/accounts/api/users/?username=vito; echo -e "\n"  
    $ curl http://localhost:8000/accounts/api/users/3/ echo -e "\n"  
    $ curl http://localhost:8000/cars/api/carbrands/; echo -e "\n"  
    $ curl -d '{"name":"LADA"}' -H "Content-Type: application/json" -X POST http://localhost:8000/cars/api/carbrands/  
    $ curl -d '{"name":"LADA"}' -H "Content-Type: application/json" -X POST https://django-restapi-p151b.herokuapp.com/cars/api/carbrands/  

# DB valid requests example

SELECT 
  accounts_user.username, 
  cars_carbrand.name AS brand, 
  cars_carmodel.name AS model, 
  cars_usercar.odo AS odometer 
FROM 
  accounts_user 
  JOIN cars_usercar ON accounts_user.id = cars_usercar.user_id 
  JOIN cars_carbrand ON cars_carbrand.id = cars_usercar.car_brand_id 
  JOIN cars_carmodel ON cars_carmodel.id = cars_usercar.car_model_id;