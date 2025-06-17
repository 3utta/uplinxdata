# Data Bot Logger

This repository contains scripts to log messages to a file named `Data_Bot`.

## Command-Line Usage

You can log arbitrary messages from the command line:

```bash
python3 data_bot_logger.py
```

Each line typed will be appended to the `Data_Bot` file. End input with `Ctrl+D` or `Ctrl+C`.

## Web Logging Server

For the chat widget in `index4.html`, run the Flask server:

```bash
pip install flask
python3 chat_logger.py
```

It exposes a `POST /log` endpoint that accepts JSON with a `message` field. Incoming messages are saved to the same `Data_Bot` file.
