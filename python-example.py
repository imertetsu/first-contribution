def greet_user(name):
    """
    Función que saluda al usuario.
    """
    return f"Hola, {name}! Bienvenido al proyecto de ejemplo."

#Add collaborators to the list
def get_collaborators(file_path):
    collaborators = []
    with open(file_path, 'r', encoding='utf-8') as file:
        in_collaborators_section = False
        for line in file:
            
            if "## Colaboradores" in line:
                in_collaborators_section = True
                continue
            
            if in_collaborators_section and line.strip() == "":
                continue  
            
            if in_collaborators_section:
                name = line.split(".", 1)[1].strip() if "." in line else line.strip()
                collaborators.append(name)
    return collaborators


# Read collaborators
collaborators = get_collaborators("D:\\Imer\\CursosDictar\\workshopGit\\README.md")
for collaborator in collaborators:
    print(greet_user(collaborator))
