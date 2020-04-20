# Movie Scrapper and Rating API
Scrap movie data from wikipedia, give rating from CSV data source, finally serve the information using API 

This project uses `pipenv` as a package management tool. If you don't have `pipenv` installed, then install it by

``` bash
pip install pipenv
```

### Quick Start Using Pipenv

``` bash
# Activate virtual env
$ pipenv shell

# Install dependencies
$ pipenv install
```

### To Create Freash Database
``` bash
$ python
>> from app import db
>> db.create_all()
>> exit()
```

### Scrapping Wikipedia And Insert To Database
``` bash
$ python scrapper.py OPTIONAL_LIMIT
# Example: python scrapper.py 50
# OPTIONAL_LIMIT decides how many list item should be scrapped
# Omit OPTIONAL_LIMIT if you want scrap full list
```

### Update Database With CSV
``` bash
$ python csvhandler.py
```

### Serve API 
``` bash
$ python app.py
# Link http://localhst:5000
```

### API Endpoints

* GET     /movies
* GET     /movies?count=20&page=3
* GET     /movie/:id
* POST    /movie
* PUT     /movie/:id
* DELETE  /movie/:id