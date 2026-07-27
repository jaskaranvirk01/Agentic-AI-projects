from loops.agent_loop import resume_reader_loop


print('Resume review & rewrite Agent')
print('type exit to exit')

while True:
    user_query = input("You : ").strip()

    if user_query.lower() == "exit":
        break

    if not user_query:
        continue

    resume_reader_loop(user_query)
