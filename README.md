    # Talk to the GitHub API

## Description

Using OAuth and the GitHub API, allow people to log into GitHub and get a list of their repositories.

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* The basics of OAuth

## Details

### Deliverables

* A Git repo called github-api containing at least:
  * `README.md` file explaining how to run your project
  * a `requirements.txt` file
  * a suite of tests for your project

### Requirements  

* Passing unit tests
* No PEP8 or Pyflakes warnings or errors

## Normal Mode

First, go to [the applications section of your GitHub preferences](https://github.com/settings/applications) and register a new application. The callback URL should be a URL you will create for logging in users via GitHub. `/login/github/authorized` is recommended if you don't have a preference.

Using either [Flask-OAuthlib](https://flask-oauthlib.readthedocs.org/) or [Flask-Dance](http://flask-dance.readthedocs.org/en/latest/), write an application that lets a user log in via GitHub and shows all their repositories.

## Hard Mode

In addition to the requirements from **Normal Mode**:

* Add pagination to allow seeing repositories in groups of 30.
* Add the ability to change a repo's description.

