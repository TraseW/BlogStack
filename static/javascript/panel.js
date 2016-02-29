var items = [];

var pageItems = new Vue({

  el: '#elements',

  data: {
    items: items,
  },

  created: function() {
    this.addItem();
  },

  methods: {
    addItem: function() {
      this.items.push({
        open: false,
        tag: '',
        class: '',
        id: '',
        content: ''
      });
    },
    removeItem: function(index) {
      this.items.splice(index, 1);
    },
    dropdown: function(index) {
      this.items[index].open = !this.items[index].open;
      if (this.items[index].open) {
        autosize($('textarea'));
      }
    }
  }

});
