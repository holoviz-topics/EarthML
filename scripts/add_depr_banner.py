
# Run ONCE in the built gh-pages branch

import glob

# Banner HTML code
banner_html = '''
<div id="deprecation-banner" style="background-color: #3bffad; color: #2f48d3; padding: 10px; text-align: center; font-size: 14px; border: 1px solid #2f4dd3; border-radius: 5px;">
    <strong style="font-size: 18px;">⚠️ IMPORTANT NOTICE ⚠️</strong><br>
    This site is <strong>ARCHIVED</strong> and will <strong>NO LONGER BE UPDATED</strong>.<br>
    For updated Tutorial material, please visit the <a href="https://projectpythia.org/landsat-ml-cookbook/README.html" style="color: #812fd3; text-decoration: underline;">Pythia landsat-ml cookbook</a>.<br>
    For Topic Examples, head over to the <a href="https://examples.holoviz.org/" style="color: #812fd3; text-decoration: underline;">HoloViz Examples</a> website.
</div>

'''

# Glob pattern to match all HTML files
html_files = glob.glob('**/*.html', recursive=True)

for file_path in html_files:
    with open(file_path, 'r+', encoding='utf-8') as file:
        content = file.read()
        body_index = content.find('</header>') + len('</header>')
        if body_index != -1:
            # Insert the banner HTML right after the <body> tag
            content = content[:body_index] + banner_html + content[body_index:]
            file.seek(0)
            file.write(content)
            file.truncate()
