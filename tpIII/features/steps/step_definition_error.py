from behave import given, when, then
import subprocess

@given('a {day} solution running')
def step_impl(context, day):
    print("Working on day: " + day)
    # Store the value in the context
    context.day = day

@when('I run the solution with the input')
def step_impl(context):
    # Retrieve the value from the context
    day = context.day

    # Construisez le chemin vers le script Python
    script_path = f"./2023/day_{day}/main.py"

    # Exécutez le script Python
    context.process = subprocess.run(["python3", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@then('the solution should not throw any error')
def step_impl(context):
    # Check if the return code is 0, indicating success
    assert context.process.returncode == 0, f"The script threw an error: {context.process.returncode}"

    # Optionally, you can print the stdout and stderr if needed
    print("Script Output:", context.process.stdout.decode("utf-8"))
    print("Script Errors:", context.process.stderr.decode("utf-8"))
