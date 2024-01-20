import logging

from openai import OpenAI

logger = logging.getLogger(__name__)
logger.debug("Initialized")


class ChatGPTSystem:
    def __init__(self,
                 openai_api_key,
                 model,
                 role,
                 use_history,
                 temperature,
                 max_tokens,
                 top_p,
                 n,
                 frequency_penalty,
                 presence_penalty,
                 stop):
        """
        Initialize the chatgpt integration class along with the api key.
        """
        self.client = OpenAI(
            api_key=openai_api_key,
        )

        self.model = model

        self.role = role

        self.temperature_input = temperature
        self.max_tokens_input = max_tokens
        self.top_p_input = top_p
        self.n_input = n
        self.frequency_penalty_input = frequency_penalty
        self.presence_penalty_input = presence_penalty
        self.stop_input = stop

        self.use_history = use_history

        self.conversation_history = [
            {"role": "system", "content": f"{self.role}"}
        ]

        logging.debug(f"Initialized with model: {model}, role: {role}, use_history: {use_history}")

    def get_response(self, text_input):
        """
        Get the chatgpt response, using the context and text input set.
        If 'use_history' is True, it will maintain a conversation history, making for a more consistent back and forth.
        :return:
        """
        logging.debug(f"Received input: {text_input}")
        if self.use_history:
            return self._get_chatgpt_response_with_history(text_input)
        else:
            return self._get_chatgpt_response(text_input)

    def _get_chatgpt_response(self, text_input):
        """
        Get the chatgpt response without using history.
        :return:
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": f"{self.role}"},
                {"role": "user", "content": text_input},
            ],
            temperature=self.temperature_input,
            max_tokens=self.max_tokens_input,
            top_p=self.top_p_input,
            n=self.n_input,
            frequency_penalty=self.frequency_penalty_input,
            presence_penalty=self.presence_penalty_input,
            stop=self.stop_input
        )

        # Extract the assistant's message from the response
        assistant_message = response.choices[0].message.content
        logging.debug(f"Assistant response (without history): {assistant_message}")

        return assistant_message

    def _get_chatgpt_response_with_history(self, text_input):
        """
        Get the chatgpt response using history.
        :param text_input:
        :return:
        """
        # Add user's message to the history
        self.conversation_history.append({"role": "user", "content": text_input})

        logging.debug(f"Conversation history: {self.conversation_history}")

        # Get a response from OpenAI
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation_history,
            temperature=self.temperature_input,
            max_tokens=self.max_tokens_input,
            top_p=self.top_p_input,
            n=self.n_input,
            frequency_penalty=self.frequency_penalty_input,
            presence_penalty=self.presence_penalty_input,
            stop=self.stop_input
        )

        # Extract the assistant's message from the response
        assistant_message = response.choices[0].message.content
        logging.debug(f"Assistant response (with history): {assistant_message}")

        # Add assistant's message to the history
        self.conversation_history.append({"role": "assistant", "content": assistant_message})

        return assistant_message
