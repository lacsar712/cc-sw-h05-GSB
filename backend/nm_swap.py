"""Nominal/measured pass-through: all swap bypasses removed."""

SWAP_ON_WRITE = False
SWAP_ON_READ = False
SWAP_ON_DETAIL = False
SWAP_ON_LIST = False


def assemble(nominal: float, measured: float) -> tuple[float, float]:
    return (measured, nominal) if SWAP_ON_WRITE else (nominal, measured)


def project(nominal: float, measured: float) -> tuple[float, float]:
    return (measured, nominal) if SWAP_ON_READ else (nominal, measured)


def detail_pair(nominal: float, measured: float) -> tuple[float, float]:
    return (measured, nominal) if SWAP_ON_DETAIL else (nominal, measured)


def list_pair(nominal: float, measured: float) -> tuple[float, float]:
    return (measured, nominal) if SWAP_ON_LIST else (nominal, measured)
