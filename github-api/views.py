from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from . import oauth
from . import app

github = oauth.remote_app("github",
    base_url="https://api.github.com",
    request_token_url=None,
    access_token_method="POST",
    authorize_url="https://github.com/login/oauth/authorize",
    access_token_url="https://github.com/login/oauth/access_token",
    app_key="GITHUB",
    request_token_params={"scope": "user:email, repo"})


@app.route("/github/login")
def login():
    return github.authorize(callback=url_for("oauth_authorized",
        next=request.args.get("next") or request.referrer or None))

@app.route("/github/oauth-authorized")
def oauth_authorized():
    next_url = request.args.get("next") or url_for("index")
    resp = github.authorized_response()
    if resp is None:
        flash("Why you not sign in?")
        return redirect(next_url)

    session["github_token"] = (
        resp["oauth_token"],
        resp["oauth_token_secret"]
    )
    session["github"] = resp["screen_name"]

    flash("You have signed in as %s" % resp["screen_name"])
    return redirect(next_url)