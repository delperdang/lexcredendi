$(function () {
  'use strict'

  $('[data-toggle="offcanvas"]').on('click', function () {
    $('.offcanvas-collapse').toggleClass('open')
  })

  if (location.protocol !== "https:") {
    location.protocol = "https:";
  }

})
