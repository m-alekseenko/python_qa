#-*- encoding: utf-8 -*-
import unittest
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    # initialization fixture
    fixture = Application()
    # destroy fixture
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
   app.login(username="admin", password="secret")
   app.create_group(Group(name="test group", header="some header text", footer="some footer text"))
   app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

