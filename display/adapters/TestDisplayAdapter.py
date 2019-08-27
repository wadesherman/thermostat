from ..DisplayAdapterInterface import DisplayAdapterInterface


class TestDisplayAdapter(DisplayAdapterInterface):
    refresh_interval = 10

    def update(self):
        print("foo")
