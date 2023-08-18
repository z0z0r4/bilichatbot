import asyncio
from bilibili_api.credential import Credential
from bilibili_api.session import Session, Event
from utils import init_credential, check_quesion
from config import config

session = Session(Credential())

async def main():
    global session
    CREDENTIAL = await init_credential(config.account.sessdata, config.account.bili_jct)
    session = Session(CREDENTIAL)


if __name__ == "__main__":
    asyncio.run(main())

@session.on(Event.TEXT)
async def on_text(event: Event):
    res = check_quesion(event.content)
    if res is not None:
        await session.reply(event, res.answer)


if __name__ == "__main__":
    asyncio.run(session.start(False))



