import histories as histories
from conversation import Unsafe_gemini


def ansver(text):
    bard = Unsafe_gemini(history=histories.bard4, model='models/gemini-pro',temp=20) #тут параметры
    q = str(bard.print_clean_answer(text))
    return q
