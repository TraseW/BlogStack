

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
        tag: '',
        class: '',
        id: '',
        content: ''
      });
    },
    removeItem: function(index) {
      this.content.splice(index, 1);
    },
    dropdown: function(index) {
      this.content[index].open = !this.content[index].open;
      if (this.content[index].open) {
        autosize($('textarea'));
      }
    }
  }

});


