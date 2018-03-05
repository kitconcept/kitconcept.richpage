# -*- coding: utf-8 -*-
from kitconcept.richpage import _
from plone.app.textfield import RichText as RichTextField
from plone.app.z3cform.widget import RichTextFieldWidget
from plone.autoform import directives as form
from plone.dexterity.content import Container
from plone.namedfile import field as namedfile
from zope import schema
from zope.interface import implementer
from zope.interface import Interface


class ISlideshow(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=False,
    )

    slide1_image = namedfile.NamedBlobImage(
        title=_(u'label_slideimage',
                default=u'Slide Bild ${number}', mapping={'number': '1'}),
        description=u'',
        required=False,
    )

    slide1_text = RichTextField(
        title=_(u'label_slidetext',
                default=u'Slide Text ${number}', mapping={'number': '1'}),
        description=u'',
        required=False,
    )
    form.widget('slide1_text', RichTextFieldWidget)

    slide1_image = namedfile.NamedBlobImage(
        title=_(u'label_slideimage',
                default=u'Slide Bild ${number}', mapping={'number': '1'}),
        description=u'',
        required=False,
    )

    slide1_text = RichTextField(
        title=_(u'label_slidetext',
                default=u'Slide Text ${number}', mapping={'number': '1'}),
        description=u'',
        required=False,
    )
    form.widget('slide1_text', RichTextFieldWidget)

    slide2_image = namedfile.NamedBlobImage(
        title=_(u'label_slideimage',
                default=u'Slide Bild ${number}', mapping={'number': '2'}),
        description=u'',
        required=False,
    )

    slide2_text = RichTextField(
        title=_(u'label_slidetext',
                default=u'Slide Text ${number}', mapping={'number': '2'}),
        description=u'',
        required=False,
    )
    form.widget('slide2_text', RichTextFieldWidget)

    slide3_image = namedfile.NamedBlobImage(
        title=_(u'label_slideimage',
                default=u'Slide Bild ${number}', mapping={'number': '3'}),
        description=u'',
        required=False,
    )

    slide3_text = RichTextField(
        title=_(u'label_slidetext',
                default=u'Slide Text ${number}', mapping={'number': '3'}),
        description=u'',
        required=False,
    )
    form.widget('slide3_text', RichTextFieldWidget)

    slide4_image = namedfile.NamedBlobImage(
        title=_(u'label_slideimage',
                default=u'Slide Bild ${number}', mapping={'number': '4'}),
        description=u'',
        required=False,
    )

    slide4_text = RichTextField(
        title=_(u'label_slidetext',
                default=u'Slide Text ${number}', mapping={'number': '4'}),
        description=u'',
        required=False,
    )
    form.widget('slide4_text', RichTextFieldWidget)

    slide5_image = namedfile.NamedBlobImage(
        title=_(u'label_slideimage',
                default=u'Slide Bild ${number}', mapping={'number': '5'}),
        description=u'',
        required=False,
    )

    slide5_text = RichTextField(
        title=_(u'label_slidetext',
                default=u'Slide Text ${number}', mapping={'number': '5'}),
        description=u'',
        required=False,
    )
    form.widget('slide5_text', RichTextFieldWidget)

    slide6_image = namedfile.NamedBlobImage(
        title=_(u'label_slideimage',
                default=u'Slide Bild ${number}', mapping={'number': '6'}),
        description=u'',
        required=False,
    )

    slide6_text = RichTextField(
        title=_(u'label_slidetext',
                default=u'Slide Text ${number}', mapping={'number': '6'}),
        description=u'',
        required=False,
    )
    form.widget('slide6_text', RichTextFieldWidget)

    slide7_image = namedfile.NamedBlobImage(
        title=_(u'label_slideimage',
                default=u'Slide Bild ${number}', mapping={'number': '7'}),
        description=u'',
        required=False,
    )

    slide7_text = RichTextField(
        title=_(u'label_slidetext',
                default=u'Slide Text ${number}', mapping={'number': '7'}),
        description=u'',
        required=False,
    )
    form.widget('slide7_text', RichTextFieldWidget)

    slide8_image = namedfile.NamedBlobImage(
        title=_(u'label_slideimage',
                default=u'Slide Bild ${number}', mapping={'number': '8'}),
        description=u'',
        required=False,
    )

    slide8_text = RichTextField(
        title=_(u'label_slidetext',
                default=u'Slide Text ${number}', mapping={'number': '8'}),
        description=u'',
        required=False,
    )
    form.widget('slide8_text', RichTextFieldWidget)

    slide9_image = namedfile.NamedBlobImage(
        title=_(u'label_slideimage',
                default=u'Slide Bild ${number}', mapping={'number': '9'}),
        description=u'',
        required=False,
    )

    slide9_text = RichTextField(
        title=_(u'label_slidetext',
                default=u'Slide Text ${number}', mapping={'number': '9'}),
        description=u'',
        required=False,
    )
    form.widget('slide9_text', RichTextFieldWidget)

    slide10_image = namedfile.NamedBlobImage(
        title=_(u'label_slideimage',
                default=u'Slide Bild ${number}', mapping={'number': '10'}),
        description=u'',
        required=False,
    )

    slide10_text = RichTextField(
        title=_(u'label_slidetext',
                default=u'Slide Text ${number}', mapping={'number': '10'}),
        description=u'',
        required=False,
    )
    form.widget('slide10_text', RichTextFieldWidget)


@implementer(ISlideshow)
class Slideshow(Container):
    """ The Slideshow content type """
