import secrets
import string
import typer


app = typer.Typer()


lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
punctuations = string.punctuation


@app.command("1", help="password contains only alphabet letters")
def alpha(length: int = typer.Option(..., prompt="How long should the password be")):
    alpha = lowercase + uppercase
    p_word = [secrets.choice(alpha) for _ in range(length)]

    for x in p_word:
        print(x, end="")



@app.command("2", help="password contains only  numbers")
def num(length: int = typer.Option(..., prompt="How long should the password be")):
    p_word = [secrets.choice(digits) for _ in range(length)]

    for x in p_word:
        print(x, end="")



@app.command("3", help="password contains alphabet letters and numbers")
def alpha_num(length: int = typer.Option(..., prompt="How long should the password be")):
    alpha_num = lowercase + uppercase + digits
    p_word = [secrets.choice(alpha_num) for _ in range(length)]

    for x in p_word:
        print(x, end="")



@app.command("4", help="password contains alphabet letters, numbers and punctuations")
def alpha_num_pun(length: int = typer.Option(..., prompt="How long should the password be")):
    alpha_num_pun = lowercase + uppercase + digits + punctuations
    p_word = [secrets.choice(alpha_num_pun) for _ in range(length)]

    for x in p_word:
        print(x, end="")



@app.command("5", help="password contains punctuations and numbers")
def num_pun(length: int = typer.Option(..., prompt="How long should the password be")):
    num_pun = digits + punctuations
    p_word = [secrets.choice(num_pun) for _ in range(length)]

    for x in p_word:
        print(x, end="")


if __name__ == "__main__":
    app()
