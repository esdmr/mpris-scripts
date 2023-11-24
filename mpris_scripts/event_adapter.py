from typing import TYPE_CHECKING
from mpris_server.events import EventAdapter

if TYPE_CHECKING:
    from typing import TYPE_CHECKING, Any
    from mpris_adapter import MprisAdapter
    from mpris_server.interfaces.playlists import Playlists
    from mpris_server.interfaces.tracklist import TrackList
    from mpris_server.server import Server


class EventHandler(EventAdapter):
    def __init__(
        self,
        mpris: "Server[MprisAdapter, Any]",
        /,
        playlist: "Playlists | None" = None,
        tracklist: "TrackList | None" = None,
    ):
        super().__init__(mpris.player, mpris.root, playlist, tracklist)
        self._mpris = mpris

    def on_quit(self):
        self._mpris.quit()
