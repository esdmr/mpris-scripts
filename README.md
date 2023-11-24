# MPRIS Scripts

Run scripts via the MPRIS/D-Bus protocol. With this tool, you can control your
scripts from various devices and applications, including:

- ⏯️ **OS media control**
- 📱 **mobile apps** like KDE Connect
- ⌚ **smartwatches and bands**

## Usage

1. 🐍 **Install Python 3.12 or later** on your system.
2. 📦 **Install the dependencies** using PDM or other PEP 518 compatible package managers.
3. ⚙️ **Create a config file.** You can refer to the
   [`example.json`](example.json) file for an example.
4. ▶️ **Start the server** using the following command: `python3 mpris_scripts --config config.json`.

## Features

- 📜 **Scroll through your scripts** via previous/next buttons.
- ⏹️ **Run and stop scripts.**
- ⏯️ Optionally **pause scripts** via `SIGSTOP` and `SIGCONT`.
