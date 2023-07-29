import logging
import multiprocessing as mp
from pathlib import Path
from subprocess import PIPE, run

from tqdm import tqdm

logging.basicConfig(
    filename="registration.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def register(args: tuple[Path, Path]):
    """Run register for input file into output folder

    Args:
        args (tuple[Path, Path]): Tuple of (input_file, output_folder)
    """
    inp_file, out_folder = args

    script_path = Path(__file__).parent / "registration.sh"
    p = run(
        (
            "bash"
            f" {script_path} {inp_file.parent} {inp_file.name} {out_folder}"
        ),
        stdout=PIPE,
        stderr=PIPE,
        text=True,
        shell=True,
    )
    logging.info(f"file: {inp_file.name} \n {p.stdout}")
    if err := p.stderr:
        logging.error(f"file: {inp_file.name} \n {err}")


def bulk_register(inp: Path, out: Path):
    """Run registration for all the files in `inp` folder and store them in `out` folder

    Args:
        inp (Path): Source folder for registration of MRI files
        out (Path): Destination folder
    """
    pool = mp.Pool()
    files = list(inp.glob("*.nii*"))

    out.mkdir(exist_ok=True)

    for _ in tqdm(
        pool.imap(register, [(file, out) for file in files]),
        total=len(files),
    ):
        ...
    pool.close()
    pool.join()
