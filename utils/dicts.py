def get_val(collection, key, default='git'):
    """Возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default.
    """
    return collection.get(key, default)
