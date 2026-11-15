# Ontario Wet Vent Sizing Calculator (OBC Table 7.5.8.1)

Size a wet vent under the Ontario Building Code: Table 7.5.8.1 gives the maximum hydraulic load a wet vent may carry, by pipe size, with and without water closets. The tool applies the Sentence 7.5.8.1.(2) exclusion (the most downstream fixture is not counted), and ships the full wet-vent conditions of 7.5.2.1 and the circuit-venting rules of 7.5.3.1 as data.

**Live web tool:** https://dust2engineering.github.io/ontario-wet-vent-sizing-calculator/web/

## How it works

- Enter the total fixture-unit load and the number of water closets (0, 1 or 2 — never more on a wet vent).
- Subtract the most downstream fixture (or symmetrically connected pair): Sentence 7.5.8.1.(2) excludes it from the sizing load.
- Read the minimum NPS from Table 7.5.8.1 — the water-closet column counts only the OTHER fixtures; the water closets themselves are not counted.
- Then check the installation against the 7.5.2.1 conditions (WCs downstream, NPS 2 trap-arm limit, 4 FU per upper storey, single limited offset, no size reduction). Length is not limited.

## Data in this repository

- `wet-vent-data.json` — Table 7.5.8.1, the 7.5.2.1 wet-vent conditions, the 7.5.3.1 circuit-venting rules and Table 7.5.7.1 minimum vent sizes, as machine-readable JSON.
- All values verified verbatim from the official 2024 Building Code Compendium, Part 7 (O. Reg. 163/24). Note: circuit venting lives in 7.5.3.1 and circuit vent sizing in Table 7.5.8.3 — older references to a '7.5.9 circuit vent table' are wrong for Ontario.

## Command line

```bash
python3 wet_vent_sizing.py --fu 20 --wcs 2 --downstream-fu 3
```

## Worked examples

- [example-bathroom-group.txt](examples/example-bathroom-group.txt)
- [example-no-wc.txt](examples/example-no-wc.txt)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code, the Canadian Electrical Code or CSA B149.1, or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Plumbing. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
