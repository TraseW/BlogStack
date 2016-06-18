from flask import Blueprint, render_template

dyn = Blueprint('dyn', __name__, template_folder='templates')


@dyn.route('/projects')
def test():
    return 'test test test test'