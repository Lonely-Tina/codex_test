# Pomodoro Timer

This repository contains a simple command-line Pomodoro timer written in Python.

## Usage

```bash
python pomodoro.py
```

### Options
- `--work` minutes for work sessions (default 25)
- `--short-break` minutes for short breaks (default 5)
- `--long-break` minutes for the long break after all cycles (default 15)
- `--cycles` number of work sessions before the long break (default 4)

Example running short test cycles:

```bash
python pomodoro.py --work 0.1 --short-break 0.1 --long-break 0.1 --cycles 1
```

This will run quickly for demonstration purposes.

