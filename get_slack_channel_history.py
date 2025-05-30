from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv
from datetime import datetime

# 환경 변수 로드
load_dotenv()
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

client = WebClient(token=SLACK_BOT_TOKEN)

def get_slack_channel_history(channel_id, limit=10):
    try:
        response = client.conversations_history(
            channel=channel_id,
            limit=limit
        )
        messages = response["messages"]

        print(f"✅ 최근 {limit}개의 메시지:")
        for msg in messages:
            user = msg.get("user", "시스템")
            text = msg.get("text", "[빈 메시지]")
            ts = float(msg["ts"])
            timestamp = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            print(f"- [{timestamp}] {user}: {text}")

    except SlackApiError as e:
        print(f"Slack API 에러 발생: {e.response['error']}")

# 테스트 실행
if __name__ == "__main__":
    # 여기에 당신의 채널 ID를 입력하세요
    test_channel_id = "C08Q20LH0MS"  # 예시: 5_강의장-python
    get_slack_channel_history(test_channel_id, limit=10)
