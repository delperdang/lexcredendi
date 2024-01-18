$(function () {
  'use strict'

  $('[data-toggle="offcanvas"]').on('click', function () {
    $('.offcanvas-collapse').toggleClass('open')
  })

  // if (location.hostname != "localhost" && !location.hostname.startsWith("10.") && !location.hostname.startsWith("127.") && !location.hostname.startsWith("172.16.") && !location.hostname.startsWith("192.168."))
  //   if (location.protocol !== "https:") {
  //     location.protocol = "https:";
  //   };

})
