import logging
import sys
import unittest

import docker
import main

logger = logging.getLogger()
logger.level = logging.INFO
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class MyTestCase(unittest.TestCase):

    def setUp(self):
        stream_handler.stream = sys.stdout
        self.client = docker.from_env()

    def test_01_positive_docker_build(self):
        logging.getLogger().info("positive docker build")
        main.docker_build(self.client, 'C:\\Users\\Tansu\\PycharmProjects\\pythonProject\\docker', 'takbay/unittest')
        image = self.client.images.get('takbay/unittest')
        self.assertIsNotNone(image.id)
        logging.getLogger().info(image.id)

    def test_02_docker_build_BuildError(self):
        self.assertIsNone(main.docker_build(self.client, 'C:\\Users\\Tansu\\PycharmProjects\\pythonProject', 'takbay/unittest'))
        # docker.errors.BuildError: {'message': 'Cannot locate specified Dockerfile: Dockerfile'}
        # self.assertRaises(docker.errors.BuildError, main.docker_build(self.client, 'C:\\Users\\Tansu\\PycharmProjects\\pythonProject'))

    def test_03_docker_build_TypeError(self):
        self.assertRaises(TypeError, main.docker_build(self.client, 'C:\\Users\\Tansu\\PycharmProjects\\pythonProject\\aaa.txt', 'takbay/unittest'))

    def test_04_positive_docker_push(self):
        logging.getLogger().info("positive docker build")
        try:
            main.docker_push(self.client, 'takbay/unittest')
        except:
            self.assertTrue(False)
        else:
            logging.getLogger().info("positive docker build passed")
            pass

    def test_05_negative_docker_push(self):
        # When passing wrong login credentials?
        # self.assertRaises(docker.errors.APIError, main.docker_push(self.client, 'test'))
        pass


if __name__ == '__main__':
    unittest.main()
