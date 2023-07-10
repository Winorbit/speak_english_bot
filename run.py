# Description: This script is used to send a request to OpenAI API and get a response from it.
import os
import sys
from handlers import logger as logging
from text_to_openaiapi import send_request_to_openai_api, num_tokens_from_messages

if __name__ == "__main__":
    # Getting environment variables
    openapi_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL")
    temperature = float(os.getenv("OPENAI_TEMPERATURE"))
    max_tokens = int(os.getenv("OPENAI_MAX_TOKENS"))
    system_level_message_text = os.getenv("HELP_LEARN_ENGLISH_SYSTEM_LEVEL_MESSAGE")

    # Checking if environment variables are set
    assert openapi_key, "OPENAI_API_KEY is not set"
    assert model, "OPENAI_MODEL is not set"
    assert temperature, "OPENAI_TEMPERATURE is not set"
    assert max_tokens, "OPENAI_MAX_TOKENS is not set"
    assert system_level_message_text, "HELP_LEARN_ENGLISH_SYSTEM_LEVEL_MESSAGE is not set"

    # Getting input message
    if len(sys.argv) > 1:
        input_message = sys.argv[1]
    else:
        logging.error("Input message is empty")
        raise Exception("Input message is empty")

    # Creating messages to send to OpenAI API
    system_level_message = {"role": "system", "content": system_level_message_text}
    messages=[
             system_level_message,
             {"role": "user", "content": input_message},
             ]
 
    # Checking if the number of tokens in request is less than the maximum allowed
    tokens_count = num_tokens_from_messages(messages=messages, model=model)
    if tokens_count >= max_tokens:
        logging.error(f"Number of tokens in request is {tokens_count}, but the maximum allowed is 2048.")
        raise Exception(f"Number of tokens in request is {tokens_count}, but the maximum allowed is 2048.")
    
    # Sending request to OpenAI API
    raw_response = send_request_to_openai_api(openapi_key=openapi_key, messages=messages, model=model, temperature=temperature)
    text_to_user_from_response = raw_response["choices"][0]["message"]["content"]
    
    print(text_to_user_from_response)
