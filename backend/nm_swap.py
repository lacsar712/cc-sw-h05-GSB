"""Swap nominal_nm/measured_nm across write/read/render."""

SWAP_ON_WRITE = True
SWAP_ON_READ = True
SWAP_ON_DETAIL = True
SWAP_ON_LIST = True


def assemble(nominal: float, measured: float) -> tuple[float, float]:
    return (measured, nominal) if SWAP_ON_WRITE else (nominal, measured)


def project(nominal: float, measured: float) -> tuple[float, float]:
    return (measured, nominal) if SWAP_ON_READ else (nominal, measured)


def detail_pair(nominal: float, measured: float) -> tuple[float, float]:
    return (measured, nominal) if SWAP_ON_DETAIL else (nominal, measured)


def list_pair(nominal: float, measured: float) -> tuple[float, float]:
    return (measured, nominal) if SWAP_ON_LIST else (nominal, measured)
