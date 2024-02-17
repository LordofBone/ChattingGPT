import logging

from langchain_community.llms import Ollama

logger = logging.getLogger(__name__)
logger.debug("Initialized")


class OllamaSystem:
    def __init__(self,
                 model,
                 role,
                 use_history,
                 base_url,
                 mirostat,
                 mirostat_eta,
                 mirostat_tau,
                 num_ctx,
                 num_gpu,
                 repeat_last_n,
                 repeat_penalty,
                 temperature,
                 stop,
                 tfs_z,
                 top_k,
                 top_p):
        """
        Initialize the Ollama LangChain chatbot class.
        """
        self.use_history = use_history
        self.conversation_history = []
        self.ollama = Ollama(base_url=base_url,
                             system=role,
                             model=model,
                             mirostat=mirostat,
                             mirostat_eta=mirostat_eta,
                             mirostat_tau=mirostat_tau,
                             num_ctx=num_ctx,
                             num_gpu=num_gpu,
                             repeat_last_n=repeat_last_n,
                             repeat_penalty=repeat_penalty,
                             temperature=temperature,
                             stop=stop,
                             tfs_z=tfs_z,
                             top_k=top_k,
                             top_p=top_p)

        logger.debug(f"Initialized with use_history: {self.use_history}")

    def get_response(self, text_input):
        """
        Get the chatbot response using the input text.
        If 'use_history' is True, it will maintain a conversation history, making for a more consistent back and forth.
        """
        logger.info(f"Processing response with input: {text_input}")
        if self.use_history:
            return self._get_llm_response_with_history(text_input)
        else:
            return self._get_llm_response(text_input)

    def _get_llm_response(self, text_input):
        """
        Get the chatbot response without using history.
        """
        response = self.ollama(text_input)

        logger.info(f"Response (without history): {response}")

        return response

    def _get_llm_response_with_history(self, text_input):
        """
        Get the chatbot response using history.
        """
        self.conversation_history.append(text_input)
        logger.debug(f"Conversation history: {self.conversation_history}")

        response = self.ollama(" ".join(self.conversation_history))

        logger.info(f"Response (with history): {response}")

        self.conversation_history.append(response)

        return response
