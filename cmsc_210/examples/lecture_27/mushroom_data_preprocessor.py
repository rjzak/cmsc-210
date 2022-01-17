"""
     1. cap-shape:                bell=b,conical=c,convex=x,flat=f,knobbed=k,sunken=s
     2. cap-surface:              fibrous=f,grooves=g,scaly=y,smooth=s
     3. cap-color:                brown=n,buff=b,cinnamon=c,gray=g,green=r,pink=p,purple=u,red=e,white=w,yellow=y
     4. bruises?:                 bruises=t,no=f
     5. odor:                     almond=a,anise=l,creosote=c,fishy=y,foul=f,musty=m,none=n,pungent=p,spicy=s
     6. gill-attachment:          attached=a,descending=d,free=f,notched=n
     7. gill-spacing:             close=c,crowded=w,distant=d
     8. gill-size:                broad=b,narrow=n
     9. gill-color:               black=k,brown=n,buff=b,chocolate=h,gray=g,green=r,orange=o,pink=p,purple=u,red=e,white=w,yellow=y
    10. stalk-shape:              enlarging=e,tapering=t
    11. stalk-root:               bulbous=b,club=c,cup=u,equal=e,rhizomorphs=z,rooted=r,missing=?
    12. stalk-surface-above-ring: fibrous=f,scaly=y,silky=k,smooth=s
    13. stalk-surface-below-ring: fibrous=f,scaly=y,silky=k,smooth=s
    14. stalk-color-above-ring:   brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y
    15. stalk-color-below-ring:   brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y
    16. veil-type:                partial=p,universal=u
    17. veil-color:               brown=n,orange=o,white=w,yellow=y
    18. ring-number:              none=n,one=o,two=t
    19. ring-type:                cobwebby=c,evanescent=e,flaring=f,large=l,none=n,pendant=p,sheathing=s,zone=z
    20. spore-print-color:        black=k,brown=n,buff=b,chocolate=h,green=r,orange=o,purple=u,white=w,yellow=y
    21. population:               abundant=a,clustered=c,numerous=n,scattered=s,several=v,solitary=y
    22. habitat:                  grasses=g,leaves=l,meadows=m,paths=p,urban=u,waste=w,woods=d
"""
import csv
import re
from typing import Dict, List, Tuple

key = __doc__


def get_column_defs(key: str) -> List[Tuple[str, Dict[str, str]]]:
    column_def = re.compile(r"\s+\d{1,2}. (?P<column>[\?\w-]+):\s{0,}(?P<keys>[\w=,]+)")
    defs = [("poisonous", {"e": "edible", "p": "poisonous"})]
    for line in key.split("\n"):
        if line:
            match = column_def.match(line)
            if not match:
                raise ValueError(f'Failed to match line: "{line}".')
            column = match.groupdict()["column"]
            key_string = match.groupdict()["keys"]
            abbreviation_map: Dict[str, str] = {}
            for keypair in key_string.split(","):
                label, abbrev = keypair.split("=")
                if abbrev == "?":
                    abbrev = "unknown"
                abbreviation_map[abbrev] = label
            defs.append((column, abbreviation_map))
    return defs


def rewrite_data(key: str):
    column_defs = get_column_defs(key)
    column_names = [c[0] for c in column_defs]
    abbreviation_mapping = dict(column_defs)
    with open("agaricus-lepiota.data", "r") as infile, open("notebooks/agaricus-lepiota.csv", "w") as outfile:
        reader = csv.DictReader(infile, fieldnames=column_names)
        writer = csv.DictWriter(outfile, fieldnames=column_names)
        writer.writeheader()
        for input_row in reader:
            output_row = {}
            for column in column_names:
                abbreviation = input_row[column]
                if abbreviation == "?":
                    value = abbreviation_mapping[column][""]
                else:
                    value = abbreviation_mapping[column][abbreviation]
                output_row[column] = value
            writer.writerow(output_row)
