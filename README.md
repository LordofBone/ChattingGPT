### Usage

Check out this project into your code:

```git clone https://github.com/LordofBone/ChattingGPT```

Then append the system path of the chatting_gpt folder to the system path of the project.

`chatting_gpt_dir = os.path.join(path_to_chatting_gpt )`

`sys.path.append(chatting_gpt_dir)`

Copy or rename 'config/api_config_template.py' to 'config/api_config.py' and fill in the appropriate values.

import the integrate_chatgpt.py file into your project and instantiate the ChatGPT class:

```from chatting_gpt import IntegrateChatGPT```

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