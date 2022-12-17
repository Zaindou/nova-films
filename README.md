# novafilms

## Description

This is a simple web application that allows users to search for movies, documentaries and series.

Alternova technical test.

Made with Django Rest Framework, VueJs, Tailwind and DaisyUI.

## Installation

### Backend

1. Create a virtual environment

```bash

python3 -m venv venv

```

2. Activate the virtual environment

```bash

source venv/bin/activate

```

3. Install the requirements

```bash

pip install -r requirements.txt

```

4. Run the migrations

```bash

python manage.py migrate

```

5. Run the server

```bash

python manage.py runserver

```

### Frontend

1. Install the dependencies

```bash

npm install

```

2. Run the server

```bash

npm run serve

```

## Usage

1. Create a superuser

```bash

python manage.py createsuperuser

```

2. Go to the admin panel

```bash

http://localhost:8000/admin/

```

Go to the movies section and add some movies, documentals and series.
 
