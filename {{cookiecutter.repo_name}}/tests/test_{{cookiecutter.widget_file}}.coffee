casper.test.begin "Widget: {{cookiecutter.widget_stem}}", ->
  casper.notebook_test ->
    @then ->
      @execute_cell @append_cell """
        from IPython.display import display
        from {{cookiecutter.pkg_name}}.widgets import {{cookiecutter.widget_stem}}
        {{cookiecutter.widget_file}} = {{cookiecutter.widget_stem}}(value="2000-01-01")""",
        "code"
  
    @wait_for_idle()

    @then ->
      @test.assertEval(
        -> IPython.WidgetManager._view_types.{{cookiecutter.widget_stem}}View != null
        "...registered"
      )
      @test.assertExists "link[href*='{{cookiecutter.widget_stem}}View.css']",
        "...style loaded"
  
    @then ->
      @execute_cell @append_cell "display({{cookiecutter.widget_file}})", "code"

    @wait_for_idle()

    @then ->
      @test.assertEval(
        -> $(".widget-subarea input").val() == "2000-01-01"
        "...initialized with value"
      )

    @wait_for_idle()

    @thenEvaluate ->
      $(".widget-subarea input").val("1999-09-09").trigger("input")

    @wait_for_idle()

    @then ->
      @execute_cell @append_cell "{{cookiecutter.widget_file}}.value", "code"

    @wait_for_output 2

    @then ->
      @test.assertEquals "1999-09-09", @get_output_cell(2),
        "...changes backend value"