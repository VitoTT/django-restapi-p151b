# p151a

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
    /accounts/api/users
    /accounts/api/users/{id}
cars:
    /cars/api/carbrands/
    /cars/api/carbrands/{id}
    /cars/api/carmodels/
    /cars/api/carmodels/{id}
    /cars/api/usercars/
    /cars/api/usercars/{id}

example requests:
    $ curl http://localhost:8000/accounts/api/users/?username=vito; echo -e "\n"
    $ curl http://localhost:8000/accounts/api/users/3/ echo -e "\n"
    $ curl http://localhost:8000/cars/api/carbrands/; echo -e "\n"
    $ curl -d '{"name":"LADA"}' -H "Content-Type: application/json" -X POST http://localhost:8000/cars/api/carbrands/