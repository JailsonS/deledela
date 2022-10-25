from mvc_flask import Router

Router.get("/login", "auth#login")
Router.post("/login", "auth#do_login")
