import os
import glob

html_files = glob.glob("*.html")
target = """<p style="color: rgba(255,255,255,0.7);">We provide top-notch veterinary services, focusing on the health, happiness, and well-being of your beloved pets.</p>"""

replacement = """<p style="color: rgba(255,255,255,0.7);">We provide top-notch veterinary services, focusing on the health, happiness, and well-being of your beloved pets.</p>
                    <div class="social-links" style="display: flex; gap: 15px; margin-top: 25px;">
                        <a href="#" style="background: rgba(255,255,255,0.1); color: var(--white-color); width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 16px; transition: var(--transition);" onmouseover="this.style.background='var(--accent-color)'" onmouseout="this.style.background='rgba(255,255,255,0.1)'"><i class="fa-brands fa-facebook-f"></i></a>
                        <a href="#" style="background: rgba(255,255,255,0.1); color: var(--white-color); width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 16px; transition: var(--transition);" onmouseover="this.style.background='var(--accent-color)'" onmouseout="this.style.background='rgba(255,255,255,0.1)'"><i class="fa-brands fa-twitter"></i></a>
                        <a href="#" style="background: rgba(255,255,255,0.1); color: var(--white-color); width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 16px; transition: var(--transition);" onmouseover="this.style.background='var(--accent-color)'" onmouseout="this.style.background='rgba(255,255,255,0.1)'"><i class="fa-brands fa-instagram"></i></a>
                        <a href="#" style="background: rgba(255,255,255,0.1); color: var(--white-color); width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 16px; transition: var(--transition);" onmouseover="this.style.background='var(--accent-color)'" onmouseout="this.style.background='rgba(255,255,255,0.1)'"><i class="fa-brands fa-linkedin-in"></i></a>
                    </div>"""

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target in content and "fa-facebook-f" not in content[content.find(target):content.find(target)+1000]:
        new_content = content.replace(target, replacement)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated {file}")

print(f"Total files updated: {count}")
