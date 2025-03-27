# Asteroids game
> A boot.dev guided project

## Requirements

- Python 3.xx
- pygame 2.6.1

## Preparing Environment and Installing `pygame`

1. (Suggested) Create a virtual environment for the project:

```bash
# run this inside the root directory of the project
python3 -m venv venv
# activate the new venv
source venv/bin/activate
```

To deactivate the environment enter `deactivate`, and to re-activate it use `source venv/bin/activate` again.

2. Install `pygame`:

```bash
pip install -r requirements.txt
```

3. Check `pygame` installation:

```bash
python3 -m pygame
```

the output will indicate that the pygame is installed together with an error ` No module named pygame.__main__` (this is fine).

## Starting the Game

To start the game, run:

```bash
python3 main.py
```
