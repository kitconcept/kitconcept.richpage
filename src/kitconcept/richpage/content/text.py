# -*- coding: utf-8 -*-
from kitconcept.richpage import _
from zope import schema
from zope.interface import Interface
from plone.dexterity.content import Item
from zope.interface import implementer


class IText(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=False,
    )


@implementer(IText)
class Text(Item):
    """ The Text content type """
