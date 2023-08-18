from bilibili_api import login
from bilibili_api.credential import Credential

from config import config, ReplyInfo

CREDENTIAL: Credential = Credential()

async def init_credential(sessdata: str = None,
                          bili_jct: str = None,
                          buvid3: str = None,
                          ac_time_value: str = None):
    
    CREDENTIAL = Credential(sessdata=sessdata,
                          bili_jct=bili_jct,
                          buvid3=buvid3,
                          ac_time_value=ac_time_value)
    
    if not await CREDENTIAL.check_valid():
        CREDENTIAL = login.login_with_qrcode_term()
    return CREDENTIAL

def check_quesion(question: str) -> ReplyInfo:
    for reply_info in config.reply_list:
        if question == reply_info.question:
            return reply_info