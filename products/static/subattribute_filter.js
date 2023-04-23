(function (jQuery) {
  jQuery(window).on('load', function() {
    console.log("Document is ready.");
    function fetchSubattributes() {
      console.log("fetchSubattributes() called.");
      let attributeId = jQuery(this).val();
      let subattributeSelect = jQuery(this).closest("tr").find(".subattribute-select");
      let valueField = jQuery(this).closest("tr").find(".value-field");

      if (attributeId) {
        jQuery.getJSON(`/products/attributes/${attributeId}/subattributes/`, function (data) {
          let options = "<option value=''>---------</option>";

          data.forEach(function (subattribute) {
            options += `<option value="${subattribute.id}">${subattribute.name}</option>`;
          });

          subattributeSelect.html(options);
        });
      } else {
        subattributeSelect.html("<option value=''>---------</option>");
        valueField.hide();  // Hide the value field
      }
    }

    jQuery(".attribute-select").change(fetchSubattributes);

    jQuery(".add-row a").click(function () {
      setTimeout(function () {
        jQuery(".attribute-select").off("change", fetchSubattributes);
        jQuery(".attribute-select").change(fetchSubattributes);
      }, 100);
    });

    // Show or hide the value field depending on subattribute selection
    jQuery(".subattribute-select").change(function () {
      let valueField = jQuery(this).closest("tr").find(".value-field");
      if (jQuery(this).val()) {
        valueField.show();
      } else {
        valueField.hide();
      }
    });

    // Hide value fields initially
    jQuery(".value-field").hide();
  });
})(django.jQuery);
