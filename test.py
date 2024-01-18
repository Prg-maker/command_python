from rich import print

# Exemplo de uso básico
print("Olá, mundo! :wave: Bem-vindo à biblioteca rich.")
print("[bold red]Isso é um texto em vermelho e negrito.[/bold red]")
print("[green]Isso é um texto verde.[/green]")

# Exemplo de tabela
table_data = [{"Nome": "Alice", "Idade": 30}, {"Nome": "Bob", "Idade": 25}]
print("[blue]Tabela de Dados[/blue]")
print_table = print(table_data, table=True)
