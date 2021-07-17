$(document).ready(function () {

	// Materialize Initialization
	$(".sidenav").sidenav({ edge: "right", draggable: true });
	$("input#password, input#username").characterCounter();
	$(".collapsible").collapsible();
	$(".fixed-action-btn").floatingActionButton({ direction: "left" });
	$(".tooltipped").tooltip();
	$("select").formSelect();
	$(".dropdown-trigger").dropdown();
	

	// Validate Materialize Select Fields
	// Obtained from Code Institute Course Material
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

	// Dynamically Add and Delete Form Input Fields
	// YouTube tutorial by Cody Mind https://www.youtube.com/watch?v=jSSRMC0F6u8

	// Pre-set
	$("#add1").click(function (e) {
		e.preventDefault()
		$("#new-field1").append('<div class="row" id="new-field1"><div class="input-field col s12"><i class="fas fa-swimmer fa-3x prefix azure-text"></i><input type="text" id="pre_set" name="pre_set" class=" validate" required><label for="pre_set">Pre Set</label>' +
			'<input type="button" value="Delete" id="delete1" class="btn-small winter-sky" aria-label="cancel new entry"></div>');
	});
		
	$('body').on('click', '#delete1', function (e) {
		$(this).parent('div').remove();
	});
	// Main-set
	$("#add2").click(function (e) {
		e.preventDefault()
		$("#new-field2").append('<div class="row" id="new-field2"><div class="input-field col s12"><i class="fas fa-swimmer fa-3x prefix azure-text"></i><input id="main_set" name="main_set" class="validate" required><label for="main_set">Main Set</label>' +
			'<input type="button" value="Delete" id="delete2" class="btn-small winter-sky" aria-label="cancel new entry"></div>');
	});
		
	$('body').on('click', '#delete2', function (e) {
		$(this).parent('div').remove();
	});


});

// Print A Set
// Code snippet obtained from: https://www.geeksforgeeks.org/how-to-print-a-page-using-jquery/
$("#print").on("click", function () {
	window.print();
	return false;
});