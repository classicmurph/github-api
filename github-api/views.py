from functools import wraps

from flask import session, Blueprint, url_for, request, redirect, flash, render_template

from .extensions import oauth


facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=410559155795197,
    consumer_secret=f64f456e4558a27416c075b7b9446050
)


@facebook.tokengetter
def get_facebook_token(token=None):
    return session.get('facebook_token')


def require_login(view):
    @wraps(view)
    def decorated_view(*args, **kwargs):
        if 'facebook_token' in session:
            return view(*args, **kwargs)
        else:
            return redirect(url_for("users.login"))

    return decorated_view


users = Blueprint("users", __name__)


@users.route("/login")
def login():
    return render_template("login.html")

@users.route("/logout")
def logout():
    session.pop('facebook_token', None)
    return redirect(url_for("repolister.index"))


@users.route("/facebook/login")
def facebook_login():
    session.pop('facebook_token', None)
    return facebook.authorize(callback=url_for('.facebook_authorized',
                                             _external=True,
                                             next=request.args.get('next') or url_for("repolister.index")))


@users.route('/login/facebook/authorized', methods=["GET", "POST"])
def facebook_authorized():
    next_url = request.args.get('next') or url_for('repolister.index')
    resp = facebook.authorized_response()
    if resp is None:
        flash('You denied the request to sign in.')
        return redirect(next_url)

    session['facebook_token'] = (resp['access_token'],)
    me = facebook.get('/user')
    session['facebook_name'] = me.data['name']

    flash('You were signed in as %s' % repr(me.data['name']))
    return redirect(next_url)

# from .users import require_login, facebook
# from ..pagination import Paginator

repolister = Blueprint("repolister", __name__)


@repolister.route("/")
# @repolister.route("/page/<int:page>")
@require_login
def index():
    resp = facebook.get("/user/repos")

    # paginator = Paginator(resp, page)

    return render_template("index.html",
                        #    paginator=paginator,
