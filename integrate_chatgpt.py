import openai
from .config.api_config import openai_api_key, default_model
import logging


def main():
    """
    Main function for testing the chatgpt integration.
    :return:
    """
    logging.basicConfig(level="DEBUG")
    integrate_chatgpt_test = IntegrateChatGPT()
    return integrate_chatgpt_test.get_chatgpt_response()


class IntegrateChatGPT:
    def __init__(self):
        """
        Initialize the chatgpt integration class along with the api key.
        """
        self.api_key = openai_api_key

        self.model = default_model

        self.context = "You are a helpful code assistant for python"
        self.text_input = "Can you please generate me some code that draws a spinning sphere in pyopengl"

    def set_model(self, model):
        """
        Set the model for the chatgpt api.
        :param model:
        :return:
        """
        self.model = model

    def set_context(self, context):
        """
        Set the context for the chatgpt api.
        :param context:
        :return:
        """
        self.context = context

    def set_text_input(self, text_input):
        """
        Set the text input for the chatgpt api.
        :param text_input:
        :return:
        """
        self.text_input = text_input

    def get_chatgpt_response(self):
        """
        Get the chatgpt response, using the context and text input set.
        :return:
        """
        openai.api_key = self.api_key

        completion = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "system", "content": self.context},
                      {"role": "user", "content": self.text_input}]
        )

        return completion["choices"][0]["message"]["content"]
