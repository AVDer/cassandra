# Ollama Setup

## Running

`ollama` is running as a service

`cat /etc/systemd/system/ollama.service`

```ini
[Unit]
Description=Ollama Service
After=network-online.target

[Service]
ExecStart=/usr/local/bin/ollama serve
User=ollama
Group=ollama
Restart=always
RestartSec=3
Environment="PATH="

[Install]
WantedBy=default.target
```

With the updated port number:

`cat /etc/systemd/system/ollama.service.d/override.conf`

```ini
[Service]
Environment="OLLAMA_HOST=0.0.0.0:11345"
```

## Check

* Service status: <http://IP:11345/>
* Installed models: <http://IP:11345/api/tags>

, where `IP` is an IP address of the machine with `ollama` running

## Models Installation

`export OLLAMA_HOST=0.0.0.0:11345`

Download model:

* ollama pull qwen3:8b
* ollama pull nomic-embed-text
