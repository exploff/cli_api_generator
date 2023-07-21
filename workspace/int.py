import subprocess

# interaction
# start 
# stop
# delete



def start(click, volume_path, project_name, image_name):

    click.echo(f"Execute this command to connect to your container env :")
    click.echo(f"docker run -it --rm -v {volume_path}\{project_name}:/workspace/workdir -w /workspace/workdir {image_name} bash")




