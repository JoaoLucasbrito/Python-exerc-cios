tipo_usuario = input("Qual é seu cargo? admin, Supervisor, Op")
status = input("A sua conta esta ativa ou bloquada? Ativa/Bloq")

if status == "ativa":
    if tipo_usuario == "admin":
        print("Acesso total")
    elif tipo_usuario == "supervisor":
        print("Acesso gerecial")
    else:
        print("Acesso opacional")
else:
    print("acesso negado")