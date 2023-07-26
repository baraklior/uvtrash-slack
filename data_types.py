from pydantic import BaseModel
from typing import List


class MediaInfo(BaseModel):
    url: str
    duration: float
    preview: str
    dims: List[int]
    size: int


class MediaFormats(BaseModel):
    webppreview_transparent: MediaInfo
    gifpreview: MediaInfo
    webp_transparent: MediaInfo
    nanomp4: MediaInfo
    loopedmp4: MediaInfo
    nanowebppreview_transparent: MediaInfo
    webm: MediaInfo
    tinymp4: MediaInfo
    tinywebppreview_transparent: MediaInfo
    gif: MediaInfo
    mp4: MediaInfo
    tinywebm: MediaInfo
    tinygif: MediaInfo
    tinygifpreview: MediaInfo
    mediumgif: MediaInfo
    nanogifpreview: MediaInfo
    nanowebp_transparent: MediaInfo
    tinywebp_transparent: MediaInfo
    nanogif: MediaInfo
    nanowebm: MediaInfo


class ResultItem(BaseModel):
    id: str
    title: str
    media_formats: MediaFormats
    created: float
    content_description: str
    itemurl: str
    url: str
    tags: list
    flags: list
    hasaudio: bool

class JsonData(BaseModel):
    results: List[ResultItem]
    next: str


class SlackCommand(BaseModel):
    token: str
    team_id: str
    team_domain: str
    channel_id: str
    channel_name: str
    user_id: str
    user_name: str
    command: str
    text: str
    api_app_id: str
    is_enterprise_install: bool
    response_url: str
    trigger_id: str

