
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Attribute, Category, SubAttribute

class AttributeResource(resources.ModelResource):
    category = fields.Field(
        column_name='category',
        attribute='category',
        widget=ForeignKeyWidget(Category, 'name')
    )
    subname = fields.Field(column_name='subname', attribute='subname')

    class Meta:
        model = Attribute
        fields = ('id', 'name', 'subname', 'category')
        export_order = ('id', 'name', 'subname', 'category')

    def before_import_row(self, row, **kwargs):
        subattribute_name = row.get('subname')
        if subattribute_name:
            attribute_name = row.get('name')
            category_name = row.get('category') # add this line
            category = Category.objects.get(name=category_name) # add this line
            attribute, _ = Attribute.objects.get_or_create(name=attribute_name, category=category) # modify this line
            SubAttribute.objects.get_or_create(name=subattribute_name, attribute=attribute)
            row['id'] = attribute.id

# class SubAttributeResource(resources.ModelResource):
#     attribute = fields.Field(
#         column_name='attribute_name',
#         attribute='attribute',
#         widget=ForeignKeyWidget(Attribute, 'name')
#     )
#
#     class Meta:
#         model = SubAttribute
#         fields = ('id', 'name', 'attribute')
