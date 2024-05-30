

country_map = {
    'Acura': 'Japan', 'Alfa Romeo': 'Italy', 'Audi': 'Germany', 'BAIC': 'China',
    'BAW': 'China', 'Bentley': 'UK', 'BMW': 'Germany', 'Brilliance': 'China',
    'Buick': 'USA', 'BYD': 'China', 'Cadillac': 'USA', 'Changan': 'China',
    'Chery': 'China', 'CheryExeed': 'China', 'Chevrolet': 'USA', 'Chrysler': 'USA',
    'Citroen': 'France', 'Daewoo': 'South Korea', 'DAF': 'Netherlands',
    'Datsun': 'Japan', 'Dayun': 'China', 'De Tomaso': 'Italy', 'DFSK': 'China',
    'Dodge': 'USA', 'Dongfeng (DFM)': 'China', 'DW Hower': 'China', 'Evolute': 'Russia',
    'Exeed': 'China', 'FAW': 'China', 'Ferrari': 'Italy', 'Fiat': 'Italy',
    'Ford': 'USA', 'Foton': 'China', 'GAC': 'China', 'Geely': 'China',
    'Genesis': 'South Korea', 'GMC': 'USA', 'Great Wall': 'China', 'Haima': 'China',
    'Haval': 'China', 'Hawtai': 'China', 'HINO': 'Japan', 'Honda': 'Japan',
    'Hyundai': 'South Korea', 'Infiniti': 'Japan', 'JAC': 'China', 'Jaguar': 'UK',
    'Jeep': 'USA', 'Jetour': 'China', 'Kaiyi': 'China', 'Kia': 'South Korea',
    'Lada': 'Russia', 'Land Rover': 'UK', 'Lexus': 'Japan', 'Lifan': 'China',
    'LiXiang': 'China', 'Luxgen': 'Taiwan', 'Maserati': 'Italy', 'Mazda': 'Japan',
    'Mercedes-Benz': 'Germany', 'Mini (BMW)': 'UK', 'Mitsubishi': 'Japan',
    'Mitsubishi-Fuso / Fuso': 'Japan', 'Nissan': 'Japan', 'Opel': 'Germany',
    'Peugeot': 'France', 'Polestar': 'Sweden', 'Porsche': 'Germany', 'Proton': 'Malaysia',
    'RAM': 'USA', 'Ravon': 'Uzbekistan', 'Renault': 'France', 'Shacman': 'China',
    'SITRAK': 'China', 'Skoda': 'Czech Republic', 'Smart': 'Germany', 'SsangYong': 'South Korea',
    'Subaru': 'Japan', 'Suzuki': 'Japan', 'Tatra': 'Czech Republic', 'Tesla': 'USA',
    'Toyota': 'Japan', 'UAZ': 'Russia', 'Volkswagen': 'Germany', 'Volvo': 'Sweden',
    'Voyah': 'China', 'Zotye': 'China', 'Москвич': 'Russia', 'Урал': 'Russia'
}

