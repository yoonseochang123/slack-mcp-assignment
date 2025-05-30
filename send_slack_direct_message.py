from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
client = WebClient(token=SLACK_BOT_TOKEN)

def send_slack_direct_message(user_id, text):
    try:
        # 1. DM 채널 열기 (im.open)
        im_response = client.conversations_open(users=user_id)
        channel_id = im_response["channel"]["id"]

        # 2. 메시지 전송
        response = client.chat_postMessage(
            channel=channel_id,
            text=text
        )
        print("✅ DM 전송 성공:", response["ts"])
    except SlackApiError as e:
        print(f"Slack API 에러 발생: {e.response['error']}")

# 테스트 실행
if __name__ == "__main__":
    test_user_id = "U08R03K7CGN"  # 👈 여기에 DM 보낼 대상의 user_id 입력
    send_slack_direct_message(test_user_id, "졸립니다")
