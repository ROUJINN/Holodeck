# import os

# from langchain.llms import OpenAI

# openai_api_key = os.environ.get("OPENAI_API_KEY")

# llm = OpenAI(
#     model_name="gpt-4o-2024-05-13",
#     max_tokens=2048,
#     openai_api_key=openai_api_key,
#     openai_api_base="https://api.zhizengzeng.com/v1",
# )

# response = llm(prompt="1+1=?")

# print(response)

# from ai2thor.controller import Controller
# from ai2thor.platform import CloudRendering

# controller = Controller(platform=CloudRendering)
# event = controller.step("MoveAhead")


import objathor.dataset.download_annotations
import objathor.dataset.download_features
