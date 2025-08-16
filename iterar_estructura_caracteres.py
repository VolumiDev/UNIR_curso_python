def extraer_info(email):
    if '@' not in email:
        return {}
    user, resto = email.split('@')
    dominio, extension = resto.split('.')
    return {
        "nombre_usuario": user,
        "dominio": dominio,
        "extension": extension
    }

print(extraer_info("hola@google.com"))