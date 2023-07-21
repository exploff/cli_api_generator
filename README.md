# Ce qui a été fait : 
Une image Dockerfile, qui contient toute la CLI spring lorsqu'on démarre un bash dans le dossier /workspace/workdir

docker run -it --rm -v volume/:/workspace/workdir -w /workspace/workdir spring-workspace bash

# A faire : 
Un script d'initialisation du projet spring
Donner à l'utilisateur le volume avec son projet spring initialisé et lui donner la possibilité de ce connecter en ligne de commande dans le container docker


# Build dev environment

docker build --target dev . -t cli-project
docker run --rm -it -v ${PWD}/workspace:/workspace cli-project sh
python --version


# Projet

Besoin de savoir quoi ?

- Nom du projet 
- Description du projet
- Emplacement du dossier où générer l'API
?- Besoin de l'authentification JWT?
?- Besoin d'une base MySQL ?
Vraiment attention au dockerfile, aux droits etc, 
- Générer le dockerfile et docker-compose (readme + commande)
- Emplacement du fichier config.xml
    (
        Ce que contient le fichier:
        Si besoin de l'uathentification, demander si tel ou telle entité à besoin d'etre authentifié pour les opérations (CRUD)
        <CLI-Spring>
            <Entity>
                <Name>Exemple</Name>
                <CRUD>
                    <Create>
                        <Auth>False</Auth>
                    </Create>
                    <Read>
                        <Auth>True</Auth>
                    </Read>
                </CRUD>
                <Fields>
                    <Field>
                        <Name></Name>
                        <Type></Type> (Nom du type + option et longueur en fonction du type)
                        <Mandatory></Mandatory>
                        <Searchable></Searchable>
                    </Field>
                </Fields>
            </Entity>
        </CLI-Spring>
    )
- Faire un récap et demander confirmation

