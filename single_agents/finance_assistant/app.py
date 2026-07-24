from agent.loop import agent_loop

print('-------------Expense Tracking Agent----------')
print()
while True:

    user_query = input("You : ")

    if user_query.lower() == 'exit':
        print('Exitting...')
        break

    agent_loop(user_query)
