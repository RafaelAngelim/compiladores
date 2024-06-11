class Variable:
    def __init__(self, name, type):
        self.name = name
        self.type = type

variables = []

def add_variable(name, type):
    variables.append(Variable(name, type))

def check_variable(name):
    return any(variable.name == name for variable in variables)

def check_assignment(type1, type2):
    if type1 == 'int' and type2 == 'float':
        return False
    if type1 == 'boolean' and (type2 == 'float' or type2 == 'int'):
        return False
    if type1 == 'float' and type2 == 'boolean':
        return False
    return True

def get_type(name):
    for variable in variables:
        if variable.name == name:
            return variable.type
    return None

def analyze(data):
    lines = data.split('\n')
    for i, line in enumerate(lines):
        if any(kw in line for kw in ['int ', 'float ', 'boolean']):
            parts = line.split()
            type = parts[0]
            name = parts[1].replace(';', '')
            add_variable(name, type)
        elif '=' in line:
            parts = line.split('=')
            variable = parts[0].strip()
            value = parts[1].strip().replace(';', '')
            if not check_variable(variable):
                print(f"Erro semântico: variável '{variable}' não declarada na linha {i+1}")
                return False
            type_variable = get_type(variable)
            if value.isdigit():
                type_value = 'int'
            elif value.replace('.', '', 1).isdigit():
                type_value = 'float'
            elif value in ['True', 'False']:
                type_value = 'boolean'
            elif '+' in value or '-' in value or '*' in value or '/' in value or '%' in value:
                type_value = 'float'  # Ajuste aqui
            else:
                type_value = get_type(value)
            
            if type_variable != type_value:
                print(f"Erro semântico: operação entre tipos incompatíveis na linha {i+1}")
                return False
    return True
