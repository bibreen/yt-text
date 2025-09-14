# CLAUDE.md

이 파일은 Claude Code (claude.ai/code)가 이 저장소에서 작업할 때 참고할 가이드입니다.

## 프로젝트 개요

`yt-text`는 YouTube 비디오 자막을 다운로드하는 Python CLI 도구입니다. yt-dlp를 사용해 자막 데이터를 추출하고 깔끔한 텍스트를 출력합니다.

## 아키텍처

**핵심 구성요소:**
- `src/yt_text/main.py` - Click 프레임워크를 사용한 CLI 인터페이스
- `src/yt_text/downloader.py` - yt-dlp를 사용한 핵심 자막 다운로드 로직
- 콘솔 스크립트 진입점: `get-transcript` 명령어

**주요 설계 패턴:**
- CLI 레이어와 비즈니스 로직의 명확한 분리
- 언어 우선순위: 한국어(`ko`) 우선, 영어(`en`) 보조
- 깔끔한 텍스트 추출을 위한 JSON3 자막 형식 파싱
- `cookiesfrombrowser`를 통한 Chrome 브라우저 쿠키 통합 (선택사항)

## 개발 명령어

```bash
# 의존성 설치 및 프로젝트 동기화
uv sync

# CLI 도구 실행
uv run get-transcript <youtube-id>

# Chrome 쿠키 사용 (비공개/제한된 비디오용)
uv run get-transcript <youtube-id> --chrome
```

## 주요 설정

**패키지 관리:** `uv` 사용 (최신 Python 패키지 관리자)
**Python 버전:** >=3.12 필요
**의존성:** yt-dlp, requests, click

**진입점 설정:** `pyproject.toml`에서 콘솔 스크립트 정의:
```toml
[project.scripts]
get-transcript = "yt_text.main:cli"

[tool.uv]
package = true
```

## 중요한 구현 세부사항

**자막 처리 흐름:**
1. yt-dlp가 비디오 메타데이터와 사용 가능한 자막 트랙을 추출
2. 수동 자막과 자동 자막을 결합
3. 한국어 우선, 영어로 폴백
4. HTTP를 통해 JSON3 형식 자막 다운로드
5. `events[].segs[].utf8`에서 텍스트를 추출하는 JSON3 구조 파싱
6. 세그먼트를 깔끔한 자막 텍스트로 연결

**Chrome 쿠키 통합:**
- 비공개 콘텐츠 접근을 위해 `ydl_opts["cookiesfrombrowser"] = ("chrome",)` 사용
- 수동 쿠키 파일 관리 불필요

## 언어 지원

기본 언어 우선순위는 `("ko", "en")`입니다. 언어를 추가하려면 `get_transcript_text_with_yt_dlp()`의 `languages` 매개변수를 수정하세요.