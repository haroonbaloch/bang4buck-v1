document.addEventListener('DOMContentLoaded', function () {
      console.log('DOMContentLoaded'); // Add this line
    function updateSubAttributeDropdown(attributeSelect, subAttributeSelect) {
        const attributeId = attributeSelect.value;
        const subAttributeOptions = subAttributeSelect.querySelectorAll('option');

        subAttributeOptions.forEach((option) => {
            if (option.value === '' || option.dataset.attributeId === attributeId) {
                option.style.display = 'block';
            } else {
                option.style.display = 'none';
            }
        });
    }

    function addAttributeChangeListener(attributeSelect, subAttributeSelect) {
        attributeSelect.addEventListener('change', () => {
            updateSubAttributeDropdown(attributeSelect, subAttributeSelect);
        });
    }

const attributeSelects = document.querySelectorAll('.attribute-select:not([id$="__prefix__-attribute"])');
const subAttributeSelects = document.querySelectorAll('.subattribute-select:not([id$="__prefix__-subattribute"])');

        console.log('attributeSelects', attributeSelects); // Add this line
    console.log('subAttributeSelects', subAttributeSelects); // Add this line

    attributeSelects.forEach((attributeSelect, index) => {
        const subAttributeSelect = subAttributeSelects[index];
        updateSubAttributeDropdown(attributeSelect, subAttributeSelect);
        addAttributeChangeListener(attributeSelect, subAttributeSelect);
    });
});
