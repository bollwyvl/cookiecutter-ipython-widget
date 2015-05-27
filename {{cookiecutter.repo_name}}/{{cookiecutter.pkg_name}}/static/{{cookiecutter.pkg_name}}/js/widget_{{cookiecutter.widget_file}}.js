// the immediately-called closure and 'use strict' helps ensure hygiene
;(function(define) {
'use strict';
 /**
  * The browser-side counterpart to {{cookiecutter.widget_stem}}
  *
  * @author {{cookiecutter.full_name}}
  * @copyright {{cookiecutter.full_name}} {{cookiecutter.year}}
  * @version {{cookiecutter.version}}
  * @license {{cookiecutter.license}}
  */
define([
  // libraries
  'jquery',
  'underscore',

  // ipython API
  'widgets/js/widget',

  // local imports
  './utils'
],
function($, _, widget, utils) {
  var {{cookiecutter.widget_stem}}View = widget.DOMWidgetView.extend({
    // namespace your CSS so that you don't break other people's stuff
    className: '{{cookiecutter.pkg_name}} {{cookiecutter.widget_stem}}View',

    loadCss: utils.loadCss,

    // Initialize DOM, etc. called once per view creation,
    // i.e. `display(widget)`
    render: function() {
      // add a stylesheet, if defined in `_view_style`
      this.loadCss();

      // Do one-off things here
      this.$date = $('<input />')
        .attr('type', 'date')
        .appendTo(this.$el);

      // call an update once the node has been added to the DOM...
      this.update();

      return this;
    }, // /render

    // Do things that are updated every time `this.model` is changed...
    // from the front-end or backend.
    update: function(options) {
      // Set the value of the date control and then call base.
      // ISO 8601 format YYYY-MM-DDTHH:mm:ss.sssZ is required
      this.$date.val(this.model.get('value'));

      // call __super__.update to handle housekeeping
      return {{cookiecutter.widget_stem}}View.__super__.update.apply(this);
    }, // /update


    // Tell Backbone to listen to the change event of input controls (which
    // the HTML date picker is)
    events: {
      'input input': 'dateChange'
    },

    // Callback for when the date is changed.
    dateChange: function(event) {
      this.model.set('value', event.currentTarget.value);
      // this ensures that the value propagates back to the backend
      this.touch();

      return this;
    }

  }); // /extend

  // The requirejs namespace.
  return {
    {{cookiecutter.widget_stem}}View: {{cookiecutter.widget_stem}}View
  };
});
}).call(this, define);
