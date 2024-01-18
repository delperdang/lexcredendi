$(function () {
  'use strict'

  $('[data-toggle="offcanvas"]').on('click', function () {
    $('.offcanvas-collapse').toggleClass('open')
  })

  // if (location.hostname != "localhost" && !location.hostname.startsWith("10.") && !location.hostname.startsWith("127.") && !location.hostname.startsWith("172.16.") && !location.hostname.startsWith("192.168."))
  //   if (location.protocol !== "https:") {
  //     location.protocol = "https:";
  //   };

  function isLocalAddress(hostname) {
    const rfc1918Ranges = [
      /^10\./,
      /^172\.(1[6-9]|2\d|3[0-1])\./,
      /^192\.168\./,
    ];
    const loopbackAddresses = ["127.0.0.1", "::1"];
  
    return (
      rfc1918Ranges.some((range) => range.test(hostname)) ||
      loopbackAddresses.includes(hostname) ||
      hostname.toLowerCase() === "localhost"
    );
  }
  
  const hostname = location.hostname;
  const protocol = location.protocol;
  
  if (!isLocalAddress(hostname) && protocol !== "https:") {
    location.protocol = "https:";
  }
  
})
