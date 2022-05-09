# This script is the simpler solution without using argparse


import docker


def docker_build(client, path_to_Dockerfile, tag_name):
    print('Starting docker build with Dockerfile in ', path_to_Dockerfile)
    try:
        client.images.build(path=path_to_Dockerfile, tag=tag_name)
    except Exception as e:
        #logging.error(traceback.format_exc())
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


if __name__ == '__main__':
    dockerfile_path = 'C:\\Users\\Tansu\\PycharmProjects\\pythonProject\\docker'
    var_client = docker.from_env()
    docker_build(var_client, dockerfile_path, 'takbay/restfuldocker')
    docker_push(var_client, 'tansu/test')
