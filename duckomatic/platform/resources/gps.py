from duckomatic.utils.resource import Resource


class Gps(Resource):

    def __init__(self, *vargs, **kwargs):
        super(Gps, self).__init__(*vargs, **kwargs)

    def get_message_to_publish(self):
        return ('feed', {'data': 'gpsdata'})

    def start(self):
        self.start_polling_for_messages_to_publish(0.2)
