import os
from dotenv import load_dotenv
from langchain.agents import create_agent
load_dotenv()

agent=create_agent(
    model="google_genai:gemini-3.5-flash-lite",
    tools=[],
    system_prompt="""
                  You are a Core Java tutor for beginners.
                  Answer only section requested by the user.
                  Be clear, concise and accurate.
                  When providing Java code, always provide the complete program.
                  Never stop the code at the middle.

                  Create a learing plan.
                  It should include:
                  1.Daily topics.
                  2.Simple explanations and definitions.
                  3.Example and Code.
                  4.Coding problems and exercise.
                  5.Important Interview questions.
                  6.Revision and Practice tasks.

                  Rules:
                  1.Don't repeat the topic.
                  2.When asked for 30 days plan generate from day 1 only.
                  3.Never skip or reorder any topic.
                  4.Cover only the core Java.
                  5.
                """
)

#user_input=input("Enter your question: ")
user_message={
    "messages":[
        {
            "role":"user",

            "content":"Create my 30-day Core Java plan"       #user prompt
        }
    ]
}
print("Start")
result=agent.invoke(user_message)
print("\n---  Core Java Study Plan  ---")

content = result["messages"][-1].content

if isinstance(content, list):
    content = "\n".join(
        item["text"]
        for item in content
        if item.get("type") == "text"
    )

    print(content)
