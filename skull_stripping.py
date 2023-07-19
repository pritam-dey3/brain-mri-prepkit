import sys
from pathlib import Path
import nipype.interfaces.fsl as fsl
import multiprocessing as mp
from tqdm import tqdm
import logging


logging.basicConfig(
    filename="skull_stripping.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def run_skull_stripping(args):
    try:
        bet = fsl.BET(in_file=args[0], out_file=args[1], mask=True)
        _ = bet.run()
        logging.info(f"Skull stripping for {args[0]} done!")
    except Exception as e:
        logging.error(f"Skull stripping failed for {args[0]} with error\n{e}")


def parallel_skull_stripping(inp_folder: Path, out_folder: Path):
    out_folder.mkdir(exist_ok=True)

    pool = mp.Pool()
    files = list(inp_folder.glob("*.nii*"))

    for _ in tqdm(
        pool.imap(
            run_skull_stripping, [(file, out_folder / file.name) for file in files]
        ),
        total=len(files),
    ):
        ...
    pool.close()
    pool.join()


if __name__ == "__main__":
    raw_folder = Path(sys.argv[1]).resolve()  # where the raw data is saved
    out_folder = Path(sys.argv[2]).resolve()  # where the out data is saved

    parallel_skull_stripping(raw_folder, out_folder)