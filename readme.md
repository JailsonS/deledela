### Requisitos

- python 3.9^

### Estrutura do projeto
O projeto está codificado no padrão Model(M)-View(V)-Controller(C)
```
project
│   readme.md
│   log_notificacoes.txt - armazena o log de envios de mensagens
│   requirements.txt - libs externas a serem instaladas
└───app
│   └───controllers
│   └───models
|   └───static
|   └───utils
|   └───views 
```

### criar ambiente virtual env
`python -m venv ./venv `

### habilitar ambiente virtual env
- para windows
    `. venv/Scripts/activate` <br>
- para linux
    `. venv/bin/activate` <br>

## Instalar libs externas
`pip install -r requirements.txt`

### Executar a aplicação
`flask run`

Acessar localhost:5000/home