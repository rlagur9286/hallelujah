gnbClick = false;

(function($){

	$(document).ready(function(){

		$("#gnb").navi({
			show : { opacity: "show", height: "show"},
			hide : { height: "hide"},
			delay : 100,
			click: gnbClick
		});

		$("#gnb .li1:first").addClass("first");
		$("#gnb .li1:last").addClass("last");

	});
	
})(jQuery);
