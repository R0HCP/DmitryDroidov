import histories as histories
from conversation import Unsafe_gemini


def answer(text):
    bard = Unsafe_gemini(history=histories.bard_ded, model='models/gemini-2.0-flash-thinking-exp-1219',temp=20) #тут параметры
    return bard.print_clean_answer(text)
