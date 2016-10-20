from duckomatic.utils.resource import Resource


class Rudder(Resource):

    def __init__(self, *vargs, **kwargs):
        super(Rudder, self).__init__(*vargs, **kwargs)

    def get_message_to_publish(self):
        return ('feed', {'data': 'rudder data'})

    def start(self):
        self.start_processing_incoming_messages()
