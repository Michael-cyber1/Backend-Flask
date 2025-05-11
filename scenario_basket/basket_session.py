from flask import session


def add_to_basket(items):
    basket = session.get('basket', [])
    for item in items:
        basket.append(item)
    session['basket'] = basket


def clear_basket():
    if 'basket' in session:
        session.pop('basket')
