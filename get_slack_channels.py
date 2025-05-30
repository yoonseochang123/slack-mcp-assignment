from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv

# .env 파일에서 토큰 불러오기
load_dotenv()
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

client = WebClient(token=SLACK_BOT_TOKEN)

def get_slack_channels():
    try:
        response = client.conversations_list(types="public_channel,private_channel")
        channels = response["channels"]

        print("✅ 접근 가능한 채널 목록:")
        for ch in channels:
            print(f"- 이름: {ch['name']}")
            print(f"  ID: {ch['id']}")
            print(f"  비공개 여부: {ch['is_private']}")
            print(f"  멤버 여부: {ch['is_member']}")
            print("")
    except SlackApiError as e:
        print(f"Slack API 에러 발생: {e.response['error']}")

# ✅ 이 줄이 반드시 있어야 실행됩니다!
if __name__ == "__main__":
    get_slack_channels()
