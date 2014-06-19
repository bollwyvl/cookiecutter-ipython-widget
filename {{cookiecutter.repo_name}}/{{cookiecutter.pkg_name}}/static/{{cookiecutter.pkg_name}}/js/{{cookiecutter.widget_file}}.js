;(function(IPython, require){
  'use strict';
   /**
    * The browser-side counterpart to {{cookiecutter.widget_stem}}View
    *
    * @author {{cookiecutter.full_name}}
    * @copyright {{cookiecutter.full_name}} {{cookiecutter.year}}
    * @version {{cookiecutter.version}}
    * @license {{cookiecutter.license}}
    */
  require(
    ['jquery', 'underscore', 'widgets/js/widget'],
    function($, _, WidgetManager){
      var {{cookiecutter.widget_stem}}View = IPython.DOMWidgetView.extend({
        // namespace your css so that you don't break other people's stuff
        className: '{{cookiecutter.widget_stem}}View',

        // Initialize DOM, etc. called once per view creation,
        // i.e. `display(widget)`
        render: function(){
          // Do one-off things here: the jQuery chained methods are great
          this.$date = this.$('<input />')
            .attr('type', 'date')
            .appendTo(this.$el);

          // call an update once the node has been added to the DOM
          _.defer(_.bind(this.update, this));

          // returning `this` makes your view chainable
          return this;
        },

        // Do things that are updated every time `this.model` is changed...
        // on the front-end or backend.
        update: function(){

          // Set the value of the date control and then call base.
          // ISO 8601 format YYYY-MM-DDTHH:mm:ss.sssZ is required
          this.$date.val(this.model.get('value'));

          // call __super__.update to handle housekeeping
          return {{cookiecutter.widget_stem}}View.__super__.update.apply(this);
        }, // update


        // Tell Backbone to listen to the change event of input controls (which
        // the HTML date picker is)
        events: {
          'change input': 'dateChange'
        },

        // Callback for when the date is changed.
        dateChange: function(event){
          this.model.set('value', event.currentTarget.value);
          this.touch();
        }

      }); // /extend

      // Register the {{cookiecutter.widget_stem}}View with the widget manager.
      WidgetManager.register_widget_view(
        '{{cookiecutter.widget_stem}}View',
        {{cookiecutter.widget_stem}}View
      );
    });
}).call(this, IPython, require);
