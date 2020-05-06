# gen-pptx-from-simple-text

> CLI to generate powerpoint slides from simple text file[s]

## How to install?
> https://pypi.org/project/gen-pptx-from-simple-text/
```bash
pip install gen-pptx-from-simple-text
```

## How should the simple text file like for generating pptx?

Here is a sample text file - [resources/dummy.txt](resources/dummy.txt).
Each section separated by an empty line makes a slide in the generated pptx.

## How to run the CLI?
```bash
$ pptx --help
Usage: pptx [OPTIONS] LYRICS_FILES...

  A powerpoint generator.

Options:
  -pt, --pptx-template-path PATH  [required]
  -ms, --master-slide-idx INTEGER
                                  [default: 0]
  -sl, --slide-layout-idx INTEGER
                                  [default: 6]
  -fs, --font-size INTEGER        [default: 32]
  -fn, --font-name TEXT           [default: Calibri]
  -ns, --dst-dir TEXT             [default: ./generated-pptx]
  -ta, --slide-txt-alignment [left|middle|right]
                                  [default: left]
  --help                          Show this message and exit.
```

```bash
pptx resources/dummy.txt -pt resources/default.pptx
```
**Notes:**
- `--pptx-template-path | -pt` is expecting either a directory with pptx templates or
a pptx template file. When it is a directory, `pptx` will chose one among all the pptx
files found in the directory. The pptx template file should be without any change to
master slide index or in slide layout index. If there are any changes to master slide
index or slide layout, you need to pass corresponding `int` type to `-ms` and `-sl`
options.
A sample pptx template file is available here [resources/black.pptx](resources/).


## FAQs
### How can I add same footer to all pptx[s] built using the CLI?

Add footer to pptx template file to pass with `--pptx-template-path` option

### How to get different backgrounds for the generated pptx files using the CLI?

Create different pptx template files with different backgrounds and pass it on to
`--pptx-template-path` option. See [this](https://youtu.be/AftDaPQwhPg) video on
creating pptx template file.

## How to setup development environment?

```bash
REPO_NAME=gen-pptx-from-simple-text
python -m ~/.venv_${REPO_NAME}
git clone https://github.com/sukujgrg/${REPO_NAME}.git
cd ${REPO_NAME}
source ~/.venv_${REPO_NAME}/bin/activate
pip install -r requirements.txt
```
