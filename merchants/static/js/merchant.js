$(function() {
    $('.item-description').each(function() {
        var $this = $(this);
        $this.popover({
            trigger: 'hover',
            placement: 'top',
            html: true,
            content: $this.html()
        });
    });
});
