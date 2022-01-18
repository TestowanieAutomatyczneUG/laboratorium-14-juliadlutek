from behave import *
from src.sample.simple import Simple


@given("there is simple class with function for adding 1")
def step_impl(context):
    context.simple = Simple()


@when('we add 1 to {number}')
def step_impl(context, number):
    context.result = context.simple.add_one(float(number))


@then('result is {result}')
def step_impl(context, result):
    assert context.result == float(result)
