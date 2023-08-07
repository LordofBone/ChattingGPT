### Usage

Check out this project into your code:

```git clone https://github.com/LordofBone/ChattingGPT```

Install the requirements:

```pip install -r requirements.txt```

Copy or rename 'config/api_config_template.py' to 'config/api_config.py' and add your own API key
from [OpenAI](https://platform.openai.com/)

import the integrate_chatgpt.py file into your project and instantiate the ChatGPT class:

```from ChattingGPT.integrate_chatgpt import IntegrateChatGPT```

```integrate_chatgpt_test = IntegrateChatGPT(model="gpt-3.5-turbo", role="You are a helpful assistant", use_history=False)```

```print(integrate_chatgpt_test.get_response())```

You can find the list of text models [here](https://platform.openai.com/docs/models/gpt-3-5), the default is set to "
gpt-3.5-turbo"

Enabling history will allow the model to remember the conversation and give more context to the responses; much
like ChatGPT in a browser does.