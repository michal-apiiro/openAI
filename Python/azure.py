from azure.openai import OpenAIClient 
from azure.ai.ml import MLClient 


def main():
    model = "vicuna-7b-v1.5"
    prompt = "Once upon a time"

    new_client = OpenAIClient()
    new_client_azure = MLClient()


if __name__ == "__main__":
    main()