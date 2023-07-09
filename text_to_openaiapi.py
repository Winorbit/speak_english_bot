from handlers import logger as logging

import openai
import tiktoken

def num_tokens_from_messages(messages:list=None, model:str=None)->int:
    """Return the number of tokens used by a list of messages."""
    tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
    tokens_per_name = -1  # if there's a name, the role is omitted

    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        log_message = f"Warning: model {model} not found. Using cl100k_base encoding."
        logging.error(log_message)
        raise Exception(log_message)
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    logging.info(f"Number of tokens in request: {num_tokens}")
    return num_tokens

def send_request_to_openai_api(openapi_key:str=None, messages:list=None, model:str=None, temperature:float=None)->dict:
    try:
        logging.info(f"Sending request to OpenAI API with input: {messages}")
        openai.api_key = openapi_key
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
            )
        return response
    except Exception as e:
        logging.error(f"Error while sending request to OpenAI API: {e}")
        raise Exception(f"Error while sending request to OpenAI API: {e}")

