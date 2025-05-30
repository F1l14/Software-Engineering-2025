import os
import ast

def get_classes_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        node = ast.parse(file.read(), filename=filepath)
    return [n for n in node.body if isinstance(n, ast.ClassDef)]

def extract_class_info(class_node):
    class_name = class_node.name
    base_classes = [base.id for base in class_node.bases if isinstance(base, ast.Name)]
    inheritance = ', '.join(base_classes) if base_classes else None

    attributes = set()
    static_attributes = set()
    methods = []

    for item in class_node.body:
        # Static/class-level attributes
        if isinstance(item, ast.Assign):
            for target in item.targets:
                if isinstance(target, ast.Name):
                    attr_name = target.id
                    visibility = detect_visibility(attr_name)
                    static_attributes.add((attr_name, visibility))
        # Methods
        elif isinstance(item, ast.FunctionDef):
            # __init__ → detect instance (self.) attributes
            if item.name == '__init__':
                for stmt in item.body:
                    if isinstance(stmt, ast.Assign):
                        for target in stmt.targets:
                            if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == 'self':
                                attr_name = target.attr
                                visibility = detect_visibility(attr_name)
                                attributes.add((attr_name, visibility))
            # All method definitions
            method_name = item.name
            params = get_params(item)
            return_type = get_return_type(item)
            methods.append((method_name, params, return_type))

    return class_name, inheritance, sorted(attributes), sorted(static_attributes), sorted(methods)

def detect_visibility(attr_name):
    if attr_name.startswith("__") and not attr_name.endswith("__"):
        return "-"  # Private
    elif attr_name.startswith("_"):
        return "#"  # Protected
    else:
        return "+"  # Public

def get_params(func_node):
    args = func_node.args.args
    start_index = 1 if args and args[0].arg in ("self", "cls") else 0
    param_list = []

    for arg in args[start_index:]:
        if arg.annotation:
            annotation = ast.unparse(arg.annotation)
            param_list.append(f"{arg.arg}: {annotation}")
        else:
            param_list.append(arg.arg)

    return ", ".join(param_list)

def get_return_type(func_node):
    if func_node.returns:
        return ast.unparse(func_node.returns)
    return None

def generate_uml_text_for_class(class_name, inheritance, attributes, static_attributes, methods):
    header = f"Class {class_name}" + (f" : {inheritance}" if inheritance else "")
    lines = [header, "-" * len(header)]

    lines.append("Attributes:")
    for attr_name, visibility in attributes:
        lines.append(f"  {visibility} {attr_name}")
    for attr_name, visibility in static_attributes:
        lines.append(f"  {visibility} {attr_name} «static»")

    lines.append("Methods:")
    for name, params, return_type in methods:
        return_str = f" -> {return_type}" if return_type else ""
        lines.append(f"  + {name}({params}){return_str}")

    lines.append("")  # Empty line between classes
    return "\n".join(lines)

def scan_project_for_classes(directory):
    uml_output = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".py"):
                filepath = os.path.join(root, filename)
                try:
                    classes = get_classes_from_file(filepath)
                    for class_node in classes:
                        class_name, base, attrs, statics, methods = extract_class_info(class_node)
                        uml_output.append(generate_uml_text_for_class(class_name, base, attrs, statics, methods))
                except Exception as e:
                    print(f"Failed to parse {filepath}: {e}")
    return "\n".join(uml_output)

# === Main script ===
if __name__ == "__main__":
    project_path = "."  # Or replace with a specific path
    output_file = "uml_output.txt"

    result = scan_project_for_classes(project_path)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"UML-like class summary with parameters and return types written to {output_file}")
