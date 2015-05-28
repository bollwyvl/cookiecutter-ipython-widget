casper.notebook_test ->
  cells = {}

  @on "error", (msg, backtrace) ->
    console.log msg, backtrace

  @then ->
    @execute_cell @append_cell """
      from IPython.display import display
      from {{cookiecutter.pkg_name}}.widgets import {{cookiecutter.widget_stem}}
      {{cookiecutter.widget_file}} = {{cookiecutter.widget_stem}}(value="2000-01-01")""",
      "code"

  @wait_for_idle()

  @then ->
    @execute_cell @append_cell "display({{cookiecutter.widget_file}})", "code"

  @wait_for_idle()

  @then ->
    @test.assertEval(
      -> $(".widget-subarea input").val() == "2000-01-01"
      "...initialized with value"
    )

  @wait_for_idle()

  @then ->
    @fillSelectors ".{{cookiecutter.widget_stem}}View", "input": "1999-09-09"

  @then ->
    @execute_cell cells.val = @append_cell "{{cookiecutter.widget_file}}.value",
      "code"

  @wait_for_idle()

  @then ->
    @test.assertMatch @get_output_cell(cells.val).data["text/plain"],
      /1999-09-09/,
      "...changes backend value"

  @then ->
    @exit()
