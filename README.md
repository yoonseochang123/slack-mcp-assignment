# Slack MCP

Slack API를 활용한 Model Context Protocol (MCP) 프로젝트입니다. Slack 워크스페이스에 파일을 업로드하고 메시지를 전송하는 기능을 제공합니다.

## 📋 프로젝트 개요

이 프로젝트는 Slack Bot을 통해 파일 업로드 및 메시지 전송 기능을 구현한 Python 애플리케이션입니다. FastMCP 프레임워크를 기반으로 구축되었습니다.

## 🚀 주요 기능

- 📎 Slack 채널에 파일 업로드
- 💬 초기 코멘트와 함께 파일 공유
- 🔐 환경변수를 통한 보안 토큰 관리
- ⚡ FastMCP 프레임워크 지원

## 📦 설치 및 설정

### 요구사항

- Python 3.13 이상
- Slack Bot Token (SLACK_BOT_TOKEN)

### 설치

1. 저장소 클론
```bash
git clone <repository-url>
cd slack-mcp
```

2. 가상환경 생성 및 활성화
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

3. 의존성 설치
```bash
pip install -r requirements.txt
# 또는 uv 사용 시
uv sync
```

### 환경 설정

1. `.env` 파일 생성
```env
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token-here
```

2. Slack Bot 설정
   - Slack 앱 생성 및 Bot 토큰 발급
   - 필요한 OAuth 권한 설정:
     - `files:write`
     - `chat:write`
     - `channels:read`

## 💻 사용법

### 기본 실행

```bash
python main.py
```

### 파일 업로드 실행

```bash
python bot_slack_mcp.py
```

### 코드 예시

```python
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv

load_dotenv()
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
client = WebClient(token=SLACK_BOT_TOKEN)

# 파일 업로드
response = client.files_upload_v2(
    channel="C08Q20LH0MS",
    file="path/to/your/file.jpg",
    title="파일 제목",
    initial_comment="📁 파일 업로드 완료!"
)
```

## 📁 프로젝트 구조

```
slack-mcp/
├── .venv/                # 가상환경
├── bot_slack_mcp.py      # 핵심 Slack Bot 기능
├── main.py               # 메인 실행 파일
├── pyproject.toml        # 프로젝트 설정
├── uv.lock              # 의존성 락 파일
├── .python-version      # Python 버전 지정
├── .env                 # 환경변수 (생성 필요)
└── README.md            # 프로젝트 문서
```

## 🔧 의존성

- **fastmcp** (>=2.5.2): Model Context Protocol 프레임워크
- **python-dotenv** (>=1.1.0): 환경변수 관리
- **requests** (>=2.32.3): HTTP 요청 처리
- **slack-sdk**: Slack API 클라이언트

## 🛠️ 개발

### 개발 환경 설정

```bash
# 개발 의존성 설치
uv add --dev pytest black flake8

# 코드 포맷팅
black .

# 린팅
flake8 .

# 테스트 실행
pytest
```

## 📝 사용 예시

현재 구현된 기능으로 특정 채널에 이미지 파일을 업로드하는 예시입니다:

```python
# 배고픈 고양이 이미지를 업로드하는 예시
response = client.files_upload_v2(
    channel="C08Q20LH0MS",
    file="C:/Users/uskyf/Desktop/Salesforce/hungrycat.jpg",
    title="배고픈 고양이",
    initial_comment="😿 배고파요"
)
```

## 🔐 보안 주의사항

- `.env` 파일을 `.gitignore`에 추가하여 토큰이 노출되지 않도록 주의
- Slack Bot 토큰은 절대 코드에 하드코딩하지 말 것
- 최소 권한 원칙에 따라 필요한 OAuth 권한만 부여

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

## 📞 문의

프로젝트에 대한 질문이나 제안사항이 있으시면 이슈를 생성해 주세요.

---
