# Data Bot Logger

This repository contains a simple Python script to log incoming messages
from the web chat widget.

## Usage

Run the logger as a small HTTP service. Chat messages sent from
`index4.html` will be POSTed to this server and appended to the file
`Data_Bot`.

```bash
python3 data_bot_logger.py
```

The server listens on port `8000`. Press `Ctrl+C` to stop it.
