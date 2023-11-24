from subprocess import Popen
from threading import Thread
from typing import TYPE_CHECKING
from mpris_server.base import Track
from mpris_server.mpris.metadata import MetadataEntries

if TYPE_CHECKING:
    from mpris_server.mpris.metadata import Metadata
    from event_adapter import EventHandler


class Script:
    def __init__(self, name: str, path: str, *args: str):
        self.name = name
        self.path = path
        self.args = args
        self.paused = False
        self.event: "EventHandler | None" = None
        self._process = None
        self._thread = None

    def is_running(self):
        return self._process is not None and self._process.poll() is None

    def get_process(self):
        assert self._process is not None
        return self._process

    def start(self):
        if not self.is_running():
            self.paused = False
            self._process = Popen([self.path, *self.args])
            self._thread = Thread(target=self._wait_for_process)
            self._thread.start()

    def _wait_for_process(self):
        self.get_process().wait()
        self._process = None
        self._thread = None

        if self.event is not None:
            self.event.on_playpause()

    def stop(self):
        if self.is_running():
            self.resume()
            self.get_process().terminate()
            self._process = None

        if self._thread is not None:
            self._thread.join()
            self._thread = None

    def pause(self):
        if self.is_running() and not self.paused:
            self.get_process().send_signal(19)
            self.paused = True

    def resume(self):
        if self.is_running() and self.paused:
            self.get_process().send_signal(18)
            self.paused = False

    def to_track(self):
        return Track(
            name=self.name,
        )

    def to_metadata(self) -> "Metadata":
        return {
            MetadataEntries.TITLE: self.name,
        }  # type: ignore
