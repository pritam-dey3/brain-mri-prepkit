import typer

from src.registration import bulk_register, register
from src.skull_stripping import strip_skull, bulk_strip_skull

app = typer.Typer()
app.command()(register)
app.command()(bulk_register)
app.command()(strip_skull)
app.command()(bulk_strip_skull)
