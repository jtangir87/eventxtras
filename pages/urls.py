"""pages URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.views.generic import TemplateView
from pages.views import contact_us

urlpatterns = [
    path('', TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path('catalogue', TemplateView.as_view(template_name="pages/catalogue.html"), name="catalogue"),
    path('catalogue/photo-novelty', TemplateView.as_view(template_name="pages/photonovelty.html"), name="photo_novelty"),
    path('catalogue/sports-and-games', TemplateView.as_view(template_name="pages/sports_and_games.html"), name="sports_and_games"),
    path('catalogue/glam-and-tattoos', TemplateView.as_view(template_name="pages/glam_and_tattoos.html"), name="glam_and_tattoos"),
    path('catalogue/tailgate', TemplateView.as_view(template_name="pages/tailgate.html"), name="tailgate"),
    path('catalogue/apparel', TemplateView.as_view(template_name="pages/apparel.html"), name="apparel"),
    path('catalogue/fun-foods', TemplateView.as_view(template_name="pages/fun_foods.html"), name="fun_foods"),

    path('contact', contact_us, name="contact_us"),


    ## SERVICE DETAILS ##
    # PHOTO NOVELTY #
    path('catalogue/photo-novelty/infinite-booth', TemplateView.as_view(template_name="pages/photo/infinite.html"), name="infinite_booth"),
    path('catalogue/photo-novelty/ring-booth', TemplateView.as_view(template_name="pages/photo/ring.html"), name="ring_booth"),
    path('catalogue/photo-novelty/swing-booth', TemplateView.as_view(template_name="pages/photo/swing_booth.html"), name="swing_booth"),
    path('catalogue/photo-novelty/cube', TemplateView.as_view(template_name="pages/photo/cube.html"), name="photo_cube"),
    path('catalogue/photo-novelty/slim-booth', TemplateView.as_view(template_name="pages/photo/slim.html"), name="slim_booth"),
    path('catalogue/photo-novelty/green-screen', TemplateView.as_view(template_name="pages/photo/green_screen.html"), name="green_screen"),
    path('catalogue/photo-novelty/digital-pictures', TemplateView.as_view(template_name="pages/photo/digital_pictures.html"), name="digital_pictures"),
    path('catalogue/photo-novelty/tapsnap-42', TemplateView.as_view(template_name="pages/photo/tapsnap_42.html"), name="tapsnap_42"),
    path('catalogue/photo-novelty/tapsnap-studio', TemplateView.as_view(template_name="pages/photo/tapsnap_studio.html"), name="tapsnap_studio"),

    # SPORTS & GAMES #
    path('catalogue/sports-and-games/20-player-foosball', TemplateView.as_view(template_name="pages/sports_games/ledfoosball.html"), name="led_foosball"),
    path('catalogue/sports-and-games/game-cube', TemplateView.as_view(template_name="pages/sports_games/game_cube.html"), name="game_cube"),
    path('catalogue/sports-and-games/led-street-hoops', TemplateView.as_view(template_name="pages/sports_games/ledstreethoops.html"), name="led_street_hoops"),
    path('catalogue/sports-and-games/led-ping-pong', TemplateView.as_view(template_name="pages/sports_games/ledpingpong.html"), name="led_ping_pong"),
    path('catalogue/sports-and-games/virtual-sports', TemplateView.as_view(template_name="pages/sports_games/virtual_sports.html"), name="virtual_sports"),
    path('catalogue/sports-and-games/led-air-hockey', TemplateView.as_view(template_name="pages/sports_games/ledairhockey.html"), name="led_air_hockey"),
    path('catalogue/sports-and-games/pop-a-shot', TemplateView.as_view(template_name="pages/sports_games/popashot.html"), name="popashot"),
    path('catalogue/sports-and-games/football-toss', TemplateView.as_view(template_name="pages/sports_games/footballtoss.html"), name="football_toss"),
    path('catalogue/sports-and-games/bubble-hockey', TemplateView.as_view(template_name="pages/sports_games/bubblehockey.html"), name="bubble_hockey"),
    path('catalogue/sports-and-games/bubble-soccer', TemplateView.as_view(template_name="pages/sports_games/bubblesoccer.html"), name="bubble_soccer"),
    path('catalogue/sports-and-games/casino', TemplateView.as_view(template_name="pages/sports_games/casino.html"), name="casino"),

    # GLAM & TATTOOS #
    path('catalogue/glam-and-tattoos/glitter-bar', TemplateView.as_view(template_name="pages/glam_and_tats/glitterbar.html"), name="glitter_bar"),
    path('catalogue/glam-and-tattoos/get-inked', TemplateView.as_view(template_name="pages/glam_and_tats/getinked.html"), name="get_inked"),
    path('catalogue/glam-and-tattoos/choker-bar', TemplateView.as_view(template_name="pages/glam_and_tats/chokerbar.html"), name="choker_bar"),
    path('catalogue/glam-and-tattoos/flash-tattoos', TemplateView.as_view(template_name="pages/glam_and_tats/flashtattoos.html"), name="flash_tattoos"),
    path('catalogue/glam-and-tattoos/glitter-tattoos', TemplateView.as_view(template_name="pages/glam_and_tats/glittertattoos.html"), name="glitter_tattoos"),

    # TAILGATE #
    path('catalogue/tailgate/led-corn-hole', TemplateView.as_view(template_name="pages/tailgate/ledcornhole.html"), name="led_corn_hole"),
    path('catalogue/tailgate/giant-jenga', TemplateView.as_view(template_name="pages/tailgate/giantjenga.html"), name="giant_jenga"),

    # APPAREL #
    path('catalogue/apparel/live-ink', TemplateView.as_view(template_name="pages/apparel/liveink.html"), name="live_ink"),
    path('catalogue/apparel/airbrush', TemplateView.as_view(template_name="pages/apparel/airbrush.html"), name="airbrush"),

    # FUN FOODS #
    path('catalogue/fun-foods/donut-wall', TemplateView.as_view(template_name="pages/fun_foods/donutwall.html"), name="donut_wall"),
    path('catalogue/fun-foods/candy-bar', TemplateView.as_view(template_name="pages/fun_foods/candybar.html"), name="candy_bar"),
    path('catalogue/fun-foods/popcorn', TemplateView.as_view(template_name="pages/fun_foods/popcorn.html"), name="popcorn"),
    path('catalogue/fun-foods/cotton-candy', TemplateView.as_view(template_name="pages/fun_foods/cottoncandy.html"), name="cotton_candy"),


]
