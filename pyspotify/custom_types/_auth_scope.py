from enum import Enum


class Scope(str, Enum):
    PLAYLIST_MODIFY_PRIVATE = "playlist-modify-private"
    PLAYLIST_MODIFY_PUBLIC = "playlist-modify-public"
    PLAYLIST_READ_PRIVATE = "playlist-read-private"
    UGC_IMAGE_UPLOAD = "ugc-image-upload"
    USER_FOLLOW_MODIFY = "user-follow-modify"
    USER_FOLLOW_READ = "user-follow-read"
    USER_LIBRARY_MODIFY = "user-library-modify"
    USER_LIBRARY_READ = "user-library-read"
    USER_READ_EMAIL = "user-read-email"
    USER_READ_PLAYBACK_POSITION = "user-read-playback-position"
    USER_READ_PRIVATE = "user-read-private"
    USER_TOP_READ = "user-top-read"
