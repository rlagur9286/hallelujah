/**
 * @version 1.0
 * @date April 27, 2011
 * @author Elkha (elkha1914@hotmail.com)
 * @copyright (c) 2011 Elkha (http://elkha.kr/)
 **/

/*
	$("#gnb").navi({
		show : { opacity: "show", height: "show"},
		hide : { height: "hide"},
		delay : 100
	});
 */

(function($){
	$.fn.navi = function(args){

		var elkha = jQuery.extend({
			show : { height: "show" },
			hide : { opacity: "hide" },
			speed: "fast",
			delay: 0,
			click: false
		}, args);

		// ieSelect
		var ieSelect = false;
		if($.browser.msie == true) ieSelect = parseInt($.browser.version);

		this.each(function(){
			var gnb = $(this);

			gnb.find("li:has(ul)").hover(function(){
				$(this).addClass("hover");
				if(elkha.click && $(this).children("a").attr("href")=="#") return;
				if(elkha.speed==0 || (ieSelect && ieSelect <= 6)) $(this).children("ul").show();
				else $(this).children("ul:not(:animated)").animate(elkha.show, elkha.speed); 
			}, function(){
				$(this).removeClass("hover");
				if(elkha.click && $(this).children("a").attr("href")=="#") return;
				var hover = $(this);
				setTimeout(function(){
					if(hover.hasClass("hover")) return;
					if(elkha.speed==0 || (ieSelect && ieSelect <= 6)) hover.children("ul").hide();
					else hover.children("ul").animate(elkha.hide, elkha.speed);
				}, elkha.delay);
			});
			gnb.find("a").focus(function(){
				$(this).parent("li").prev("li").find("ul").hide();
				$(this).parent("li").next("li").find("ul").hide();
				if(elkha.click && $(this).attr("href")=="#") return;
				$(this).next("ul").show();
			});
/*
			$("*:not(#gnb a)").focus(function(){
				if(ieSelect) if($(this).parents("#gnb").attr("id")=="gnb") return; // 익스는 *:not 선택이 안되나 ㅜㅜ
				gnb.find("li > ul").hide();
			});
*/
			gnb.find("a").click(function(){
				if($(this).attr("href")=="#") {
					if(elkha.click) {
						if( $(this).next("ul").css("display")=="block" ) $(this).next("ul").hide();
						else $(this).next("ul").show();
					}
					return false;
				}
			});

		});

		return this;
	};
})(jQuery);
