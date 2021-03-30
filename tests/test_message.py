from postx.message import Messsage    # noqa
import pytest


@pytest.fixture()
def message():
    return Messsage()


def test_message_default_length(message):
    assert len(message.get_message()) == 0


def test_message_counter_length(message):
    assert message._elementTotal == 0


def test_message_add_text_key(message):
    message.text('a')
    assert 'text' in message.get_message()['0']


def test_message_add_text_value(message):
    message.text('a')
    assert 'a' in message.get_message()['0'].values()


def test_message_add_title_key(message):
    message.title('a')
    assert 'title' in message.get_message()['0']


def test_message_add_title_value(message):
    message.title('a')
    assert 'a' in message.get_message()['0'].values()


def test_message_add_subtitle_key(message):
    message.sub_title('a')
    assert 'sub' in message.get_message()['0']


def test_message_add_subtitle_value(message):
    message.sub_title('a')
    assert 'a' in message.get_message()['0'].values()


def test_message_add_link_key(message):
    message.link('a', 'http://google.com')
    assert 'link' in message.get_message()['0']


def test_message_add_link_value_length(message):
    message.link('a', 'http://google.com')
    assert len(message.get_message()['0']['link']) == 2


def test_message_add_link_value_text(message):
    message.link('a', 'http://google.com')
    assert 'a' in message.get_message()['0']['link'][0]


def test_message_add_link_value_link(message):
    message.link('a', 'http://google.com')
    assert 'http://google.com' in message.get_message()['0']['link'][1]