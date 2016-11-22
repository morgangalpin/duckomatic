import logging
import os
from duckomatic.utils.resource import Resource


class Camera(Resource):

    def __init__(self, image_dir, image_format='%d.jpg',
                 fake=False, *vargs, **kwargs):
        super(Camera, self).__init__(*vargs, **kwargs)
        self._image_num = 0
        self._image_dir = image_dir
        self._image_format = image_format
        self._fake = fake

    def get_message_to_publish(self):
        self._image_num += 1

        # Save the current image to the next file number.
        self._camera.capture(os.path.join(
            self._image_dir, self._image_format % (self._image_num)))

        # Notify listeners of the new image.
        return ('feed', {
            'image_id': self._image_num
        })

    def start(self):
        # Initialize the camera object.
        if self._fake:
            self._camera = FakePiCamera()
        else:
            # https://github.com/waveform80/picamera
            import picamera
            self._camera = picamera.PiCamera()
            self._camera.resolution = (320, 240)
        self.start_polling_for_messages_to_publish(4)


class FakePiCamera(object):
    """ Implements the same interface as the Adafruit_Camera.Camera, but
    none of the methods do anything.
    """

    def __init__(self, *vargs, **kwargs):
        super(FakePiCamera, self).__init__(*vargs, **kwargs)

    def capture(
            self, output, format=None, use_video_port=False, resize=None,
            splitter_port=0, bayer=False, **options):
        logging.debug('FakePiCamera.capture(...)')
