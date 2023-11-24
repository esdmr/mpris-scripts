from typing import TYPE_CHECKING
from mpris_server.base import PlayState

if TYPE_CHECKING:
    from mpris_scripts.event_adapter import EventHandler
    from mpris_scripts.script import Script


class ScriptBackend:
    def __init__(
        self,
        scripts: "list[Script]",
        /,
        supports_pausing=False,
        supports_multi=False,
    ):
        self._scripts = scripts
        self._index = 0
        self._event = None
        self._supports_pausing = supports_pausing
        self._supports_multi = supports_multi

    def get_state(self) -> PlayState:
        if self.get_current().process is None:
            return PlayState.STOPPED
        elif self.get_current().paused:
            return PlayState.PAUSED
        else:
            return PlayState.PLAYING

    def get_current(self):
        return self._scripts[self._index]

    def get_list(self):
        return self._scripts[self._index :] + self._scripts[: self._index]

    def get_next(self):
        return self._scripts[(self._index + 1) % len(self._scripts)]

    def get_previous(self):
        return self._scripts[(self._index - 1) % len(self._scripts)]

    def set_event_adapter(self, event: "EventHandler"):
        self._event = event

    def _set_index(self, val: int):
        if not self._supports_multi:
            self.stop()

        self._index = val

        if self._event:
            self._event.on_title()
            self._event.on_playpause()

    def next(self):
        self._set_index((self._index + 1) % len(self._scripts))

    def previous(self):
        self._set_index((self._index - 1) % len(self._scripts))

    def start(self):
        self.get_current().start()

        if self._event:
            self._event.on_playpause()

    def stop(self):
        self.get_current().stop()

        if self._event:
            self._event.on_playpause()

    def pause(self):
        if not self._supports_pausing:
            self.stop()
            return

        self.get_current().pause()

        if self._event:
            self._event.on_playpause()

    def resume(self):
        if not self._supports_pausing:
            self.start()
            return

        self.get_current().resume()

        if self._event:
            self._event.on_playpause()

    def quit(self):
        if self._event:
            self._event.on_quit()
