import re

files = [
    "/home/mauriciobc/Documentos/Code/videos-gab/RPA-video/index.html",
    "/home/mauriciobc/Documentos/Code/videos-gab/RPA-video/compositions/cena-01-abertura.html",
    "/home/mauriciobc/Documentos/Code/videos-gab/RPA-video/compositions/cena-02-dataviz.html",
    "/home/mauriciobc/Documentos/Code/videos-gab/RPA-video/compositions/cena-03-rh.html",
    "/home/mauriciobc/Documentos/Code/videos-gab/RPA-video/compositions/cena-04-grid.html",
    "/home/mauriciobc/Documentos/Code/videos-gab/RPA-video/compositions/cena-05-highlight.html",
    "/home/mauriciobc/Documentos/Code/videos-gab/RPA-video/compositions/cena-06-pilares.html",
    "/home/mauriciobc/Documentos/Code/videos-gab/RPA-video/compositions/cena-07-fim.html",
]

CDN = '<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>'
PATTERN = re.compile(r'<script>(?:/\*![\s\S]*?</script>)', re.DOTALL)

for path in files:
    content = open(path).read()
    new_content = PATTERN.sub(CDN, content, count=1)
    if new_content != content:
        open(path, "w").write(new_content)
        print(f"OK: {path}")
    else:
        print(f"SKIP (no match): {path}")

