## Installation

### Clone project
```bash
git clone https://github.com/DHushchin/django-intro
```

## Usage

- Go to the necessary directory lab

### Create virtual environment
```bash
python -m venv venv
```

### Activate it
```bash
venv\Scripts\activate (Windows)
source venv/bin/activate (MacOS)
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Create .env
- create **.env** file in lab directory
- copy data from **.env.example** file to **.env**
- fill empty fields with your credentials

### Running
```bash
python ./src/menu.py
```

## Running lab4

```bash
cd lab4
pip install -r requirements.txt
python server.py
```

## Running lab5

```bash
cd lab5
pip install -r requirements.txt
python manage.py runserver
```