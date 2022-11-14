
from flask import render_template
from flask_paginate import Pagination, get_page_args

from pprint import pprint

from ..models.Cliente import Cliente
from app.forms import SendForm

class ClientesController:

    def index(self):

        cliente = Cliente()  
        result_list = []

        clientes_devedores = cliente.getClientesDevedores()

        for res in clientes_devedores:
            result_list.append(res)


        page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')

        total = len(result_list)

        clientes_in_page = self.clientes_per_page(result_list, offset, per_page)

        pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap5')

        form = SendForm()

        return render_template('pages/clientes.html', 
            clientes=clientes_in_page,
            page=page,
            per_page=per_page,
            pagination=pagination,
            form=form)

    def clientes_per_page(self, clientes=[], offset=0, per_page=10):
        return clientes[offset: offset + per_page]