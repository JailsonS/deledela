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

### Orientações ao usuário

<p>Ao acessar a url `localhost:5000/home`o usuário irá visualizar um painel com indicadores 
a respeito dos clientes e suas respectivas parcelas. O usuário precisará clicar no botão `enviar notificações` e a 
aplicação abrirá um navegador para envio de mensagens. Para isso, será necessário que o número habilitado para envio 
esteja logado no whatsapp web. Assim o sistema reconhecerá o número e irá iniciar o envio.</p>
<p>
    As notificações de envio de mensagens estão programadas para serem enviadas de 15 em 15s, com o limite de 500 mensagens por dia para evitar bloqueio do número. Ao enviar uma mensagem, as informações do envio são gravadas em um arquivo de log onde é possível identificar o cliente, a data e máquina de onde partiu o envio. O sistema possui uma regra de que não é possível enviar mais de 1 notificação de cobrança para o mesmo cliente no mesmo mês, isso também é outra forma de prevenção contra bloqueio do número de celular.
</p>