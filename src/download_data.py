from config import MP_API_KEY
from mp_api.client import MPRester # connection with Dataset
from datetime import datetime
import pandas as pd # to treat the dataset

# FIX: use mpr.materials.summary.search (mpr.summary.search is deprecated as of mp-api 0.39+)
# list with materials features we are interested in
fields = ['material_id','formula_pretty','nsites','volume','symmetry',
          'formation_energy_per_atom','energy_above_hull','band_gap','is_stable','is_metal']

# dictionary for the metadata of the dataset 
query_metadata = {
    'query_date': datetime.now().isoformat(),
    'database': 'Materials Project',
    'query': "elements contains Li AND O (all phases — not restricted to binary Li-O)",
    'fields': fields,
    'note': 'Includes ternary/quaternary Li-O-X phases (oxides, phosphates, sulfates, …)',
}

# creates docs variable (list of objects = material), that contains the properties defined in fields of the materials with Li and O, 
with MPRester(MP_API_KEY) as mpr:
    docs = mpr.materials.summary.search(
    elements=['Li', 'O'],
    fields=fields)
print(f'Retrieved: {len(docs)} entries')

# create the list records. records[n] it's a dictionary that correspond to a material, with his property. We now fill the list rocords with all available materials.
records = []
for d in docs:
    cs = d.symmetry.crystal_system.value if d.symmetry else 'unknown'
    records.append({
        'material_id': d.material_id,
        'formula':     d.formula_pretty,
        'nsites':      d.nsites,
        'volume_per_site': d.volume / d.nsites if d.nsites else None,
        'crystal_system':  cs,
        'Ef':     d.formation_energy_per_atom,
        'Ehull':  d.energy_above_hull,
        'Eg':     d.band_gap,
        'is_stable': d.is_stable,
        'is_metal':  d.is_metal,
    })

# converting the list records into a pandas DataFrame
df = pd.DataFrame(records)



