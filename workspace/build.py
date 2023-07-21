import docker
import subprocess
# Build de l'image docker spring

def create_image(dockerfile_path, image_name):

    result = subprocess.run(['docker', 'build', '-t', image_name, dockerfile_path],
                            capture_output=True, text=True)
    
    # Vérifie si la commande s'est exécutée avec succès
    if result.returncode == 0:
        print(f"Docker image {image_name} build successfully.")
    else:
        print(f"Error during the build of the docker image {image_name}.")
        print(result.stderr)

def check_image(image_name):
    client = docker.from_env()
    try:
        client.images.get(image_name)
        return True
    except docker.errors.ImageNotFound:
        return False
    
def check_environment_start(container_name):
    client = docker.from_env()
    try:
        client.containers.get(container_name)
        return True
    except docker.errors.NotFound:
        return False
    
def start_container(container_name, image_name, volume_path, project_name, package_name):

    command = f'docker run -it --rm -v {volume_path}:/workspace/workdir -w /workspace/workdir {image_name} bash -c "spring init -d=web,actuator,lombok,devtools -n={project_name} --package-name={package_name} --build=maven {project_name}"'

    result = subprocess.run(command, shell=True, check=True)

    # Vérifie si la commande s'est exécutée avec succès
    if result.returncode == 0:
        print(f"Docker container {container_name} started successfully.")
    else:
        print(f"Error during the start of the container {container_name}.")
        print(result.stderr)


# Start l'image docker spring
def start_environment(click, image_name, volume_path, project_name, package_name):
    dockerfile_path = "./sources"

    if not check_image(image_name):
        click.echo(f"Docker image not present, creating the image, it may take some time...")
        create_image(dockerfile_path, image_name)

    click.echo(f"Start environment with docker image")
    container_name = project_name
    if not check_environment_start(container_name):
        click.echo(f"Starting the docker container...")
        start_container(container_name, image_name, volume_path, project_name, package_name)


