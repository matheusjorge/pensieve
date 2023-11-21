# Pensieve

A lightweight note-taking managament app for the terminal.

## For who we are made?

The Pensieve was thought to make the lives of those who loves the terminal so much and do want to get out even for taking notes. 

If you are used to work most of your time in your terminal and needed something to help you keep yor notes organized, the Pensieve is for you.

## The name
The name was inspired by a Harry Potter World's instrument: a Pensieve!
The Pensieve is an instrument that helps the wizard or witch remove their thoughts from its head and store it in bottles, so they can access it latter.

## Instalation
The Pensieve CLI has ony two dependencies:
- Python 3.11 (If you don't have it, I suggest using [pyenv](https://github.com/pyenv/pyenv));
- [Glow](https://github.com/charmbracelet/glow), a Go module to render markdown files in the terminal

You can install the cli in two ways

### Manual

1. Install Glow using one of the [document methods](https://github.com/charmbracelet/glow#installation)
2. Clone this repo

```sh
git clone https://github.com/matheusjorge/penseive.git
```

3. Install the CLI using `pip` or `poetry`

```sh
pip install .
```

or

```sh
poetry install
```

### install.sh

The repository comes with a installer so you can leave everything (almost) with us. The only dependency it has is that you must have Golang installed in your machine. If you don't have yet (wasting your time), just follow the [documentation](https://go.dev/dl/).

1. Add permission to execute `install.sh`

```sh
chmod +x install.sh
```

2. Execute the installation script

```sh
./install.sh
```

## Features

### What the Pensieve is not?

- We are not a editor;
- We are not a markdown previewer;

The main goal of the Pensieve CLI is to be a lightweight note management software so it couples with some other softwares you already have, like your terminal editor, and the Glow library to render markdown

### Choosing your editor

By default, the Pensieve uses the `nano` editor that comes along with many terminal emulators. But don't worry if you want to change that.

Setting the environment variable `PENSIEVE_EDITOR` you can choose whatever editor you prefer.

```sh
export PENSIEVE_EDITOR="nvim"
```

### Commands

The commands might seem quite counterintuitive in a first attempt to use the cli. All commands make reference to the way the Pensieve works in the Harry Potter World.

- for writing a note (a memory) you need to drop it inside a recipient, so the command used for that is `pensieve drop`;
- for retrieving notes you can use the `pensieve fetch` command;
- for deleting notes and directories you can use the command `pensive let-go`;

You can find more information about all commando running `pensieve --help` or `pensieve {command} --help`

### Demo



## Next steps

- [] Implement search inside the files
- [] Implement tag system
- [] Implement embedding search
