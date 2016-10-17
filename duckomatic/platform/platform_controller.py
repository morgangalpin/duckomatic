import threading
import time


class PlatformController(object):
    """ Main controller for the robot platform.
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self):
        """ Constructor.
        Creates a thread and starts it immediately.
        """
        super(PlatformController, self).__init__()

        self._resources = {}

        self._thread = threading.Thread(target=self.run, args=())
        self._thread.daemon = True
        self._thread.start()

    def run(self):
        """ Method that runs forever """
        count = 0
        while True:
            # Just send a message periodically for now until reading from the
            # queue is in place.
            time.sleep(10)
            count += 1
            # self.update('test', {
            #             'message': 'Server generated event',
            #             'count': count,
            #             'namespace': '/test'
            #             })
            # message = self._messages.get()
            # self.update_observers(message['name'], message['data'])

    def wait_until_finished(self):
        """ Blocks until the main thread is finished. """
        self._thread.join()

    def add_subscriber_to_resource_publisher(self, resource_id, subscriber,
                                             *topics):
        if resource_id in self._resources:
            publisher = self._resources[resource_id].get_publisher()
            publisher.subscribe(subscriber, *topics)

    def add_resource_subscriber_to_publisher(self, resource_id, publisher,
                                             *topics):
        if resource_id in self._resources:
            subscriber = self._resources[resource_id].get_subscriber()
            publisher.subscribe(subscriber, *topics)
