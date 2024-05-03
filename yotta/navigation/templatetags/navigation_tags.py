from django import template

register = template.Library()


# Primary nav desktop snippet
@register.inclusion_tag(
    "components/navbar.html", takes_context=True
)
def primarynav(context):
    request = context["request"]
    return {
        "primarynav": context["settings"]["navigation"][
            "NavigationSettings"
        ].primary_navigation,
        "request": request,
    }

# Footer nav snippets
@register.inclusion_tag(
    "components/footer.html", takes_context=True
)
def footernav(context):
    request = context["request"]
    return {
        "footernav": context["settings"]["navigation"][
            "NavigationSettings"
        ].footer_links,
        "request": request,
    }