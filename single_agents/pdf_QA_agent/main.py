from agent.loop import agent_loop

print("========================================")
print("PDF Q/A Agent")
print("========================================")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("\nYou : ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    agent_loop(user_query=user_input)
