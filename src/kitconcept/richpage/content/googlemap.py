# -*- coding: utf-8 -*-
from kitconcept.richpage import _
from zope import schema
from zope.interface import Interface
from plone.dexterity.content import Item
from zope.interface import implementer


class IGoogleMap(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    google_map_embed_url = schema.TextLine(
        title=_(u"Google Map embed URL"),
        description=_(u"""Wie bekomme ich die Google Map URL?
1.Öffnen Sie Google Maps.
2.Wenn Sie eine Karte, Street View-Bilder oder eine Route mit anderen teilen
möchten, müssen sie in der aktuellen Kartenansicht zu sehen sein.
3.Klicken Sie zum Teilen auf das Menü .
4.Wählen Sie Karte teilen oder einbetten aus. Wenn Sie diese Option nicht
sehen, klicken Sie stattdessen auf Link zu aktueller Karte.
5.Kopiere den Link und füge ihn in dieses Feld ein."""),
        required=True,
    )


@implementer(IGoogleMap)
class GoogleMap(Item):
    """ The GoogleMap content type """
