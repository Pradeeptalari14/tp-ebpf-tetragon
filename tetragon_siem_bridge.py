#!/usr/bin/env python3
"""Tetragon eBPF Event Bridge to SIEM."""
import json

print("Tetragon SIEM bridge listening on :54321...")
event = {
    "action": "SIGKILL",
    "binary": "/usr/bin/nsenter",
    "threat": "Privilege Escalation Intercepted"
}
print("Sample Event Intercepted:", json.dumps(event))
