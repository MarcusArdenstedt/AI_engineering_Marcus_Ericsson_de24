from pydantic_ai import Agent
from dotenv import load_dotenv


load_dotenv()


class JokeBot:
    def __init__(self):
        self.chat_agent = Agent(
            "google-gla:gemini-2.5-flash",
            system_prompt="Be joking programming nerd, always answer with programming joke no matter what the question is. used emoji to make it more funny.",
        )
        
        self.result = None
        
    def chat(self, prompt: str) -> dict:
        message_history = self.result.all_messages() if self.result else None
        self.result = self.chat_agent.run_sync(prompt, message_history=message_history)
        
        return {"user": prompt, "bot": self.result.data}
    
    
if __name__=="__main__":
    
    bot = JokeBot()
    
    result = bot.chat("hello there")
    print(result, "\n")
    
    
    result = bot.chat("What did I ask you first")
    print(result)
    
        
        
