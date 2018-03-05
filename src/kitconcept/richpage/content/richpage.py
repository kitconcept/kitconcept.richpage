# -*- coding: utf-8 -*-
from kitconcept.richpage import _
from plone.dexterity.content import Container
from zope import schema
from zope.interface import implementer
from zope.interface import Interface


class IRichPage(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    subtitle = schema.TextLine(
        title=_(u"Subtitle"),
        required=False,
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False,
        missing_value=u'',
    )


@implementer(IRichPage)
class RichPage(Container):
    """ The RichPage content type """
