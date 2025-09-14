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

## 주의사항

### IP 차단 문제 (RequestBlocked 또는 IpBlocked 예외)

유튜브는 클라우드 제공업체(AWS, Google Cloud Platform, Azure 등)의 알려진 IP를 차단하기 시작했습니다. 따라서 클라우드 솔루션에 코드를 배포할 때 RequestBlocked 또는 IpBlocked 예외가 발생할 가능성이 높습니다. 자체 호스팅 솔루션에서도 너무 많은 요청을 하면 같은 문제가 발생할 수 있습니다.

**권장사항:**
- 로컬 환경에서 개인적인 용도로 사용
- 로컬 환경에서도 너무 많은 요청 시 IP 차단 가능성 있음
- 클라우드 배포 시 IP 차단 가능성 인지