from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from website.views import PostListView, PostDetailView, PoemListView, PoemDetailView, LetterListView, LetterDetailView


urlpatterns = patterns('website.views',
    url(r'^$', PostListView.as_view(),
        name='home'),
    url(r'^aktuelles/$', PostListView.as_view(), name='aktuelles'),
    url(r'^aktuelles/(?P<slug>[-_\w]+)/$', PostDetailView.as_view(),
        name='post_detail'),
    url(r'^leben/$', TemplateView.as_view(
        template_name="website/zeittafel.html"), name='leben'),
    url(r'^leben/zeittafel/$', TemplateView.as_view(
        template_name="website/zeittafel.html"), name='zeittafel'),
    url(r'^leben/biografie/$', TemplateView.as_view(
        template_name="website/biografie.html"), name='biografie'),
    url(r'^leben/galerie/$', TemplateView.as_view(
        template_name="website/galerie.html"), name='galerie'),
    url(r'^werk/$', TemplateView.as_view(
        template_name="website/neuausgabe.html"), name='werk'),
    url(r'^werk/neuausgabe/$', TemplateView.as_view(
        template_name='website/neuausgabe.html'), name='neuausgabe'),
    url(r'^werk/gedichte/$', PoemListView.as_view(), name='gedichte'),
    url(r'^werk/gedichte/(?P<slug>[-_\w]+)/$', PoemDetailView.as_view(),
        name='poem_detail'),
    url(r'^werk/bibliografie/$', TemplateView.as_view(
        template_name="website/bibliografie.html"), name='bibliografie'),
    url(r'^werk/nachlass/$', TemplateView.as_view(
        template_name="website/nachlass.html"), name='nachlass'),

    url(r'^briefe/$', LetterListView.as_view(), name='briefe'),
    url(r'^briefe/(?P<slug>[-_\w]+)/$', LetterDetailView.as_view(),
        name='letter_detail'),

    url(r'^predigten/$', TemplateView.as_view(
        template_name="website/predigten.html"), name='predigten'),

    url(r'^rezeption/$', TemplateView.as_view(
        template_name="website/rezeption.html"), name='rezeption'),

    url(r'^audio/$', TemplateView.as_view(
        template_name="website/audio.html"), name='audio'),

    url(r'^links/$', TemplateView.as_view(
        template_name="website/links.html"), name='links'),

    url(r'^impressum/$', TemplateView.as_view(
        template_name="website/impressum.html"), name='impressum'),
)
