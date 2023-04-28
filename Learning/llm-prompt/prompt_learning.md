LLM - Large Language model
Prompt - Instruction to the LLM to give us the response.

	Types:
		Base LLM:
			Predicts the next sentence
		Instruction Tuned LLM:
			It built on top of Base LLM where input and output sort of instructions are followed. It is trained used a technique called RLHF (Reinforcement Learning with Human Feedback), reinforcement learning.
		
		ChatGPT is one such instruction tuned LLMs. Prompts are used as instructions and the better the prompt the better the responses will be.
	
	Prompt Principles:
        1. Write Clear and Specific Instructions
        2. Give the model time to "think"
    
    Setup:
        1. Python Library - openai
        2. Create API key at https://platform.openai.com/account/api-keys
        3. Load it at openai.api_key
        4. Different models can be used: e.g., gpt-3.5-turbo