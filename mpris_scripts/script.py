from subprocess import Popen
from typing import TYPE_CHECKING
from mpris_server.base import Track
from mpris_server.mpris.metadata import MetadataEntries

if TYPE_CHECKING:
    from mpris_server.mpris.metadata import Metadata


class Script:
    def __init__(self, name: str, path: str, *args: str):
        self.name = name
        self.path = path
        self.args = args
        self.process = None
        self.paused = False

    def start(self):
        if self.process is None:
            self.process = Popen([self.path, *self.args])
            self.paused = False

    def stop(self):
        if self.process is not None:
            self.resume()
            self.process.terminate()
            self.process = None

    def pause(self):
        if self.process is not None and not self.paused:
            self.process.send_signal(19)
            self.paused = True

    def resume(self):
        if self.process is not None and self.paused:
            self.process.send_signal(18)
            self.paused = False

    def to_track(self):
        return Track(
            name=self.name,
        )

    def to_metadata(self) -> "Metadata":
        return {
            MetadataEntries.TITLE: self.name,
        }  # type: ignore
