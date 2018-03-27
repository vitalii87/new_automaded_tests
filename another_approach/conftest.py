import pytest
from book_app import BookApp


@pytest.fixture()
def app():
    app = BookApp()
    yield app
    app.destroy()

@pytest.fixture()
def login(app):
    #login
    app.first_page.username_filed.send_keys('anna@nxte.nl')
    app.first_page.password_filed.send_keys('pass')
    yield
    app.internal_page.logout_button.click()