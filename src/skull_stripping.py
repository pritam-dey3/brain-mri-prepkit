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
    inp_file, out_file, mask = args
    inp_file = inp_file.resolve().absolute()
    assert inp_file.exists(), f"Input file {inp_file} does not exist"
    out_file = out_file.resolve().absolute()
    out_folder = out_file.parent
    assert out_folder.exists(), f"Output folder {out_folder} does not exist"
    try:
        bet = fsl.BET(in_file=inp_file, out_file=out_file, mask=mask)
        _ = bet.run()
        logging.info(f"Skull stripping for {inp_file} done!")
    except Exception as e:
        logging.error(f"Skull stripping failed for {inp_file} with error\n{e}")


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
