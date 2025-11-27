from hmac import new
from os import remove
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ReplaceWord(BaseModel):
    snt: str
    word: str
    new: str


@router.post("/replace")
def replace_word(replace: ReplaceWord):
    index = 0
    word_len = len(replace.word)
    for char in replace.snt:
        split_snt = replace.snt[index: index + word_len]
        if split_snt == replace.word:
            first_part = replace.snt[:index]
            sec_part = replace.snt[index+word_len:]
            final = first_part + replace.new + sec_part
            return final
        index += 1
    return "not found"
