from pages.multipage import MultiPage


# Import Pages
from pages.art import body_art

# Show Pages
app = MultiPage(app_name='Niklas Strassmann')

app.app_page('Art', body_art)

app.run()