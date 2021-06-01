user = {
    'id': 1,
    'name': 'jose',
    'role': 'admin'
}


def delete_database():
    print('Database deleted!')


def secure_delete_database():
    dd = delete_database
    deleting_the_database = check_permission(dd)
    return deleting_the_database


def check_permission(func):
    if user.get("role") == "admin":
        return func
    raise PermissionError


print(secure_delete_database())
