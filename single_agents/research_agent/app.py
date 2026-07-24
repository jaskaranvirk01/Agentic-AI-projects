from agent.loop import agent_loop
from rich import print
print("[bold cyan]========================================[/bold cyan]")
print("[bold green]Research Intelligence Agent[/bold green]")
print("[bold cyan]========================================[/bold cyan]")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("\nYou : ")

    if user_input.lower() == "exit":
        print("[yellow]Goodbye![/yellow]")
        break

    agent_loop(user_query=user_input)
