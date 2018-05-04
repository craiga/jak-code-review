from distutils.core import setup
from os import path

readme = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(readme, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
name             = "Jade-Application-Kit",
version          = "v1.3.4",
packages         = ["j"],
url              = "https://codesardine.github.io/Jade-Application-Kit",
license          = "GPLv2",
author           = "Vitor Lopes",
author_email     = "vmnlop@gmail.com",
description      = "Create native web wrappers or write hybrid Web and Desktop applications on Linux, with Python, JavaScript, HTML5, and CSS3 and WebKit.",
long_description = long_description,
download_url     = "https://github.com/codesardine/Jade-Application-Kit/zipball/master",
keywords         = ["Jade Application Kit", "gui", "webkit", "html5", "web technologies", "javascript", "python", "webgl", "css3", "pygobject", "gtk", "desktop", "gnome", "linux"],
classifiers      = [
"Development Status :: 3 - Alpha",
"Intended Audience :: Developers",
"License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
"Operating System :: OS Independent",
"Environment :: Web Environment",
"Environment :: Win32 (MS Windows)",
"Environment :: MacOS X",
"Environment :: X11 Applications",
"Environment :: X11 Applications :: Gnome",
"Environment :: X11 Applications :: GTK",
"Programming Language :: Python :: 3",
"Topic :: Software Development :: Libraries :: Application Frameworks",
"Topic :: Software Development :: Libraries :: Python Modules",
"Topic :: Software Development :: User Interfaces",
        ],
    include_package_data=True,
    package_data={"j":["window.css"]},
    data_files=[
    ("/usr/bin/", ["bin/jak"]),
    ],
)
