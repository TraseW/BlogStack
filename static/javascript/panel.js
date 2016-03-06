

$(document).ready(function () {
  $("#nav").click(function () {
    if (!$("#nav").hasClass("active")) {
      $(this).toggleClass("active");
    }
  });


  $("#main").click(function () {
    if ($("#nav").hasClass("active")) {
      $("#nav").toggleClass("active");
    }
  });

  $(".navdrop").click(function () {
    $(this).siblings("ul").toggleClass("active");
  })
});


var pageItems = new Vue({

  el: '#elements',

  data: {
    pageName: '',
    content: [],
    meta: [],
  },

  created: function() {
    this.addItem();
  },

  methods: {
    addItem: function() {
      this.content.push({
        open: false,
        tag: 'p',
        class: '',
        id: '',
        content: ''
      });
    },
    removeItem: function(index) {
      this.content.splice(index, 1);
    },
    addMeta: function() {
      this.meta.push({
        open: false,
        title: '',
        value: ''
      });
    },
    removeMeta: function(index) {
      this.meta.splice(index, 1);
    },
    dropdown: function(index) {
      this.content[index].open = !this.content[index].open;
      if (this.content[index].open) {
        autosize($('textarea'));
      }
    },
    dropdownMeta: function(index) {
      this.meta[index].open = !this.meta[index].open;
      if (this.meta[index].open) {
        autosize($('textarea'));
      }
    },
    submit: function() {
      console.log('test');
      if (this.pageName != '') {
        this.meta = metaItems.meta;
        $.post('/admin/create', JSON.stringify(this.$data));
        window.location = "/admin";
      }
    }
  }

});

var metaItems = new Vue({

  el: '#meta',

  data: {
    meta: []
  },

  created: function() {
    this.addMeta();
  },

  methods: {
    addMeta: function() {
      this.meta.push({
        open: false,
        title: '',
        value: ''
      });
    },
    removeMeta: function(index) {
      this.meta.splice(index, 1);
    },
    dropdownMeta: function(index) {
      this.meta[index].open = !this.meta[index].open;
      if (this.meta[index].open) {
        autosize($('textarea'));
      }
    },
    submit: function() {
      console.log('test');
      pageItems.meta = this.meta;
      $.post('/admin/create', JSON.stringify(pageItems.$data));
      window.location = "/admin";
    }
  }

});
