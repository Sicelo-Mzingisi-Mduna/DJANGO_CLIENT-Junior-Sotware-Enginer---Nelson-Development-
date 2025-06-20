"""
This type stub file was generated by pyright.
"""

from functools import lru_cache
from django import template
from crispy_forms.templatetags.crispy_forms_filters import *

register = ...
class ForLoopSimulator:
    """
    Simulates a forloop tag, precisely::

        {% for form in formset.forms %}

    If `{% crispy %}` is rendering a formset with a helper, We inject a `ForLoopSimulator` object
    in the context as `forloop` so that formset forms can do things like::

        Fieldset("Item {{ forloop.counter }}", [...])
        HTML("{% if forloop.first %}First form text{% endif %}"
    """
    def __init__(self, formset) -> None:
        ...
    
    def iterate(self): # -> None:
        """
        Updates values as if we had iterated over the for
        """
        ...
    


class BasicNode(template.Node):
    """
    Basic Node object that we can rely on for Node objects in normal
    template tags. I created this because most of the tags we'll be using
    will need both the form object and the helper string. This handles
    both the form object and parses out the helper string into attributes
    that templates can easily handle.
    """
    def __init__(self, form, helper, template_pack=...) -> None:
        ...
    
    def get_render(self, context):
        """
        Returns a `Context` object with all the necessary stuff for rendering the form

        :param context: `django.template.Context` variable holding the context for the node

        `self.form` and `self.helper` are resolved into real Python objects resolving them
        from the `context`. The `actual_form` can be a form or a formset. If it's a formset
        `is_formset` is set to True. If the helper has a layout we use it, for rendering the
        form or the formset's forms.
        """
        ...
    
    def get_response_dict(self, helper, context, is_formset): # -> dict[str, Any]:
        """
        Returns a dictionary with all the parameters necessary to render the form/formset in a template.

        :param context: `django.template.Context` for the node
        :param is_formset: Boolean value. If set to True, indicates we are working with a formset.
        """
        ...
    


@lru_cache()
def whole_uni_formset_template(template_pack=...): # -> _BaseTemplate:
    ...

@lru_cache()
def whole_uni_form_template(template_pack=...): # -> _BaseTemplate:
    ...

class CrispyFormNode(BasicNode):
    def render(self, context): # -> SafeText | str:
        ...
    


@register.tag(name="crispy")
def do_uni_form(parser, token): # -> CrispyFormNode:
    """
    You need to pass in at least the form/formset object, and can also pass in the
    optional `crispy_forms.helpers.FormHelper` object.

    helper (optional): A `crispy_forms.helper.FormHelper` object.

    Usage::

        {% load crispy_tags %}
        {% crispy form form.helper %}

    You can also provide the template pack as the third argument::

        {% crispy form form.helper 'bootstrap' %}

    If the `FormHelper` attribute is named `helper` you can simply do::

        {% crispy form %}
        {% crispy form 'bootstrap' %}
    """
    ...

