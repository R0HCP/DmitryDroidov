from colorama import Fore, Style
import google.generativeai as genai
import config
import time
from google.generativeai.types.content_types import to_content
from google.generativeai.types.safety_types import HarmCategory,HarmBlockThreshold
import datetime
#я сам не ебу что тут происходит, но это работает
genai.configure(api_key=config.google_api_key)

SAFETY_SETTINGS = [
    {
        'category': HarmCategory.HARM_CATEGORY_HARASSMENT,
        'threshold': HarmBlockThreshold.BLOCK_NONE
        
    },
    {
        'category': HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        'threshold': HarmBlockThreshold.BLOCK_NONE
        
    },
    {
        'category': HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        'threshold': HarmBlockThreshold.BLOCK_NONE
        
    },
    {
        'category': HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        'threshold': HarmBlockThreshold.BLOCK_NONE
        
    }
]


class Unsafe_gemini(genai.GenerativeModel):



        
    def __init__(self,history,model = 'models/gemini-pro',temp = 2, idea = ""):
        super().__init__(model,safety_settings=SAFETY_SETTINGS, system_instruction=idea)
        generation_config = genai.GenerationConfig()
        generation_config.temperature = temp
        self.history = self.__get_history(history)
        
    
    def start_chat(self):  
        return super().start_chat(history=self.history)
    
    # @__cleaner
    def print_clean_answer(self,question,shorting = False):
        response = self.start_chat().send_message(question,stream=False)
        print (response.text)
        print (Fore.BLUE +"_________________________________________________________________" + Style.RESET_ALL)
        # print (Fore.BLUE + response.parts[1].text + Style.RESET_ALL)
        fin = response.text
        while shorting and len(fin) > 140:
            fin = self.short_answer(fin)

        return fin, response.usage_metadata.total_token_count
    

    def short_answer(self,question):
        print (Fore.RED + "Сокращаю сообщение" + Style.RESET_ALL)
        
        while len(question) > 150:
            question, _ = self.print_clean_answer(question + " сократи это сообщение меньше 140 символов", True)
        if len(question) <= 150:
            return question
        else:
            while len(question) > 150:
                question, _ = self.print_clean_answer(question + " сократи это сообщение меньше 140 символов", True)
            return question

 
    
    def __get_history(self,model):
        history = []
        for i in model:
            content = to_content(i[0])
            content.role = 'user'
            history.append(content)
            content = to_content(i[1])
            content.role = 'model'
            history.append(content)
        return history
    
