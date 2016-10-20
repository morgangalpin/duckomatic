from duckomatic.utils.resource import Resource


class Throttle(Resource):

    def __init__(self, *vargs, **kwargs):
        super(Throttle, self).__init__(*vargs, **kwargs)

    def get_message_to_publish(self):
        return ('feed', {'data': 'throttle data'})

    def start(self):
        self.start_processing_incoming_messages()
