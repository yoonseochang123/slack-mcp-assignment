from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv

# .env에서 SLACK_BOT_TOKEN 불러오기
load_dotenv()
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
client = WebClient(token=SLACK_BOT_TOKEN)

def get_slack_users():
    try:
        response = client.users_list()
        members = response["members"]

        print("✅ 사용자 목록:")
        for m in members:
            if not m["deleted"] and not m.get("is_bot", False):
                name = m["real_name"]
                uid = m["id"]
                print(f"- {name} ({uid})")
    except SlackApiError as e:
        print(f"Slack API 에러 발생: {e.response['error']}")

if __name__ == "__main__":
    get_slack_users()
