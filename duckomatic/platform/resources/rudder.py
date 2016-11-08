import logging
from os.path import (dirname, abspath, join)
import sys
import time
from duckomatic.utils.resource import Resource
sys.path.append(join(dirname(dirname(dirname(dirname(abspath(__file__))))),
                     'submodules', 'Adafruit_Python_PCA9685'))
import Adafruit_PCA9685


class Rudder(Resource):
    SERVO_MIN = 150  # Min pulse length out of 4096.
    SERVO_MAX = 600  # Max pulse length out of 4096.
    SERVO_CHANNEL = 0
    RUDDER_KEY = 'rudder'
    MIN_RUDDER = 0
    MAX_RUDDER = 10

    def __init__(self, *vargs, **kwargs):
        super(Rudder, self).__init__(*vargs, **kwargs)
        self._pwm = Adafruit_PCA9685.PCA9685()

    def handle_incoming_message(self, topic, data):
        logging.debug('Received message on topic "%s": %s' % (topic, data))

        # Ensure the rudder value is given in the data.
        if self.RUDDER_KEY not in data:
            logging.info('Rudder data does not contain %s key' %
                         self.RUDDER_KEY)
            return

        # Validate the requested rudder value.
        rudder = self.validate_rudder(data[self.RUDDER_KEY])

        # Make the servo move.
        self._pwm.set_pwm(self.SERVO_CHANNEL, 0, self.get_servo_value(
            rudder, self.MIN_RUDDER, self.MAX_RUDDER, self.SERVO_MIN,
            self.SERVO_MAX))
        time.sleep(1)

    @staticmethod
    def validate_rudder(rudder, min_rudder, max_rudder):
        """ Validate the rudder value is between min_rudder and max_rudder. """
        if rudder < min_rudder:
            logging.warning('Rudder value %d less than minimum value of %d. \
Setting to minimum.' % (rudder, min_rudder))
            rudder = min_rudder
        if rudder > max_rudder:
            logging.warning('Rudder value %d greater than maximum value of \
%d. Setting to maximum.' % (rudder, max_rudder))
            rudder = max_rudder
        return rudder

    @staticmethod
    def get_servo_value(rudder, min_rudder, max_rudder, servo_min, servo_max):
        """ Calcuate the servo value for the given rudder value. """
        return servo_min + \
            int((float(rudder - min_rudder) / float(max_rudder - min_rudder))
                * (servo_max - servo_min))

    def start(self):
        self.start_processing_incoming_messages()
