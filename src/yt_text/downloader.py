import json

import requests
from yt_dlp import YoutubeDL


def get_transcript_text_with_yt_dlp(
    video_id: str, use_chrome_cookies: bool = False, languages=("ko", "en")
) -> str | None:
    """
    yt-dlp Python API를 사용해 자막을 추출하는 함수. 여러 언어(languages) 중 첫 번째로 성공한 자막을 반환. 실패 시 None 반환.
    """
    ydl_opts = {
        "skip_download": True,
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitlesformat": "json3",
        "quiet": True,
        "no_warnings": True,
    }

    if use_chrome_cookies:
        ydl_opts["cookiesfrombrowser"] = ("chrome",)

    url = f"https://www.youtube.com/watch?v={video_id}"
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        subs = {}
        subs.update(info.get("automatic_captions") or {})
        subs.update(info.get("subtitles") or {})

        if not subs:
            print(f"yt-dlp: 자막 없음")
            return None
        for lang in languages:
            if lang not in subs:
                continue
            json3_url = None
            for sub in subs[lang]:
                if sub.get("ext") == "json3":
                    json3_url = sub["url"]
                    break
            if not json3_url:
                continue
            resp = requests.get(json3_url, timeout=30)
            resp.raise_for_status()
            # json3 파싱
            data = json.loads(resp.text)
            # json3 구조에서 텍스트 추출
            # 일반적으로 'events' 리스트의 'segs' 하위 'utf8' 키에 텍스트가 있음
            text_chunks = []
            for event in data.get("events", []):
                segs = event.get("segs")
                if segs:
                    for seg in segs:
                        t = seg.get("utf8", "").strip()
                        if t:
                            text_chunks.append(t)
            text = " ".join(text_chunks).strip()
            if text:
                return text
        print(f"yt-dlp: {languages} 중 사용 가능한 자막 없음")
        return None
