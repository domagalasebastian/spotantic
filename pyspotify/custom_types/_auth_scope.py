from enum import Enum


class Scope(str, Enum):
    PLAYLIST_MODIFY_PRIVATE = "playlist-modify-private"
    PLAYLIST_MODIFY_PUBLIC = "playlist-modify-public"
    PLAYLIST_READ_PRIVATE = "playlist-read-private"
    UGC_IMAGE_UPLOAD = "ugc-image-upload"
