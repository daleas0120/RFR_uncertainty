def get_samples_w_element_X(df, col_w_atomic_formula, element):
    list_of_idx = []
    str_of_element_second_char = "abcdefghijklmnopqrstuvwxyz"

    if len(element) == 1:
        for i, formula in enumerate(df[col_w_atomic_formula]):
            if element in formula:
                element_idx = formula.index(element)
                if (element_idx + 1) == len(formula):
                    list_of_idx.append(i)
                elif formula[element_idx+1] in str_of_element_second_char:
                    continue
    elif len(element) == 2:
        for i, formula in enumerate(df[col_w_atomic_formula]):
            if element in formula:
                list_of_idx.append(i)
    else:
        print('Error in element definition')

    return list_of_idx

def format_dataset(data):
    data = data.dropna(axis=1)
    for col in data.columns:
        if type(data[col].values[0]) == str:
            data = data.drop(axis=1, columns=col)
        elif type(data[col].values[0]) == np.bool_:
            data = data.drop(axis=1, columns=col)

    data = data.drop(axis=1, columns='atoms')


def get_target_label():
    X = data.iloc[sample_list].drop(axis=1, columns=target).values
    y = data.iloc[sample_list][target].values
    return X, y