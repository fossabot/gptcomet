import typer

from gptcomet.config_manager import ConfigManager, get_config_manager
from gptcomet.log import logger, set_debug


def entry(
    debug: bool = typer.Option("--debug", "-d", help="Print debug information."),
    local: bool = typer.Option(
        "--local", help="Use local configuration file.", rich_help_panel="Options"
    ),
):
    cfg: ConfigManager = get_config_manager(local=local)
    if debug:
        set_debug()
        logger.debug(f"Using Config path: {cfg.current_config_path}")
    keys: str = cfg.list_keys()
    typer.echo(typer.style("Supported keys:\n", fg=typer.colors.GREEN) + keys)