pre_segment_map = {
    'Supercar': ['NSX', 'R8', 'F12Berlinetta', 'GT-R', '911', '718', 'Cayman', 'Boxster', 'Cayenne Turbo', 'Cayenne Turbo S', 'Panamera Turbo', 'Panamera Turbo S', 'Taycan', 'Cayenne GTS', 'Cayman GTS', 'Panamera GTS', 'Panamera S', 'Cayman GT4'],
    'Sedan': ['TLX', 'ILX', 'A3', 'A4', 'A6', 'A7', 'A8', '3 Series', '5 Series', '7 Series', 'Civic', 'Accord', 'Camry', 'Corolla', 'Fusion', 'Malibu', 'Passat', 'Jetta', 'Arteon', 'S60', 'S90', 'Impreza', 'Legacy', 'Octavia III', 'Octavia IV', 'Superb'],
    'Van': ['Odyssey', 'Sienna', 'Sprinter', 'Sprinter Classic', 'Vito', 'Tourneo Custom', 'Transit', 'Transit Custom', 'Multivan', 'Caravelle', 'Transporter', 'Caddy', 'Caddy California', 'Zafira Life', 'Vivaro', 'Combo Cargo', 'Combo Life', 'Berlingo', 'Jumper', 'Jumpy', 'SpaceTourer', 'Grand Voyager', 'Pacifica', 'Espace', 'Kangoo Fourgon', 'Kangoo Passenger', 'Profi'],
    'SUV': ['MDX', 'RDX', 'Q3', 'Q5', 'Q7', 'Q8', 'X1', 'X3', 'X5', 'X6', 'X7', 'Explorer', 'CR-V', 'Rav4', 'Highlander', '4Runner', 'Grand Cherokee', 'Cherokee', 'Wrangler', 'Compass', 'Renegade', 'Pilot', 'Escape', 'Expedition', 'Tahoe', 'Suburban', 'Traverse', 'Equinox', 'Blazer', 'TrailBlazer', 'Kodiaq', 'Karoq', 'Tiguan', 'Touareg', 'Atlas', 'Atlas Cross Sport', 'Taos', 'ID.4', 'Teramont', 'Tayron', 'Tayron X', 'Seltos', 'Sportage', 'Sorento', 'Niro', 'Telluride', 'Kona', 'Santa Fe', 'Palisade', 'Tucson', 'C-HR', 'Land Cruiser Prado', 'Land Cruiser 200', 'Land Cruiser 300', 'Hilux', 'Sequoia', 'Fortuner', 'Alphard', 'Venza', 'RX', 'NX', 'UX', 'GX', 'LX', 'XT4', 'XT5', 'XT6', 'SRX', 'Escalade', 'RX', 'NX', 'UX', 'GX', 'LX', 'Murano', 'Rogue', 'Pathfinder', 'Armada', 'Kicks', 'Qashqai', 'X-Trail', 'Yeti', 'Q5', 'Macan', 'Cayenne', 'Cayenne Coupe', 'Bentayga', 'Urus', 'Levante', 'G-Class', 'GLB-Class', 'GLC-Class', 'GLE-Class', 'GLS-Class', 'G-Class', 'EQC', 'I-Pace', 'E-Pace', 'F-Pace', 'Tiggo 8', 'Tiggo 7', 'Tiggo 5', 'Tiggo 3', 'H6', 'H9', 'H8', 'H2', 'Haval', 'Atlas', 'Monjaro', 'Atlas Pro', 'Coolray', 'Tugella', 'GC6', 'GS', 'Trax', 'Terrain', 'Acadia', 'Encore', 'Hummer EV'],
    'Hatchback': ['Focus', 'Fiesta', 'Golf', 'Fit', 'Polo', 'Mini', 'Mini Clubman', 'Mini Countryman', 'Mini Paceman', 'Clio', 'i3'],
    'Coupe': ['Mustang', 'Camaro', 'M3', 'M4', 'Challenger', '370Z', '4C', 'TT', 'A5', 'S5', 'RS 5', 'RC', 'LC', 'CLK-Class', 'E-Class Coupe', 'C-Class Coupe'],
    'Convertible': ['Boxster', 'Z4', 'TT Roadster', 'A5 Cabriolet', 'Mustang Convertible', 'Camaro Convertible', 'Miata', 'SLC-Class', 'SL-Class', 'E-Class Cabriolet', 'C-Class Cabriolet'],
    'Pickup': ['F-150', 'Ranger', 'Silverado', 'Sierra', 'Tacoma', 'Tundra', 'Ram 1500', 'Ram 1500 Classic', 'Colorado', 'Canyon', 'Ridgeline', 'Titan', 'Frontier', 'Gladiator'],
}

# Функция для удаления повторяющихся моделей
def remove_duplicates(segment_map):
    seen = set()
    for segment, models in segment_map.items():
        unique_models = []
        for model in models:
            if model not in seen:
                seen.add(model)
                unique_models.append(model)
        segment_map[segment] = unique_models
    return segment_map

# Удаление дубликатов
segment_map = remove_duplicates(pre_segment_map)



