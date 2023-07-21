import click
import os
import sys
import build
import int


@click.group()
def cli():
    pass

@click.command()
@click.argument("folder", type=click.Path(exists=False), required=1)
@click.option("-n", "--name", prompt="Name of the project", help="The name of the project API to generate.")
@click.option("-p", "--package", prompt="Package of the project", help="The package of the project API to generate.")
@click.option("-d", "--desc", prompt="Description of the project", help="The description of the project API to generate.")
def generate(name, desc, package, folder):
    """Generate a new Spring API project."""
    
    # Check if the folder is empty sinon error
    if os.path.exists(folder):
        if os.listdir(folder):
            sys.exit(f"Error: {folder} is not empty") 
    else:
        click.confirm("Do you want to create the folder?", abort=True)
        os.makedirs(folder)

    click.echo(f"Destination folder: {folder}")
    click.echo(f"Generating a new Spring API project")
    click.echo(f"Name: {name}")
    click.echo(f"Description: {desc}")

    # Demarre un docker pour générer le projet Spring
    absolute_path = os.path.abspath(folder)
    image_name = "spring-workspace:latest"
    build.start_environment(click, image_name, absolute_path, name, package)




@click.command()
@click.argument("project_path", type=click.Path(exists=False), required=1)
@click.argument("project_name", type=click.Path(exists=False), required=1)
def start(project_path, project_name):
    absolute_path = os.path.abspath(project_path)
    image_name = "spring-workspace:latest"
    int.start(click, absolute_path, project_name, image_name)


cli.add_command(generate)
cli.add_command(start)


if __name__ == "__main__":
    cli()