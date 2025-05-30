from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv

# 환경 변수에서 토큰 로드
load_dotenv()
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
client = WebClient(token=SLACK_BOT_TOKEN)

def send_slack_message(channel, text):
    try:
        response = client.chat_postMessage(
            channel=channel,
            text=text
        )
        print("✅ 메시지 전송 성공:", response["ts"])
    except SlackApiError as e:
        print(f"Slack API 에러 발생: {e.response['error']}")

# 테스트 실행
if __name__ == "__main__":
    send_slack_message("C08Q20LH0MS", "광장시장 꽈배기 맛있어용")
