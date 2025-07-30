from pyDOE2 import fracfact
import pandas as pd

def generate_ff_design(num_factors: int) -> pd.DataFrame:
    if not (2 <= num_factors <= 6):
        raise ValueError("Only 2 to 6 binary factors supported.")

    # Generate fractional factorial design string
    design_str_map = {
        2: 'a b',
        3: 'a b ab',
        4: 'a b ab ac',
        5: 'a b ab ac bc',
        6: 'a b ab ac bc abc'
    }
    design_str = design_str_map[num_factors]

    matrix = fracfact(design_str)
    columns = [f"factor_{chr(97+i)}" for i in range(num_factors)]
    return pd.DataFrame(matrix, columns=columns)

if __name__ == "__main__":
    print(generate_ff_design(3))

