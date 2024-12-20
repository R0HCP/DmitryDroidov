import google.generativeai as genai
import config
from google.generativeai.types.content_types import to_content
from google.generativeai.types.safety_types import HarmCategory,HarmBlockThreshold
import datetime

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

    def __cleaner(func):
        def wrapper(self,*args,**kwargs):
            try:
                # print(f'\n\n\n\t{self.model_name} | {datetime.datetime.now()}\n\n')
                func(self,*args,**kwargs)
            except Exception as ex:
                print(str(ex))
            finally:
                print(".")
        return wrapper

        
    def __init__(self,history,model = 'models/gemini-pro',temp = 2):
        super().__init__(model,safety_settings=SAFETY_SETTINGS)
        generation_config = genai.GenerationConfig()
        generation_config.temperature = temp
        self.history = self.__get_history(history)
    
    def start_chat(self):
        return super().start_chat(history=self.history)
    
    @__cleaner
    def print_clean_answer(self,question):
        response = self.start_chat().send_message(question,stream=True)
        for chunk in response:
            print(chunk.text,end='')

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
