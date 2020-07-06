# Examples

## Example Builder Tool

- Build multiple examples of various analysis routines from shared model definition files.
- Provides a central serialized roster of all examples (`conf.yml`).

### Workflow

empty

### Schema
|   |  |
|---|---|
| `id` | this serves as both the name of the documentation `.rst` file, and the name of the directory which will hold the source files. |
| `title` | This will serve as the title of the documentation web page. |
| `docs` | This object contains strings that are used to populate the `example.md` template with Jinja. Pandoc is then used to translate the markdown string produced by Jinja to an `.rst` file. |
| `input` | This object comprises the information of the `input.json` file for the example. |

Proposed script naming convention:

- `model.py`, `model.tcl`: a file that defines an FE model, but does not include post processing.
- `fem.py`, `fem.tcl`: a file that defines a FE model *and* the post-processing routine.

-------------------------------------------

**SAMPLE EXAMPLE STRUCTURE:**

## [H2] Example name

Brief description of the example, with paragraph structure roughly as follows:

[statement]

1. Begin with a general problem statement.
2. Specify specifics (e.g. dimensions, parameters, etc.).

[files]

### [H3] [fem]

Walk user through setup of the FE model with a description of each input file used.

### [H3] [uq]

Explain the problem workflow. This section should explain what information is passed to and from the modeling scripts introduced in the following section.


### [H3] Results

Explain the output that is generated and what visualizations are available from the GUI.

-------------------------------------------
