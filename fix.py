import os
import glob
import re

html_files = glob.glob('*.html')
nav_replacement = """      <nav class="Nav">
        <a href="Home.html" class="logo">Mithresh M</a>
        <ul class="Nav-links">
          <li><a href="Home.html"{h_act}>Home</a></li>
          <li><a href="About.html"{a_act}>About</a></li>
          <li><a href="Projects.html"{p_act}>Projects</a></li>
          <li><a href="Resume.html"{r_act}>Resume</a></li>
        </ul>
        <a class="contact-btn" href="Contact.html">Contact Me</a>
      </nav>"""

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()

    h_act = ' class="active"' if file in ['Home.html', 'portfolio.html'] else ''
    a_act = ' class="active"' if file == 'About.html' else ''
    p_act = ' class="active"' if file == 'Projects.html' else ''
    r_act = ' class="active"' if file == 'Resume.html' else ''

    nav_resolved = nav_replacement.format(h_act=h_act, a_act=a_act, p_act=p_act, r_act=r_act)

    content = re.sub(r'<nav class="Nav">.*?</nav>', nav_resolved, content, flags=re.DOTALL)
    
    if file == 'Home.html' or file == 'portfolio.html':
        home_title_rep = """<p class="home-title">
        Web Developer | Designer | Programmer<br /><br />
        <b>Turning concepts into pixel-perfect, fast, and interactive web
        applications powered by modern frameworks and thoughtful
        engineering.</b>
      </p>"""
        content = re.sub(r'<p class="home-title">.*?</p>', home_title_rep, content, flags=re.DOTALL)

    with open(file, 'w') as f:
        f.write(content)

with open('portfolio.css', 'r') as f:
    css = f.read()

vars_rep = """:root {
  --bg-color: #000000;
  --bg-card: rgba(15, 15, 15, 0.4);
  --text-primary: #f8fafc;
  --text-secondary: #94a3b8;
  --accent-color: #22c55e;
  --accent-gradient: linear-gradient(90deg, #10b981, #22c55e, #4ade80);
  --border-light: rgba(255, 255, 255, 0.1);
  --border-medium: rgba(255, 255, 255, 0.15);
  --glass-blur: blur(12px);
}"""
css = re.sub(r':root\s*\{[^}]+\}', vars_rep, css)

nav_css_rep = """/* ───────────── NAVBAR ───────────── */
header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--bg-color);
  padding: 15px 0;
  border-bottom: 1px solid var(--border-light);
}

.Nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
}

.logo {
  display: block;
  font-size: 1.6rem;
  font-weight: 800;
  color: var(--text-primary);
  text-decoration: none;
  background: var(--accent-gradient);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.contact-btn {
  display: inline-block;
  padding: 10px 24px;
  border: 1px solid var(--border-medium);
  border-radius: 20px;
  color: var(--text-primary);
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  transition: all 0.3s ease;
}

.contact-btn:hover {
  background: var(--accent-color);
  color: #000;
  border-color: var(--accent-color);
}

.Nav-links {
  display: flex;
  gap: 30px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.Nav-links a {
  text-decoration: none;
  font-weight: 500;
  color: var(--text-primary);
  font-size: 0.95rem;
  transition: all 0.3s ease;
  position: relative;
  padding-bottom: 5px;
}

.Nav-links a:hover {
  color: var(--accent-color);
}

.Nav-links a.active {
  color: var(--text-primary);
}

.Nav-links a.active::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: var(--accent-gradient);
}"""

css = re.sub(r'/\* ───────────── NAVBAR \(Pill Style\) ───────────── \*/.*?/\* ───────────── PAGE TITLES ───────────── \*/', nav_css_rep + '\n\n/* ───────────── PAGE TITLES ───────────── */', css, flags=re.DOTALL)

css = css.replace('rgba(147, 51, 234', 'rgba(34, 197, 94')
css = css.replace('#a855f7', 'var(--text-primary)')
css = css.replace('#db2777', 'var(--accent-color)')
css = css.replace('#e879f9', 'var(--accent-color)')
css = css.replace('#d8b4fe', 'var(--text-primary)')
css = css.replace('#9333ea', 'var(--accent-color)')

pf_rep = """.profile-photo {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  object-fit: cover;
  border: 4px solid var(--accent-color);
  box-shadow: 0 0 30px rgba(34, 197, 94, 0.3);
  margin-bottom: 30px;
  transition: transform 0.3s;
}"""
css = re.sub(r'\.profile-photo\s*\{[^}]+\}', pf_rep, css)

with open('portfolio.css', 'w') as f:
    f.write(css)

print("Updated perfectly.")
