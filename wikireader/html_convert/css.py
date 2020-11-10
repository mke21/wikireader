from pathlib import Path
import os
CSS = """
html {
  scroll-behavior: smooth;
}

body {
  background-color: #111;
  color: #818181;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 16;
}

.content {
    max-width: 80em;
    margin: auto;
}

/* The sidebar menu */
.sidenav {
  width: 300px; /* Set the width of the sidebar */
  height: 100%;
  position: fixed; /* Fixed Sidebar (stay in place on scroll) */
  z-index: 1; /* Stay on top */
  top: 0; /* Stay at the top */
  left: 0;
  background-color: #222; /* Black */
  overflow-x: hidden; /* Disable horizontal scroll */
  overflow-y: auto;
}

/* The navigation menu links */
.sidenav a {
  padding: 6px 8px 6px 16px;
  text-decoration: none;
  color: #818181;
  display: block;
}

/* When you mouse over the navigation links, change their color */
.sidenav a:hover {
  color: #f1f1f1;
}

/* Style page content */
.article {
  margin-left: 160px; /* Same as the width of the sidebar */
  padding: 0px 10px;
}

/* On smaller screens, where height is less than 450px, change the style of the sidebar (less padding and a smaller font size) */
@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
p {
    line-height: 1.6;
}

"""


def get_css():
    """
    gets file from $HOME/.config/wikireader/layout.css or saves default
    and then reads it
    """
    config_dir = Path(os.environ['HOME']) / '.config/wikireader'
    if not config_dir.exists():
        config_dir.mkdir()
    css_file =  config_dir / 'layout.css'
    if not css_file.exists():
        css_file.write_text(CSS)
    return css_file.read_text()
