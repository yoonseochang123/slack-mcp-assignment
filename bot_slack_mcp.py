from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv

load_dotenv()
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
client = WebClient(token=SLACK_BOT_TOKEN)

def main():
    try:
        response = client.files_upload_v2(
            channel="C08Q20LH0MS",
            file="C:/Users/uskyf/Desktop/Salesforce/hungrycat.jpg",
            title="배고픈 고양이",
            initial_comment="😿 배고파요"
        )
        print("파일 업로드 성공:", response["file"]["id"])  # ✅ 들여쓰기 오류 수정됨
    except SlackApiError as e:
        print(f"Slack API 에러 발생: {e.response['error']}")

if __name__ == "__main__":
    main()
