import os
import time
import requests
from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich import box
from rich.progress import Progress


def show_dev_info():

    console = Console()

    table = Table(
        show_header=False,
        box=box.ROUNDED,
        border_style="bright_magenta",
        pad_edge=True,
        width=60,
        highlight=True,
    )

    table.add_column("Content", style="bold bright_blue", justify="center")

    table.add_row("[bold gradient]✨ Monad Testnet ✨[/bold gradient]")
    table.add_row("─" * 55)
    table.add_row("[bright_red][link]https://github.com/a2nk[/link][/bright_red]")

    console.print("\n")
    console.print(table, justify="center")
    console.print("\n")

if __name__ == "__main__":
    show_dev_info()

