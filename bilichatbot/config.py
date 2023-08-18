import json
import os
from typing import Optional, List

class AccountInfo:
    sessdata: Optional[str] = None
    bili_jct: Optional[str] = None

    def __init__(self, sessdata: str = None, bili_jct: str = None):
        self.sessdata = sessdata
        self.bili_jct = bili_jct
    
    @classmethod
    def to_dict(cls) -> dict[str, str]:
        return {"sessdata": cls.sessdata, "bili_jct": cls.bili_jct}


class ReplyInfo:
    question: str = None
    answer: str = None

    def __init__(self, question: str, answer: str) -> None:
        self.question = question
        self.answer = answer

    def __dict__(self) -> dict[str, str]:
        return {"question": self.question, "answer": self.answer}


class Config:
    account: AccountInfo = AccountInfo
    reply_list: List[ReplyInfo] = []

    def to_dict(self):
        return {
            "account": self.account.to_dict(),
            "reply_list": [dict(reply_info) for reply_info in self.reply_list],
        }

    @classmethod
    def load(cls, target: str = "config.json"):
        if not os.path.exists(target):
            Config.default()
        with open(target, encoding="UTF-8") as f:
            info: dict = json.load(f)
            cls.account = AccountInfo(
                sessdata=info["account"]["sessdata"], bili_jct=info["account"]["bili_jct"]
            )
            cls.reply_list = [
                ReplyInfo(question=reply_info["question"], answer=reply_info["answer"])
                for reply_info in info["reply_list"]
            ]
        return cls

    @staticmethod
    def default(target: str = "config.json") -> None:
        if not os.path.exists(target):
            with open(target, "w", encoding="UTF-8") as f:
                info = Config().to_dict()
                json.dump(info, f)

config: Config = Config.load()