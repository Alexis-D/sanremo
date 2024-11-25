[![CI](https://github.com/Alexis-D/sanremo/actions/workflows/ci.yml/badge.svg)](https://github.com/Alexis-D/sanremo/actions/workflows/ci.yml)

Dummy project to play with modern python packaging/tooling (~~`poetry`, `black`, `isort`, [`rye`](https://rye.astral.sh/)~~, `pipx`, [`uv`](https://docs.astral.sh/uv/)) and github actions.

Produces a CLI that queries <https://ismilansanremoexcitingyet.com/>, and will let you if Milan-San Remo 🚴 is finally
exciting.

Most of the year, and during most of the race, the produced CLI should output something like this:

```
$ sanremo
❌ what did you expect?
$ echo $?
1
```

Wanna try it? Easily install with `pipx install git+https://github.com/Alexis-D/sanremo.git` (or `pipx install .` after
cloning the repo).

---

Note for future self: run `uv run pre-commit install`.

---

Added a `Dockerfile` because why not?

```
$ docker build -t sanremo:latest .
$ docker run --rm sanremo
```
