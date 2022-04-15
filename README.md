# Amphetamine
## _When you really want to look like you're at your desk_

Amphetamine is a Python3 command line utility that keeps your computer from going asleep. To the outside world, it looks like you're at your desk when Amphetamine is running. 

## Features

- Every 100 seconds the mouse is oved to the top left of the screen, shift is pressed, and the mouse it returned to it's original postion.
- Completely non-disruptive. Can be used when you're active or not.
- Displays: t:time running w:"wiggle count" d:distance in pixels the mouse has moved 

## Tech

Dillinger uses a number of open source projects to work properly:

- [Python3] - Simply the best programming language in the world. 

## Installation

```sh
cd amphetamine
python3 -m venv venv && source venv/bin/activate && python -m pip install --upgrade pip && pip install -r requirements.txt
```

## Execution

```sh
cd amphetamine ; source venv/bin/activate ; python amphetamine.py
```

## License

MIT

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Python3]: <https://www.python.org/>
 
