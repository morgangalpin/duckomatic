from duckomatic.utils.publisher import Publisher
from duckomatic.utils.subscriber import Subscriber


class Resource(object):

    def __init__(self, *vargs, **kwargs):
        super(Resource, self).__init__(*vargs, **kwargs)
        self._publisher = Publisher()
        self._subscriber = Subscriber()

    def get_publisher(self):
        return self._publisher

    def get_subscriber(self):
        return self._subscriber
