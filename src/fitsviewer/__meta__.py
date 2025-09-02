# `name` is the name of the package as used for `pip install package`
name = "fitsviewer"
# `path` is the name of the package for `import package`
path = name.lower().replace("-", "_").replace(" ", "_")
# Your version number should follow https://python.org/dev/peps/pep-0440 and
# https://semver.org
version = "0.1"
author = "vtcloud"
author_email = "vtolls@cfa.harvard.edu"
description = "fitsviewer"  # One-liner
url = "https://github.com/vtcloud/SPHEREx_Ices_Simulator"  # your project homepage
license = "CC0 1.0 Universal"  # See https://choosealicense.com
