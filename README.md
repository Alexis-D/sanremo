Dummy project to play with modern python packaging/tooling (`poetry`, `black`, `pipx`) and github actions.

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
