$(document).ready(function () {
  $('.sidenav').sidenav({ edge: "right", draggable: true });
  $('input#password, input#username').characterCounter();
  $('.collapsible').collapsible();
  $('.fixed-action-btn').floatingActionButton({ direction: 'left' });
  $('.tooltipped').tooltip();
  });