
from spectator import GlobalRegistry

#setup
class TimerExample:

    def __init__(self, registry=GlobalRegistry):
        self._registry = registry
        self._requestLatency = registry.timer('server.requestLatency')
    #setup

    #using-with
    def handle_using_with(self, request):
        with self._requestLatency.stopwatch():
            return self._handle_impl(request)
    #using-with

    #explicitly
    def handle_explicitly(self, request):
        start = self._registry.clock().monotonic_time()
        try:
            return self._handle_impl(request)
        finally:
            end = self._registry.clock().monotonic_time()
            self._requestLatency.record(end - start)
    #explicitly

    def _handle_impl(self, request):
        # do something useful
        return None
