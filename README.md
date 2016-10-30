# svenkreiss.github.io

Prerequisites (in parent folder)

```bash
git clone https://github.com/svenkreiss/pelican-plugins
git clone https://github.com/svenkreiss/pure pelican-theme-pure
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
