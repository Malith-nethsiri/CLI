import typer


app = typer.Typer()


@app.command("add")
def addition(inputs:list[float] = typer.Argument()):
    total = 0.0
    if not inputs or len(inputs) < 2:
            typer.echo("❌ Please provide at least two numbers.")
            return

    for x in inputs:
        total += x
    typer.echo (f"The total is {total}")


@app.command("sub")
def subtraction(inputs:list[float] = typer.Argument()):
    total = inputs[0]
    if not inputs or len(inputs) < 2:
            typer.echo("❌ Please provide at least two numbers.")
            return

    for x in inputs[1:]:
        total -= x
    typer.echo (f"The total is {total}")



@app.command("multi")
def multipication(inputs:list[float] = typer.Argument()):
    total = inputs[0]
    if not inputs or len(inputs) < 2:
            typer.echo("❌ Please provide at least two numbers.")
            return

    for x in inputs[1:]:
        total *= x
    typer.echo (f"The total is {total}")


@app.command("div")
def division(inputs: list[float] = typer.Argument(...)):
    try:
        if not inputs or len(inputs) < 2:
            typer.echo("❌ Please provide at least two numbers.")
            return

        total = inputs[0]
        for x in inputs[1:]:
            total /= x
        typer.echo(f"The total is: {total}")
    except ZeroDivisionError:
        typer.echo("❌ ZeroDivisionError: You tried to divide by zero.")



if __name__ == "__main__" :
    app()
