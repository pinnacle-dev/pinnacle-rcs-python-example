import os
from dotenv import load_dotenv
from rcs import Action, Pinnacle, Card, SendRcsResponse

load_dotenv()

KEY: str | None = os.getenv("PINNACLE_API_KEY")
if not KEY:
    raise ValueError("No key provided")

client = Pinnacle(
    api_key=KEY,
)

def basic_message() -> SendRcsResponse:
    response: SendRcsResponse = client.send.rcs(
        from_="test",
        to="+16287261512",
        text="Hello, world!",
    )
    return response

def send_media_message() -> SendRcsResponse:
    response: SendRcsResponse = client.send.rcs(
        from_="test",
        to="+16287261512",
        cards=[Card(title="Hello, world!", media_url="https://ia601509.us.archive.org/10/items/Rick_Astley_Never_Gonna_Give_You_Up/Rick_Astley_Never_Gonna_Give_You_Up.mp4")],
    )
    return response

def send_card_with_buttons() -> SendRcsResponse:
    response: SendRcsResponse = client.send.rcs(
        from_="test",
        to="+16287261512",
        cards=[
            Card(
                title="Hello, world!",
                subtitle="- Pinnacle",
                media_url="https://i.ibb.co/r2j65H4/Congrats-Pitch-Deck-5.png",
                buttons=[
                    Action(
                        title="Learn more",
                        payload="https://docs.trypinnacle.app/",
                        type="openUrl",
                    )
                ],
            )
        ],
    )
    return response

def send_card_with_buttons_quick_replies() -> SendRcsResponse:
    response: SendRcsResponse = client.send.rcs(
        from_="test",
        to="+16287261512",
        cards=[
            Card(
                title="Hello, world!",
                subtitle="- Pinnacle",
                media_url="https://i.ibb.co/r2j65H4/Congrats-Pitch-Deck-5.png",
                buttons=[
                    Action(
                        title="Learn more",
                        payload="https://docs.trypinnacle.app/",
                        type="openUrl",
                    )
                ],
            )
        ],
        quick_replies=[
            Action(
                title="What's RCS?",
                payload="WHAT_IS_RCS",
                type="trigger",
            ),
            Action(
                title="What's Pinnacle?",
                payload="WHAT_IS_PINNACLE",
                type="trigger",
            )
        ],
    )
    return response

def main() -> None:
    response: SendRcsResponse = send_card_with_buttons_quick_replies()
    print("Status:", response.message)

if __name__ == "__main__":
    main()
