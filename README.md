## Installation & Setup

This can either be used for using the ChatGPT API or the Ollama API (running locally) please note that running Ollama
will require quite a lot of ram (at least 8GB to get good performance), but will allow for very good responses without
any internet connection required.

Check out this project into your code:

```bash
git clone https://github.com/LordofBone/ChattingGPT
```

Install the requirements:

```bash
pip install -r requirements.txt
```

And for Ollama follow the installation instructions [here](https://github.com/jmorganca/ollama/blob/main/docs/linux.md).

This is primarily meant to be used with Linux (Raspberry Pi OS), but you can find installations for other platforms
[here](https://ollama.ai/download).

Then within your own code you need to set up the path to the code:

```python
import sys
from pathlib import Path

chatting_gpt_dir = Path(__file__).parent / 'ChattingGPT'

sys.path.append(str(chatting_gpt_dir))
```

And then import the integration module:

```python
from ChattingGPT.integrate_chatgpt import IntegrateChatGPT, IntegrateOllama
```

## ChatGPT API Usage
Make a file in the root of your project:

```.env```

And add the following line:
```OPENAI_API_KEY=<your_api_key>```

Adding your own API key from [OpenAI](https://platform.openai.com/)

Having already imported the integrate_chatgpt.py file into your project, instantiate the ChatGPT class:

```python
integrate_chatgpt_test = IntegrateChatGPT(model="gpt-3.5-turbo", role="You are a helpful assistant", use_history=False)

print(integrate_chatgpt_test.get_response(text_input="Hello, how are you?"))
```

You can find the list of text models [here](https://platform.openai.com/docs/models/gpt-3-5), the default is set to "
gpt-3.5-turbo"

You can also customise the role the AI will play in the conversation, the default is set to "You are a helpful
assistant".

Enabling history will allow the model to remember the conversation and give more context to the responses; much
like ChatGPT in a browser does.

There are also a number of other options that can be set, such as the temperature, max_tokens, top_p, n,
frequency_penalty, presence_penalty, stop; either by passing them into the instantiation of the class or by setting
them under config/chatgpt_config.py.

You can also read more about the
options [here](https://platform.openai.com/docs/api-reference/audio/createTranscription).

## Ollama API Usage

You will need to pull any LLM you intend to use, for the default that is used here:

```bash
ollama pull orca-mini
```

Having already imported the integrate_chatgpt.py file into your project, instantiate the ChatGPT class:

```python
integrate_ollama_test = IntegrateOllama(model="orca-mini", role="You are a helpful assistant", use_history=False)

print(integrate_ollama_test.get_response(text_input="Hello, how are you?"))
```

You can find the list of text models [here](https://ollama.ai/library), the default is set to "orca-mini", which is the
smallest and fastest model currently available.

As with the ChatGPT API, you can also customise the role the AI will play in the conversation, the default is set to "
You are a helpful assistant".

Enabling history will allow the model to remember the conversation and give more context to the responses; resulting in
a consistent conversation.

There are also a number of other options that can be set, such as the temperature, top_p, top_k, max_tokens, and more;
either by passing them into the instantiation of the class or by setting them under config/ollama_config.py.

You can also read more about the options [here](https://github.com/jmorganca/ollama/blob/main/docs/modelfile.md).