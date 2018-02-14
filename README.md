# svenkreiss.github.io

Prerequisites (in parent folder)

```bash
git clone https://github.com/svenkreiss/pelican-plugins
git clone https://github.com/svenkreiss/pure pelican-theme-pure
```

Static assets:

```bash
npm i
cp -r node_modules/katex/dist content/extras/katex
mkdir content/extras/font-awesome
cp -r node_modules/font-awesome/css content/extras/font-awesome/
cp -r node_modules/font-awesome/fonts content/extras/font-awesome/
```

Local development with

```bash
make devserver
```

Publish with

```bash
make github
```

Compile CV

```sh
localcrawl --start cv.html --out content/files --depth=0 --pdf
```

```sh
alias chrome="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
chrome --headless --disable-gpu --dump-dom cv.html > content/files/cv.html
chrome --headless --disable-gpu --print-to-pdf=content/files/cv.pdf cv.html
```
