import logging

from apps.twitter import twitter
import pytest
from pytest_bdd import scenario, given, when, then

from common.methods import ClientData


@pytest.fixture()
def url():
    return "https://twitter.com"


@pytest.fixture()
def client():
    client = ClientData()
    yield client


@scenario('twitter_register_user.feature', 'new user', features_base_dir='tests/bdd_tests/features')
def test_start_test(page):
    logging.debug("starting test")


@given('a new user wants to register', target_fixture=url)
def go_to_site(page):
    twitter.launch(page)


@when('they navigate to home landing page')
def verify_site(page, url):
    assert url in page.url


@then('they can register')
def register(page):
    twitter.login_page.register(page)
