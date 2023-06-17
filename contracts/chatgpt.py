import json
import openai
from config.config import Config
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
) 

class buildClass:
    def __init__(self, d=None) -> None:
        if d is not None:
            for k, v in d.items():
                setattr(self, k, v)

class chatGPT:
    n = 1
    max_token = 150
    temperature = 0.3
    engine = "gpt-3.5-turbo"
    total = 0

    def __init__(self, debug: False) -> None:
        self.systemMessage = "You are my helpful assistant"
        self.messages = []
        self.total = 0
        self.debug = debug
        self.config = Config()
        self.openai = openai
        self.__setKey()
        self.__memorize('system', self.systemMessage)

    def __setKey(self) -> None:
        self.openai.api_key = self.config.get('openai.key')

    def __memorize(self, type: str = 'system', message: str = None) -> None:
        self.messages.append({"role":type, "content":message})
        if self.debug: print(f"Messages: {self.messages}")
        for r, c in self.messages:
            if str(r).upper == "USER" or str(r).upper == "ASSISTANT":
                self.total =+ len(c)
        if self.total > 1000:
            self.total =- len(self.messages[-2].content)
            del self.messages[-2]

        # match str(type).upper:
        #     case "SYSTEM":
        #         self.messages[type] = message
        

    @retry(wait=wait_random_exponential(min=1, max=3), stop=stop_after_attempt(3))
    def __askGPT(self) -> None :
        try:                        
            self.completion = self.openai.ChatCompletion.create( 
                        model=self.engine,
                        messages=self.messages,
                        # max_tokens=self.max_token,
                        temperature=self.temperature
                        # top_p=1,
                        # presence_penalty=0,
                        # frequency_penalty=0,
                        # echo=False,
                        # n=self.n,
                        # stream=False,
                        # logprobs=None,
                        # best_of=1,
                        # logit_bias={}
                    )
        except self.openai.error.RateLimitError as e:
            self.__setError(e)
        except self.openai.error.APIConnectionError as e:
            self.__setError(e)
        except self.openai.error.Timeout as e:
            self.__setError(e)
        except self.openai.error.APIError as e:
            self.__setError(e)
        except self.openai.error.AuthenticationError as e:
            self.__setError(e)
        except:
            self.__setError("There was an error with Chat GPT")

    def __setError(self, e: str) -> None:
        print(e)
        text = buildClass({"text" : e})                
        self.completion = buildClass({"choices":[text]})

    def ask(self, message: str = None) -> None:
        self.__memorize('user', message)
        self.__askGPT()        

    def getResponse(self) -> str:
        if self.debug: dir(self.completion)
        if self.n == 1:
            self.__memorize('assistant', self.completion.choices[0].text)
            return self.completion.choices[0].text
        else:
            texts = []
            for idx in range(0, self.n):
                texts.append(self.completion.choices[idx].text)
            # self.__memorize('assistant', texts)
            return texts

