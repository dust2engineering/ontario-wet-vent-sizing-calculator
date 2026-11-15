#!/usr/bin/env python3
"""Ontario wet vent sizing (OBC 2024, Table 7.5.8.1) + circuit-venting rules (7.5.3.1).
Usage:
  python3 wet_vent_sizing.py --fu 12 --wcs 0
  python3 wet_vent_sizing.py --fu 20 --wcs 2 --downstream-fu 3
--fu is the total fixture-unit load drained to the wet vent; --downstream-fu is the load of the
most downstream fixture (or symmetric pair), which Sentence 7.5.8.1.(2) excludes from sizing.
"""
import argparse
TABLE = [(1.5, 2, None), (2, 4, 3), (3, 12, 8), (4, 36, 14), (5, None, 18), (6, None, 23)]
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fu", type=float, required=True)
    ap.add_argument("--wcs", type=int, choices=[0, 1, 2], default=0, help="water closets served by the wet vent (max 2)")
    ap.add_argument("--downstream-fu", type=float, default=0, help="load of the most downstream fixture/pair, excluded per 7.5.8.1.(2)")
    a = ap.parse_args()
    eff = a.fu - a.downstream_fu
    col = 1 if a.wcs == 0 else 2
    size = None
    for row in TABLE:
        if row[col] is not None and eff <= row[col]:
            size = row[0]; cap = row[col]; break
    print(f"Effective load for sizing: {eff:g} FU (total {a.fu:g} FU less {a.downstream_fu:g} FU downstream fixture, per 7.5.8.1.(2))")
    if size:
        print(f"Minimum wet vent size: NPS {size} (Table 7.5.8.1 capacity {cap} FU, {'not serving water closets' if a.wcs == 0 else 'serving up to 2 water closets - load counted excludes the water closets themselves'})")
    else:
        print("Load exceeds Table 7.5.8.1 for a single wet vent (max 36 FU without water closets, 23 FU of other fixtures with water closets). Split the group or vent conventionally.")
    print("Remember: wet vent length is not limited (7.5.2.1.(1)); water closets must be the most downstream fixtures; trap arms into the wet vent are limited to NPS 2.")
if __name__ == "__main__":
    main()
