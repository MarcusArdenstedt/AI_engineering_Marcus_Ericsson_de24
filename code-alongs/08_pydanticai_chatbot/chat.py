from pydantic_ai import Agent
from dotenv import load_dotenv

load_dotenv()

class JokeBot:
    def __init__(self):
        self.chat_agent = Agent(
            model="google-gla:gemini-2.5-flash", 
            system_prompt="Be a joking programming nerd, always answer programming joke")
        
        
        self.result = None
        
    def chat(self, prompt: str):
        # ternary operator, one line if-else statement
        message_history = self.result.all_messages() if self.result else None
        self.result = self.chat_agent.run_sync(prompt, message_history=message_history)
        
        return {"user": prompt, "bot": self.result.data}
    
    
if __name__=="__main__":
    # Instansiate an instance of class JokeBot(bot is sent as self)
    bot = JokeBot()
    
    # call method cha(bot sent in as self)
    result = bot.chat("Tell me a math joke")
    result = bot.chat("Hello there")
    print(result)
    
    result = bot.chat("What did I ask you first time")
    print(result)
   
        
        