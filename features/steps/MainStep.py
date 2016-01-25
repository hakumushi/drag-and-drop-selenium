from pages.MainPage import MainPage
from util.Utils import Utils
from hamcrest import assert_that, equal_to

@given(u'I am on Main Page')
def step_impl(context):
    context.page_object = MainPage(context.driver)
    context.page_object.open_main_page()

@when(u'x')
def step_impl(context):
    print("")

@then(u'x')
def step_impl(context, title):
    print("")
