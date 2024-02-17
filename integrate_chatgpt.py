import logging

logger = logging.getLogger(__name__)
logger.debug("Initialized")
from components.openai_api_key import gpt_openai_api_key

from .components.chatgpt_functions import ChatGPTSystem
from .components.ollama_functions import OllamaSystem

from .config.chatgpt_config import (gpt_default_model, gpt_default_role, gpt_default_use_history,
                                    gpt_temperature,
                                    gpt_max_tokens, gpt_top_p, gpt_n, gpt_frequency_penalty, gpt_presence_penalty,
                                    gpt_stop)

from .config.ollama_config import (ollama_default_role, ollama_default_use_history, ollama_default_model,
                                   ollama_default_base_url, ollama_default_mirostat,
                                   ollama_default_mirostat_eta, ollama_default_mirostat_tau, ollama_default_num_ctx,
                                   ollama_default_num_gpu,
                                   ollama_default_repeat_last_n, ollama_default_repeat_penalty,
                                   ollama_default_temperature, ollama_default_stop,
                                   ollama_default_tfs_z, ollama_default_top_k, ollama_default_top_p)


def IntegrateChatGPT(openai_api_key=gpt_openai_api_key,
                     use_history=gpt_default_use_history,
                     role=gpt_default_role,
                     model=gpt_default_model,
                     temperature=gpt_temperature,
                     max_tokens=gpt_max_tokens,
                     top_p=gpt_top_p,
                     n=gpt_n,
                     frequency_penalty=gpt_frequency_penalty,
                     presence_penalty=gpt_presence_penalty,
                     stop=gpt_stop):
    chat_system_init = ChatGPTSystem(use_history=use_history,
                                     role=role,
                                     model=model,
                                     openai_api_key=openai_api_key,
                                     temperature=temperature,
                                     max_tokens=max_tokens,
                                     top_p=top_p,
                                     n=n,
                                     frequency_penalty=frequency_penalty,
                                     presence_penalty=presence_penalty,
                                     stop=stop)

    logger.debug(f"Initialized ChatGPT with use_history: {use_history}")

    return chat_system_init


def IntegrateOllama(model=ollama_default_model,
                    role=ollama_default_role,
                    use_history=ollama_default_use_history,
                    base_url=ollama_default_base_url,
                    mirostat=ollama_default_mirostat,
                    mirostat_eta=ollama_default_mirostat_eta,
                    mirostat_tau=ollama_default_mirostat_tau,
                    num_ctx=ollama_default_num_ctx,
                    num_gpu=ollama_default_num_gpu,
                    repeat_last_n=ollama_default_repeat_last_n,
                    repeat_penalty=ollama_default_repeat_penalty,
                    temperature=ollama_default_temperature,
                    stop=ollama_default_stop,
                    tfs_z=ollama_default_tfs_z,
                    top_k=ollama_default_top_k,
                    top_p=ollama_default_top_p):
    chat_system_init = OllamaSystem(use_history=use_history,
                                    role=role,
                                    model=model,
                                    base_url=base_url,
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

    logger.debug(f"Initialized Ollama with use_history: {use_history}")

    return chat_system_init
