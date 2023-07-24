import logging
import multiprocessing as mp
from pathlib import Path

import nipype.interfaces.fsl as fsl
from tqdm import tqdm

logging.basicConfig(
    filename="skull_stripping.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def strip_skull(args: tuple[Path, Path, bool]):
    """Run skull stripping for input file and save in output file

    Args:
        Tuple of
        inp (Path): Source file name for skull striping
        out (Path): Target file name of stripped MRIs
        mask (bool, optional): Whether to return mask of not. Defaults to True. Maked
            files will be saved in the same output folder with _mask suffix
    """
    try:
        bet = fsl.BET(in_file=args[0], out_file=args[1], mask=args[2])
        _ = bet.run()
        logging.info(f"Skull stripping for {args[0]} done!")
    except Exception as e:
        logging.error(f"Skull stripping failed for {args[0]} with error\n{e}")


def bulk_strip_skull(inp: Path, out: Path, mask: bool = True):
    """Run skull stripping in bulk for all the files in `inp` folder and save them
        in `out` folder

    Args:
        inp (Path): Source folder for skull striping
        out (Path): Target folder to save stripped MRIs and masks
        mask (bool, optional): Whether to return mask of not. Defaults to True. Maked
            files will be saved in the same output folder with _mask suffix
    """
    out.mkdir(exist_ok=True)

    pool = mp.Pool()
    files = list(inp.glob("*.nii*"))

    for _ in tqdm(
        pool.imap(strip_skull, [(file, out / file.name, mask) for file in files]),
        total=len(files),
    ):
        ...
    pool.close()
    pool.join()
