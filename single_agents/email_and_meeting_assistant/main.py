from agent.loop import agent_loop
from agent.agent import automation_agent

automation_agent.reset()

print("Email Automation Agent")
print("say exit to exit")

while True:
    user_query = input("You : ")

    if user_query.lower() == 'exit':
        print('Exitting .....')
        break

    agent_loop(user_query)
