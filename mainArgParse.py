# This script contains the approach with argparse (giving the path as parameter by executing it with the console)

import argparse
from pathlib import Path

import docker


def create_parser():
    var_argparser = argparse.ArgumentParser()
    var_argparser.add_argument('path', type=Path, help='Path to the Dockerfile')
    return var_argparser.parse_args()


def arg_parser(argparser):
    if argparser.path.exists():
        print('The path ', argparser.path, ' does exist.')
        return str(argparser.path)
    else:
        print('The path ', argparser.path, ' does not exist. Exiting script')
        return None


def docker_build(client, path_to_Dockerfile, tag_name):
    print('Starting docker build with Dockerfile in ', path_to_Dockerfile)
    try:
        client.images.build(path=path_to_Dockerfile, tag=tag_name)
    except Exception as e:
        # logging.error(traceback.format_exc())
        print('Build failed')
        return None
    else:
        print('Successfully built')


def docker_push(client, repo):
    print('Starting docker push')
    try:
        client.api.push(repository=repo)
    except docker.errors.APIError:
        return None
    else:
        print('Successfully pushed')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = create_parser()
    dockerfile_path = arg_parser(parser)
    if dockerfile_path is None:
        print('Exiting script.')
        # exit()
    else:
        var_client = docker.from_env()
        docker_build(var_client, dockerfile_path, 'takbay/restfuldocker')
        docker_push(var_client, 'tansu/test')
