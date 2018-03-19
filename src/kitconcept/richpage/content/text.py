# -*- coding: utf-8 -*-
from kitconcept.richpage import _
from zope import schema
from zope.interface import Interface
from plone.dexterity.content import Item
from zope.interface import implementer


class IText(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )


@implementer(IText)
class Text(Item):
    """ The Text content type """
