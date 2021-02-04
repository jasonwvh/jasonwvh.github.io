const chartWrapper = document.querySelector(".chart-wrapper");
const scrollDown = document.querySelector(".scroll-down");

function isElementInViewport(el) {
    var rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <=
            (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <=
            (window.innerWidth || document.documentElement.clientWidth)
    );
}

window.addEventListener("scroll", scrollHandler);

function scrollHandler() {
    window.pageYOffset > 0
        ? scrollDown.classList.add("is-hidden")
        : scrollDown.classList.remove("is-hidden");
    if (isElementInViewport(chartWrapper))
        chartWrapper.classList.add("in-view");
}
