from django import template
 
register = template.Library()
 
@register.filter(name='saludo')
def saludo(valor):
    return f"<h1 style='background:#00ffff; color:white;'> Sea Bienvenido, {valor} </h1>"