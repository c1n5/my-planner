#!/usr/bin/env python
import sys
import os
from my_planner.crew import MyPlannerCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'dietary_requirement': 'diary free, vegetables and protein heavy',
        'ingredients': 'as you see fit, fresh, unprocessed ingredients', 
        'health_goals': 'ess sweet, lose weight, healthy eats'
    }
    MyPlannerCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
         'dietary_requirement': 'diary free, vegetables and protein heavy',
        'ingredients': 'as you see fit, fresh, unprocessed ingredients', 
        'health_goals': 'ess sweet, lose weight, healthy eats'
    }
    try:
        MyPlannerCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MyPlannerCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
         'dietary_requirement': 'diary free, vegetables and protein heavy',
        'ingredients': 'as you see fit, fresh, unprocessed ingredients', 
        'health_goals': 'ess sweet, lose weight, healthy eats'
    }
    try:
        MyPlannerCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
