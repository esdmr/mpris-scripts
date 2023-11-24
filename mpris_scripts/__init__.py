from argparse import ArgumentParser, Namespace
from json import load
from typing import cast
from mpris_server.server import Server
from mpris_scripts.event_adapter import EventHandler
from mpris_scripts.mpris_adapter import MprisAdapter
from mpris_scripts.script import Script
from mpris_scripts.script_backend import ScriptBackend


class Args(Namespace):
    config: str


def main():
    parser = ArgumentParser()
    parser.add_argument("-c", "--config", required=True, help="JSON config file")
    args = cast(Args, parser.parse_args())

    with open(args.config) as f:
        json = load(f)

    scripts = [Script(i["name"], i["args"][0], *i["args"][1:]) for i in json["scripts"]]

    backend = ScriptBackend(
        scripts,
        supports_pausing=json.get("supports_pausing", False),
        supports_multi=json.get("supports_multi", False),
    )
    adapter = MprisAdapter(backend)
    mpris = Server("MPRISScripts", adapter=adapter)
    event = EventHandler(mpris)
    backend.set_event_adapter(event)
    print("starting")
    mpris.loop()
