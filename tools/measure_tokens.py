#!/usr/bin/env python3
"""
measure_tokens.py — Measure token counts for CMN test cases.

Compares the "normal text" form against the CMN form for each case in
docs/cmn/tests.md and reports savingPercent.

Usage:
    python3 tools/measure_tokens.py [--encoding cl100k_base|o200k_base]

Requires tiktoken:
    pip install tiktoken
    # or, on Arch/CachyOS:
    sudo pacman -S python-tiktoken
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass


@dataclass
class Case:
    name: str
    normal: str
    cmn: str


CASES: list[Case] = [
    Case(
        name="001 javaCrud",
        normal=(
            "Este projeto é um CRUD em Java usando Maven. O objetivo é aprender "
            "Java, Maven e organização de código. A aplicação será uma biblioteca "
            "de jogos. Os próximos passos são criar os models e implementar testes."
        ),
        cmn=(
            "cmn1 project javaCrud state\n"
            "goal learnJava maven codeOrg\n"
            "app gameLibrary\n"
            "next createModels implementTests"
        ),
    ),
    Case(
        name="002 aiContext",
        normal=(
            "Quero criar um arquivo Markdown para guardar o contexto atual do "
            "projeto e reutilizar em novos chats com IA. O arquivo deve ser curto, "
            "atualizado e organizado por objetivo, estado atual, decisões, "
            "problemas e próximos passos."
        ),
        cmn=(
            "cmn1 doc aiContext plan\n"
            "goal storeProjectCtx\n"
            "use futureChats\n"
            "format markdown\n"
            "rule keepShort updated organized\n"
            "sections goal state decisions problems next\n"
            "reader aiPrimary humanSecondary"
        ),
    ),
    Case(
        # Historical cautionary case from a removed L3 draft.
        # Demonstrates that over-abbreviation costs ambiguity without paying
        # token savings. Kept as a control case for the §13 ambiguity rules.
        name="003 over-abbreviation (cautionary)",
        normal=(
            "Este projeto é um CRUD em Java usando Maven. O objetivo é aprender "
            "Java e Maven. A aplicação será uma biblioteca de jogos. Os próximos "
            "passos são criar o model e as classes de teste."
        ),
        cmn=(
            "cmn1 p jc s\n"
            "g lj mv\n"
            "a gl\n"
            "nx cm tc"
        ),
    ),
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Measure CMN token savings.")
    parser.add_argument(
        "--encoding",
        default="cl100k_base",
        help="tiktoken encoding name (default: cl100k_base; also try o200k_base)",
    )
    args = parser.parse_args()

    try:
        import tiktoken
    except ImportError:
        sys.stderr.write(
            "tiktoken not installed. Install with:\n"
            "    pip install tiktoken\n"
            "  or on Arch/CachyOS:\n"
            "    sudo pacman -S python-tiktoken\n"
        )
        return 1

    enc = tiktoken.get_encoding(args.encoding)

    print(f"Encoding: {args.encoding}\n")
    header = f"{'Case':<28} {'normal':>8} {'cmn':>6} {'saving%':>8}"
    print(header)
    print("-" * len(header))

    for case in CASES:
        n = len(enc.encode(case.normal))
        m = len(enc.encode(case.cmn))
        saving = (1 - m / n) * 100 if n else 0.0
        print(f"{case.name:<28} {n:>8} {m:>6} {saving:>7.1f}%")

    return 0


if __name__ == "__main__":
    sys.exit(main())
