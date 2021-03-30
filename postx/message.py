from collections import OrderedDict


class Messsage(object):
    def __init__(self):
        self.message = OrderedDict()
        self._elementTotal = 0

    def text(self, msg):
        self.message.update({str(self._elementTotal): {'text': msg}})
        self._elementTotal += 1
        return self

    def title(self, title):
        self.message.update({str(self._elementTotal): {'title': title}})
        self._elementTotal += 1
        return self

    def link(self, text, link):
        self.message.update({str(self._elementTotal): {'link': [text, link]}})
        self._elementTotal += 1
        return self

    def sub_title(self, sub):
        self.message.update({str(self._elementTotal): {'sub': sub}})
        self._elementTotal += 1
        return self

    def get_message(self):
        return self.message
