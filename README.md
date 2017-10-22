# Thegoldenkoala website

Public site available at https://thegoldenkoala.com

# Install

1. Clone [the sources](https://github.com/YliesC/website.git)

        git clone https://github.com/YliesC/website.git

3. Install python dependancies

        cd website
        virtualenv .
        source bin/activate
        pip install pelican pelican-youtube markdown beautifulsoup4

4. Edit the file pelicanconf.py to add your own configuration
5. Start writing your content
6. Generate your website

        pelican
