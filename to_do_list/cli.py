from func import load_save,save_files, saving_file
import typer


app = typer.Typer()

removed_tasks = []


# -----------------------------
# Add task to list
# -----------------------------
@app.command("add")
def add_task():
    tasks = load_save(save_files)
    next_id = max(tasks.keys(), default=0) + 1

    while True:
        task = input("📝 Enter a new task (or 'x' to quit): ").strip()

        if task.lower() == "x":
            break

        tasks[next_id] = {"task": task, "state": False}
        saving_file(save_files, tasks)
        typer.echo(f"✅ Task added with ID {next_id}")
        next_id += 1

    return tasks



# -----------------------------
# Remove or complete tasks
# -----------------------------

@app.command("remove")
def removing_tasks():
    tasks = load_save(save_files)
    while True:
        if not tasks:
            typer.echo("⚠️ NO TASKS LEFT")
            break

        typer.echo("\n📋 Current Tasks:")
        for k, v in tasks.items():
            typer.echo(f"{k}: {v['task']} {'✅' if v['state'] else '❌'}")


        removing_task = input("\nEnter ID to remove (or 'x' to cancel): ")

        if removing_task.lower() == "x":
            break
        elif removing_task.isdigit():
            removing_task_id = int(removing_task)

            if removing_task_id in tasks:
                removed_tasks.append(tasks.pop(removing_task_id))
                saving_file(save_files, tasks)
                typer.echo(f"❌ Task {removing_task_id} removed")
            else:
                typer.echo("⚠️ Task ID not found")
        else:
            typer.echo("⚠️ Invalid input. Please enter a number.")

    return removed_tasks, tasks

# -------------------
# Complete Task
# -------------------
@app.command("complete")
def complete_task() :
    tasks = load_save(save_files)
    while True:
        if not tasks:
            typer.echo("⚠️ NO TASKS LEFT")
            break

        typer.echo("\n📋 Current Tasks:")
        for k, v in tasks.items():
            typer.echo(f"{k}: {v['task']} {'✅' if v['state'] else '❌'}")

        complete_task = input("\nEnter ID to mark as complete (or 'x' to cancel): ")

        if complete_task.lower() == "x":
            break
        elif complete_task.isdigit():
            complete_task_id = int(complete_task)

            if complete_task_id in tasks:
                tasks[complete_task_id]["state"] = True
                saving_file(save_files, tasks)
                typer.echo(f"✅ Task {complete_task_id} marked as complete")
            else:
                typer.echo("⚠️ Task ID not found")
        else:
            typer.echo("⚠️ Invalid input. Please enter a number.")

    return tasks

@app.command("show")
def show_tasks():
    tasks = load_save(save_files)
    if not tasks:
        typer.echo("📭 No tasks available.")

    else:
        typer.echo("\n📋 All Tasks:")
        for k, v in tasks.items():
            typer.echo(f"{k}: {v['task']} {'✅' if v['state'] else '❌'}")


# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    app()
