from itertools import count
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class FindingWord(BaseModel):
    sentence: str
    word: str


@router.post("/findword")
def find_word(findingtext: FindingWord):
    index = 0
    word_len = len(findingtext.word)
    findings = []
    for _ in findingtext.sentence:
        split_sentence = findingtext.sentence[index:index + word_len]
        print(split_sentence)
        if split_sentence == findingtext.word:
            findings.append(index)
        index += 1
    return findings
