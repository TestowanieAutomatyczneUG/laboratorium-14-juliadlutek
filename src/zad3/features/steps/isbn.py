from behave import *
from src.sample.isbn import ISBN


@given("there is ISBN class with function for checking control number")
def step_impl(context):
    context.isbn = ISBN()


@when('we check control number for ISBN {number}')
def step_impl(context, number):
    context.result = context.isbn.controlNumber(number)


@then('result is {result}')
def step_impl(context, result):
    assert context.result == int(result)
