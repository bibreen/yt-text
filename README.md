# yt-text

유튜브 비디오 자막을 다운로드하는 파이썬 CLI 도구입니다.

## 기능

- 유튜브 비디오 ID로 자막 다운로드
- 한국어 우선, 영어 보조 언어 지원
- 크롬 브라우저 쿠키 지원 (비공개/제한된 비디오)
- 깔끔한 텍스트 출력

## 설치

```bash
# 의존성 설치
uv sync
```

## 사용법

```bash
# 기본 사용
uv run get-transcript dQw4w9WgXcQ

# 크롬 쿠키 사용 (비공개 비디오)
uv run get-transcript dQw4w9WgXcQ --chrome

# 도움말
uv run get-transcript --help
```

## 요구사항

- Python 3.12+
- uv (패키지 관리자)

## 의존성

- yt-dlp
- requests
- click