from pages.MainPage import MainPage

@given(u'I am on Main Page')
def step_impl(context):
    context.page_object = MainPage(context.driver)
    context.page_object.open_main_page()

@when(u'I drag the square to the target')
def step_impl(context):
    context.page_object.drag_and_drop_the_square_to_the_box()
