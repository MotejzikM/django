from django import template

register = template.Library()

@register.filter
def has_group(user, group_name):
    """Zkontroluje, zda uživatel patří do určité skupiny."""
    if user.is_authenticated:
        return user.groups.filter(name=group_name).exists()
    return False  # Pokud není přihlášený uživatel, vrátí False
