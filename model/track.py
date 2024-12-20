from dataclasses import dataclass

@dataclass
class Track:
    name: str
    disc: int
    number: int
    time_millis: int
    preview_url: str | None = None
    album: str = "Unknown Album"  # New field
    artist: str = "Unknown Artist"  # New field
