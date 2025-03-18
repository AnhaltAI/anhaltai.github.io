"""
Creates a .html that redirects / to /de.
We may parametrize it etc. at some point, but for now the name reflects that it's the DE profile.
"""

import os
from pathlib import Path

REDIRECT_TO_LANG = "de"

HTML_CONTENT = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Redirecting...</title>
    <!--<meta http-equiv="refresh" content="0; URL=/{REDIRECT_TO_LANG}">-->
    <meta http-equiv="refresh" content="0; URL={REDIRECT_TO_LANG}/">
    <!--<link rel="canonical" href="/{REDIRECT_TO_LANG}">-->
    <link rel="canonical" href="{REDIRECT_TO_LANG}/">
</head>
<body>
    Redirecting to <a href="/{REDIRECT_TO_LANG}">/{REDIRECT_TO_LANG}</a>...
</body>
</html>
"""


def get_output_dir() -> Path:
    project_output_dir = os.getenv("QUARTO_PROJECT_OUTPUT_DIR")
    if project_output_dir:
        # we use parent because we assume we're rendering to e.g. _site/de/
        output_dir = Path(project_output_dir).parent
        # print(f"Using {output_dir} from quarto env.")
    else:
        # if we do `quarto run assets/post_render.sh` for some reason
        output_dir = Path("./_site/").resolve()
        if not output_dir.exists():
            raise ValueError(
                f"No QUARTO_PROJECT_OUTPUT_DIR env. variable passed and guessed {output_dir} doesn't exist."
            )
        # print(f"Using default {output_dir}")
    return output_dir


def write_index():
    output_dir = get_output_dir()
    file_path = output_dir / "index.html"

    # Write the HTML content to the file
    file_path.write_text(HTML_CONTENT)

    print(f"Index with redirect created at {file_path}")


def run():
    write_index()


if __name__ == "__main__":
    run()
