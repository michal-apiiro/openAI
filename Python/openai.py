import numpy as np
import openai
from dotenv import load_dotenv

def main():
    # OPENAI-KEY
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
if __name__ == "__main__":
    main()