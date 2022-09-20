from pages.multipage import MultiPage


# Import Pages
from pages.art import body_art
from pages.hero import body_hero

# create app as a platform
app = MultiPage(app_name='Niklas Strassmann')

# Show pages
app.app_page('Art', body_art)
app.app_page('Hero', body_hero)

app.run()