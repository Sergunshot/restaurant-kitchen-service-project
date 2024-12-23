# restaurant-kitchen-service-project

Project for managing local restaurant.

## Check it out!

[restaurant-kitchen-service-project deployed to Render](https://restaurant-kitchen-service-ei7n.onrender.com/)


- Use the following command to load prepared data from fixture to see the site features:
  
`python manage.py loaddata dump.json`

- Before start server use the following command to collect static files:

`python manage.py collectstatic`

- After loading data from fixture you can use following test user (or create another one by yourself):
  - Username: `Sergiy`
  - Password: `2202`

## Installation

Python3 must be already installed

```shell
git clone https://github.com/Sergunshot/restaurant-kitchen-service-project.git
cd service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver # starts Django server
```


## Features


* Authentication functionality for Cook/User
* Managing dish types, ingredients, dishes & cooks directly from the website interface
* Powerful admin panel for advanced managing


# Demo 

![Website Interface](demo.png)
