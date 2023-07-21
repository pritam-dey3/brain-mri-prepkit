import logging
import multiprocessing as mp
import sys
from pathlib import Path
from subprocess import PIPE, run

from tqdm import tqdm

logging.basicConfig(
    filename="registration.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def run_registration(args: tuple[Path, Path]):
    inp_file, out_folder = args

    p = run(
        "bash registration.sh " f"{inp_file.parent} {inp_file.name} {out_folder}",
        stdout=PIPE,
        stderr=PIPE,
        text=True,
        shell=True,
    )
    logging.info(f"file: {inp_file.name} \n {p.stdout}")
    if err := p.stderr:
        logging.error(f"file: {inp_file.name} \n {err}")


def parallel_registration(inp_folder: Path, out_folder: Path):
    pool = mp.Pool()
    files = list(inp_folder.glob("*.nii*"))

    out_folder.mkdir(exist_ok=True)

    for _ in tqdm(
        pool.imap(run_registration, [(file, out_folder) for file in files]),
        total=len(files)
    ):
        ...
    pool.close()
    pool.join()


if __name__ == "__main__":
    inp_folder = Path(sys.argv[1]).resolve()  # where the raw data is saved
    out_folder = Path(sys.argv[2]).resolve()  # where you want to save processed scans

    parallel_registration(inp_folder, out_folder)
