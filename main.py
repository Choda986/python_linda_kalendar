import os
import requests
import linda


def get_weekly_data():
    url_before = "https://www.lidl.rs/l/sr/katalog/pogledajte-nase-ponude-"
    url_after = "/view/flyer/page/1"
    day = linda.get_dates_from_monday()
    # Example logic
    message = "📅 Nedeljni Kalendar:\n\n"
    message += f"{url_before}{day}{url_after}\n\n"
    message += "Srecan Shopping!"
    return message


def send_telegram_message(message):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("Error: Telegram credentials not found in environment variables.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("Message sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message: {e}")


if __name__ == "__main__":
    # 1. Generate your content
    report_content = get_weekly_data()

    # 2. Send to Telegram
    send_telegram_message(report_content)
