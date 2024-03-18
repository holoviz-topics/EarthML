import glob
import re

def remove_banner(html_files):
    banner_pattern = re.compile(r'<div id="deprecation-banner".*?</div>', re.DOTALL)

    for file_path in html_files:
        with open(file_path, 'r+', encoding='utf-8') as file:
            content = file.read()
            new_content = banner_pattern.sub('', content)
            if new_content != content:
                file.seek(0)
                file.write(new_content)
                file.truncate()

html_files = glob.glob('**/*.html', recursive=True)

remove_banner(html_files)