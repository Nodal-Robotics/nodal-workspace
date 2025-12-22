import json
import sys


def bot_error(message, **extra):
    payload = {
        "status": "error",
        "message": message,
        **extra
    }
    print(json.dumps(payload))
    sys.exit(1)


def bot_success(message, **extra):
    payload = {
        "status": "success",
        "message": message,
        **extra
    }
    print(json.dumps(payload))
