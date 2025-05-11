from flask import session, request, current_app
from functools import wraps


def group_validation(sess: session) -> bool:
    group = session.get('group_name', None)
    if group is not None and group != '':
        return True
    return False


def group_permission_validation(config: dict, sess: session) -> bool:
    group = sess.get('group_name', 'unauthorized')
    target_app = "" if len(request.endpoint.split('.')) == 1 else request.endpoint.split('.')[0]
    if group in config and target_app in config[group]:
        return True
    else:
        return False

'''
def mydecor(f):
    def wrapper(*args, **kwargs):
        print('Before')
        return f(*args, **kwargs)
    return wrapper


def sum_(a, b):
    return a + b


sum_d = mydecor(sum_(1, 2))
'''

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if group_validation(session):
            return f(*args, **kwargs)
        return 'Permission denied'
    return wrapper


def login_permission_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if group_permission_validation(current_app.config['ACCESS_CONFIG'], session):
            return f(*args, **kwargs)
        return 'Group permission denied'
    return wrapper