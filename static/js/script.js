$(document).ready(function () {
	$(".sidenav").sidenav({ edge: "right", draggable: true });
	$("input#password, input#username").characterCounter();
	$(".collapsible").collapsible();
	$(".fixed-action-btn").floatingActionButton({ direction: "left" });
	$(".tooltipped").tooltip();
	$("select").formSelect();
	$(".dropdown-trigger").dropdown();
	$('.parallax').parallax();

	// Customise Materialize Select Validation
	validateMaterializeSelect();
	function validateMaterializeSelect() {
		let classValid = {
			"border-bottom": "1px solid #4dec38",
			"box-shadow": "0 1px 0 0 #4dec38",
		};
		let classInvalid = {
			"border-bottom": "1px solid #ff006e",
			"box-shadow": "0 1px 0 0 #ff006e",
		};
		if ($("select.validate").prop("required")) {
			$("select.validate").css({
				display: "block",
				height: "0",
				padding: "0",
				width: "0",
				position: "absolute",
			});
		}
		$(".select-wrapper input.select-dropdown")
			.on("focusin", function () {
				$(this)
					.parent(".select-wrapper")
					.on("change", function () {
						if (
							$(this)
								.children("ul")
								.children("li.selected:not(.disabled)")
								.on("click", function () {})
						) {
							$(this).children("input").css(classValid);
						}
					});
			})
			.on("click", function () {
				if (
					$(this)
						.parent(".select-wrapper")
						.children("ul")
						.children("li.selected:not(.disabled)")
						.css("background-color") === "rgba(0, 0, 0, 0.03)"
				) {
					$(this).parent(".select-wrapper").children("input").css(classValid);
				} else {
					$(".select-wrapper input.select-dropdown").on(
						"focusout",
						function () {
							if (
								$(this)
									.parent(".select-wrapper")
									.children("select")
									.prop("required")
							) {
								if (
									$(this).css("border-bottom") != "1px solid rgb(77, 236, 56)"
								) {
									$(this)
										.parent(".select-wrapper")
										.children("input")
										.css(classInvalid);
								}
							}
						}
					);
				}
			});
	}
});
