import logging
import sys
import argparse
import os
import pandas as pd
from langchain.callbacks import get_openai_callback
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from tqdm.auto import tqdm
from google_utils import df_to_sheet_overwrite, df_to_sheet_append
import tiktoken


def main():
    model = "vicuna-7b-v1.5"
    prompt = "Once upon a time"
    get_call = get_openai_callback()
    new_chat = ChatOpenAI

if __name__ == "__main__":
    main()

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
tqdm.pandas()
()
