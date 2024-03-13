### Requirements

- python 3.9^

### Tree folder project
Pattern Model(M)-View(V)-Controller(C)
```
project
│   readme.md
│   log_notificacoes.txt - logs 
│   requirements.txt - requirements
└───app
│   └───controllers
│   └───models
|   └───static
|   └───utils
|   └───views 
```

### create virtual env
`python -m venv ./venv `

### activate virtual env
- windows
    `. venv/Scripts/activate` <br>
- linux
    `. venv/bin/activate` <br>

## Install requirements
`pip install -r requirements.txt`

### Run app
`flask run`

access localhost:5000/home
