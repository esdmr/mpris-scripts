from decimal import Decimal
from typing import TYPE_CHECKING
import mpris_server.adapters

if TYPE_CHECKING:
    from mpris_server.base import (
        ActivePlaylist,
        DbusObj,
        PlaylistEntry,
        PlayState,
        Position,
        Rate,
        Track,
        Volume,
    )
    from mpris_server.enums import LoopStatus
    from mpris_server.mpris.metadata import Metadata
    from mpris_scripts.script_backend import ScriptBackend


DEFAULT_RATE: "Rate" = Decimal(1)
DEFAULT_VOLUME: "Volume" = Decimal(1)


class MprisAdapter(mpris_server.adapters.MprisAdapter):
    def __init__(self, backend: "ScriptBackend"):
        self.backend = backend

    # region RootAdapter

    def can_fullscreen(self):
        return False

    def can_quit(self):
        return True

    def can_raise(self):
        return False

    def get_mime_types(self) -> list[str]:
        return []

    def get_uri_schemes(self) -> list[str]:
        return []

    def has_tracklist(self):
        return True

    def quit(self) -> None:
        self.backend.quit()

    def set_fullscreen(self, val: bool):
        print("Invalid operation set_fullscreen", val)

    def set_raise(self, val: bool):
        print("Invalid operation set_raise", val)

    # endregion
    # region PlayerAdapter

    def get_current_track(self) -> "Track":
        """
        This function is an artifact of forking the base MPRIS library to a generic interface.
        The base library expected Track-like objects to build metadata.

        If metadata() is implemented, this function won't be used to build MPRIS metadata.
        """

        return self.backend.get_current().to_track()

    def can_control(self) -> bool:
        return True

    def can_go_next(self) -> bool:
        return True

    def can_go_previous(self) -> bool:
        return True

    def can_pause(self) -> bool:
        return True

    def can_play(self) -> bool:
        return True

    def can_seek(self) -> bool:
        return False

    def get_art_url(self, track: int) -> str:
        return ""

    def get_current_position(self) -> "Position":
        return 0

    def get_maximum_rate(self) -> "Rate":
        return DEFAULT_RATE

    def get_minimum_rate(self) -> "Rate":
        return DEFAULT_RATE

    def get_next_track(self) -> "Track":
        return self.backend.get_next().to_track()

    def get_playstate(self) -> "PlayState":
        return self.backend.get_state()

    def get_previous_track(self) -> "Track":
        return self.backend.get_previous().to_track()

    def get_rate(self) -> "Rate":
        return DEFAULT_RATE

    def get_shuffle(self) -> bool:
        return False

    def get_stream_title(self) -> str:
        return self.backend.get_current().name

    def get_volume(self) -> "Volume":
        return DEFAULT_VOLUME

    def is_mute(self) -> bool:
        return True

    def is_playlist(self) -> bool:
        return True

    def is_repeating(self) -> bool:
        return False

    def next(self):
        self.backend.next()

    def open_uri(self, uri: str):
        print("Invalid operation open_uri", uri)

    def pause(self):
        self.backend.pause()

    def play(self):
        self.backend.start()
        self.backend.resume()

    def previous(self):
        self.backend.previous()

    def resume(self):
        self.backend.resume()

    def seek(self, time: "Position", track_id: "DbusObj | None" = None):
        print("Invalid operation seek", time, track_id)

    def set_loop_status(self, val: "LoopStatus"):
        print("Invalid operation set_loop_status", val)

    def set_maximum_rate(self, val: "Rate"):
        print("Invalid operation set_maximum_rate", val)

    def set_minimum_rate(self, val: "Rate"):
        print("Invalid operation set_minimum_rate", val)

    def set_mute(self, val: bool):
        print("Invalid operation set_mute", val)

    def set_rate(self, val: "Rate"):
        print("Invalid operation set_rate", val)

    def set_repeating(self, val: bool):
        print("Invalid operation set_repeating", val)

    def set_shuffle(self, val: bool):
        print("Invalid operation set_shuffle", val)

    def set_volume(self, val: "Volume"):
        print("Invalid operation set_volume", val)

    def stop(self):
        self.backend.stop()

    # endregion
    # region PlaylistAdapter

    def activate_playlist(self, id: "DbusObj"):
        print("Invalid operation activate_playlist", id)

    def get_active_playlist(self) -> "ActivePlaylist":
        return (True, ("default", "default", ""))

    def get_playlists(
        self, index: int, max_count: int, order: str, reverse: bool
    ) -> list["PlaylistEntry"]:
        return [("default", "default", "")]

    # endregion
    # region TrackListAdapter

    def add_track(self, uri: str, after_track: "DbusObj", set_as_current: bool):
        print("Invalid operation add_track", uri, after_track, set_as_current)

    def can_edit_tracks(self) -> bool:
        return False

    def get_tracks(self) -> list["DbusObj"]:
        print("Invalid operation get_tracks")
        return []

    def get_tracks_metadata(self, track_ids: list["DbusObj"]) -> "list[Metadata]":
        print("Invalid operation get_tracks_metadata", track_ids)
        return []

    def go_to(self, track_id: "DbusObj"):
        print("Invalid operation go_to", track_id)

    def remove_track(self, track_id: "DbusObj"):
        print("Invalid operation remove_track", track_id)

    # endregion
