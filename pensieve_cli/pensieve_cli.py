import datetime
import os
import shutil
import subprocess
from typing import Annotated

import typer
import questionary

from .autocomplete import autocomplete
from .env import NOTES_PATH, EDITOR
from .search import SearchMethod, Seacher

app = typer.Typer()


@app.command()
def drop(
    thought_name: Annotated[
         str,
         typer.Argument(
            help="Filename where you want to write your notes",
            autocompletion=autocomplete,
        )
    ]
):
    FILE_PATH = NOTES_PATH / (f"{thought_name}.md" if not thought_name.endswith(".md") else thought_name)
    FILE_PATH.parents[0].mkdir(parents=True, exist_ok=True)
    subprocess.run(f"{EDITOR} {FILE_PATH}", shell=True)
    return typer.Exit(0)


@app.command()
def fetch(
    thought_name: Annotated[
         str,
         typer.Argument(
            help="Path where you want to retrieve your notes",
            autocompletion=autocomplete
        )
     ] = ""
):

    FILE_PATH = NOTES_PATH / thought_name
    subprocess.run(f"glow {FILE_PATH}", shell=True)
    return typer.Exit(0)


@app.command()
def let_go(
    thought_name: Annotated[
         str,
         typer.Argument(
            help="Path where you want to retrieve your notes",
            autocompletion=autocomplete
        )
     ]
):
    _ = typer.confirm("Are you sure you want to delete it?", abort=True)
    FILE_PATH = NOTES_PATH / thought_name
    if FILE_PATH.is_dir():
        shutil.rmtree(FILE_PATH)
    elif FILE_PATH.is_file():
        os.remove(FILE_PATH)
    return typer.Exit(0)

   

@app.command()
def search(
    by: Annotated[
        SearchMethod,
        typer.Option(
            help="How to search the notes",
        )
    ] = SearchMethod.date
):
    files = Seacher.search(by)
    if by is SearchMethod.date:
        date = questionary.select(
            "Which date do you want to select?",
            choices=[d.isoformat() for d in files.keys()]
        ).ask()
        date = datetime.date.fromisoformat(date)

        thought_name = questionary.select(
            "Which file do you want",
            choices=files[date]
        ).ask()

    FILE_PATH = NOTES_PATH / thought_name
    subprocess.run(f"glow {FILE_PATH}", shell=True)
    return typer.Exit(0)
        

if __name__ == "__main__":
    typer.run(app)
