import pandas as pd
NEW_NAMES = {
    'id':'student_id',
    'first':'first_name',
    'last':'last_name',
    'age':'age_in_years'
}
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns = NEW_NAMES)