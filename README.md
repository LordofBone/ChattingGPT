### Usage

Check out this project into your code:

```git clone https://github.com/LordofBone/ChattingGPT```

Install the requirements:

```pip install -r requirements.txt```

Copy or rename 'config/api_config_template.py' to 'config/api_config.py' and fill in the appropriate values.

import the integrate_chatgpt.py file into your project and instantiate the ChatGPT class:

```from ChattingGPT.integrate_chatgpt import IntegrateChatGPT```

```integrate_chatgpt_test = IntegrateChatGPT()```

```print(integrate_chatgpt_test.get_chatgpt_response())```

IntegrateChatGPT, you can call
the functions:

```integrate_chatgpt_test.set_context(str) ```

and 

```integrate_chatgpt_test.set_text_input(str)```

to set the context and text input respectively.

Then you can call the function

```integrate_chatgpt_test.get_chatgpt_response()```

to get the output for any code that uses this class.

The function for switching models:

```integrate_chatgpt_test.set_model(str)```

can also be called from the class to choose a different text completion model.

You can find the list of text models [here](https://platform.openai.com/docs/models/gpt-3-5), the default is set to
"gpt-3.5-turbo"