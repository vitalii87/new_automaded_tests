import pytest
from book_app import BookApp


@pytest.fixture()
def app():
    app = BookApp()
    yield app
    app.destroy()
