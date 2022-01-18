from behave import *
from Password import Password


@given("there is password validator")
def step_impl(context):
    context.password = Password()


@when('we check password {password}')
def step_impl(context, password):
    context.result = context.password.isValid(password)


@then('result is {result}')
def step_impl(context, result):
    if int(result) == 1:
        assert context.result
    else:
        assert not context.result
