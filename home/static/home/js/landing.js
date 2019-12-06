$(function () {
    if (location.protocol !== "https:") {
        location.protocol = "https:";
    } else {
        window.location.replace("/");
    };
})
