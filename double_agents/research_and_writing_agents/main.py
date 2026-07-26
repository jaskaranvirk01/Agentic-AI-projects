from loops.agent_loop import research_agent, writer_agent, research_agent_loop


research_agent.reset()
writer_agent.reset()

print("Research and writing agent")
print('type exit to exit')

while True:
    user_query = input("You : ")
    if user_query.lower() == 'exit':
        print("Good Bye")
        break

    research_agent_loop(user_query)
