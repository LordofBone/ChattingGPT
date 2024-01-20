ollama_default_model = "orca-mini"
ollama_default_role = "You are a helpful assistant"
ollama_default_use_history = False
ollama_default_base_url: str = "http://localhost:11434"

ollama_default_mirostat = 0
"""Enable Mirostat sampling for controlling perplexity.
(default: 0, 0 = disabled, 1 = Mirostat, 2 = Mirostat 2.0)"""

ollama_default_mirostat_eta = 0.1
"""Influences how quickly the algorithm responds to feedback
from the generated text. A lower learning rate will result in
slower adjustments, while a higher learning rate will make
the algorithm more responsive. (Default: 0.1)"""

ollama_default_mirostat_tau = 5.0
"""Controls the balance between coherence and diversity
of the output. A lower value will result in more focused and
coherent text. (Default: 5.0)"""

ollama_default_num_ctx = 2048
"""Sets the size of the context window used to generate the
next token. (Default: 2048)	"""

ollama_default_num_gpu = 0
"""The number of GPUs to use. On macOS it defaults to 1 to
enable metal support, 0 to disable."""

ollama_default_repeat_last_n = 64
"""Sets how far back for the model to look back to prevent
repetition. (Default: 64, 0 = disabled, -1 = num_ctx)"""

ollama_default_repeat_penalty = 1.1
"""Sets how strongly to penalize repetitions. A higher value (e.g., 1.5)
will penalize repetitions more strongly, while a lower value (e.g., 0.9)
will be more lenient. (Default: 1.1)"""

ollama_default_temperature = 0.8
"""The temperature of the model. Increasing the temperature will
make the model answer more creatively. (Default: 0.8)"""

ollama_default_stop = None
"""Sets the stop tokens to use."""

ollama_default_tfs_z = 1
"""Tail free sampling is used to reduce the impact of less probable
tokens from the output. A higher value (e.g., 2.0) will reduce the
impact more, while a value of 1.0 disables this setting. (default: 1)"""

ollama_default_top_k = 40
"""Reduces the probability of generating nonsense. A higher value (e.g. 100)
will give more diverse answers, while a lower value (e.g. 10)
will be more conservative. (Default: 40)"""

ollama_default_top_p = 0.9
"""Works together with top-k. A higher value (e.g., 0.95) will lead
to more diverse text, while a lower value (e.g., 0.5) will
generate more focused and conservative text. (Default: 0.9)"""
