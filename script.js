if (!String.prototype.format) {
    String.prototype.format = function() {
        let args = arguments;
        return this.replace(/{(\d+)}/g, function(match, number) {
            return typeof args[number] != 'undefined' ? args[number] : match;
        });
    }
}

let contentTemplate = '<div class="content_box"><a href="{2}" target="_blank"><img class="content_image" src="{0}"><p class="content_title">{1}</p></a></div>'

for (let x in imageList) {
    let contentHtml = contentTemplate.format(imageList[x].img,
        imageList[x].title,
        imageList[x].url);
    $('#waterfallArea').append(contentHtml);
}

$(function() {
    //Trigger layout after each image loads and initialise Mansonry
    $('#waterfallArea').imagesLoaded(function() {
        $('#waterfallArea').masonry({
            itemSelector: '.content_box',
            columnWidth: 30, //gap
            animate: true,
            horizontalOrder: true,
            originTop: true
        });
    });

    //Fade Out the loading screen when all images loaded
    $('#waterfallArea').imagesLoaded().always(function(instance) {
        $('.loadingScreen').fadeOut();
    });
});