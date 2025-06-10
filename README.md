# Brain MRI Prepkit

Brain MRI Prepkit is a Python toolkit for automating common preprocessing steps in brain MRI analysis, including image registration and skull stripping. It provides a command-line interface for batch processing of MRI files, making it easy to prepare large datasets for further analysis.

## Features

- **Registration**: Aligns MRI images to a common space using a shell script backend.
- **Skull Stripping**: Removes non-brain tissue from MRI images using FSL's BET tool.
- **Batch Processing**: Supports bulk operations for both registration and skull stripping.
- **Command-line Interface**: Simple CLI powered by [Typer](https://typer.tiangolo.com/).

## Installation

> **Requires Python 3.10**

We recommend using [uv](https://docs.astral.sh/uv/getting-started/installation/) to install this package.

```sh
uv pip install git+https://github.com/pritam-dey3/brain-mri-prepkit.git
```

## Dependencies

[FSL](https://fsl.fmrib.ox.ac.uk/fsl/docs/#/) must be installed and available in your system's PATH for skull stripping to work.

## Usage

You can use Brain MRI Prepkit in two ways:

- **Standard Installation & Usage**: Install the package and use the `prepkit` command directly.
- **Running with uvx (No Install)**: Run the CLI without installing, using the `uvx` command.

Choose the method that best fits your workflow. Both provide the same functionality.

---

### Standard Installation & Usage

After installation, the `prepkit` command will be available.

#### Registration

Register a single MRI file:

```sh
prepkit register <input_file> <output_folder>
```

Register all MRI files in a folder:

```sh
prepkit bulk-register <input_folder> <output_folder>
```

#### Skull Stripping

Strip the skull from a single MRI file:

```sh
prepkit strip-skull <input_file> <output_file> [--mask/--no-mask]
```

Strip the skull from all MRI files in a folder:

```sh
prepkit bulk-strip-skull <input_folder> <output_folder> [--mask/--no-mask]
```

---

### Running with uvx (No Install)

If you prefer not to install the package, you can run all commands using `uvx`. Just replace `prepkit` with:

```
uvx --from git+https://github.com/pritam-dey3/brain-mri-prepkit.git prepkit
```

For example:

```sh
uvx --from git+https://github.com/pritam-dey3/brain-mri-prepkit.git prepkit bulk-register examples/ADNI/ examples/ADNI/reg/
uvx --from git+https://github.com/pritam-dey3/brain-mri-prepkit.git prepkit bulk-strip-skull examples/ADNI/ examples/ADNI/stripped/ --mask
```

---

### Example Workflow

Suppose you have MRI files in `examples/ADNI/` and want to register and skull-strip them:

```sh
prepkit bulk-register examples/ADNI/ examples/ADNI/reg/
prepkit bulk-strip-skull examples/ADNI/ examples/ADNI/stripped/ --mask
```

Or, using `uvx` (no install):

```sh
uvx --from git+https://github.com/pritam-dey3/brain-mri-prepkit.git prepkit bulk-register examples/ADNI/ examples/ADNI/reg/
uvx --from git+https://github.com/pritam-dey3/brain-mri-prepkit.git prepkit bulk-strip-skull examples/ADNI/ examples/ADNI/stripped/ --mask
```
