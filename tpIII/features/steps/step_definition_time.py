from behave import given, when, then
import subprocess
import time

@given('a {day} solution')
def step_impl(context, day):
    print("Working on day: " + day)
    # Store the value in the context
    context.day = day

@when('I run the solution')
def step_impl(context):
    # Retrieve the value from the context
    day = context.day

    # Construisez le chemin vers le script Python
    script_path = f"./2023/day_{day}/main.py"
    
    # Start a stopwatch
    start_time = time.time()

    # Exécutez le script Python
    subprocess.run(["python3", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Stop the stopwatch
    end_time = time.time()

    # Store the time_spent in the context
    context.time_spent = end_time - start_time


@then('the solution should not last longer than {max_time} second')
def step_impl(context, max_time):
    # Retrieve the time_spent from the context
    time_spent = context.time_spent

    max_time = int(max_time)

    print(f"BLABLA d'exécution : {time_spent:.3f} s")
    # Make time_spent in seconds
    assert time_spent <= max_time, "The script took too long to execute"

