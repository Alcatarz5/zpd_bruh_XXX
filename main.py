import os
import re


def initialization_parser(row: str):
    a = [s for s in re.split('[=|;|\s+]+', row)]
    # print(a)
    return a


def assignment_parser(row: str):
    a = [s for s in re.split('[=|;|\s+]+', row)]
    # print(a)
    return a


def addition_common_parser(row: str):
    a = [s for s in re.split('[=|;|+|\s+]+', row)]
    # print(a)
    return a


def addition_uncommon_parser(row: str):
    a = [s for s in re.split('[=|;|+|\s+]+', row)]
    a.insert(1, a[0])
    # print(a)
    return a

def multiplication_common_parser(row: str):
    a = [s for s in re.split('[=|;|*|\s+]+', row)]
    # print(a)
    return a

def multiplication_uncommon_parser(row: str):
    a = [s for s in re.split('[=|;|*|\s+]+', row)]
    a.insert(1, a[0])
    # print(a)
    return a

def decrease_common_parser(row: str):
    a = [s for s in re.split('[=|;|\-|\s+]+', row)]
    print(a)
    return a

def decrease_uncommon_parser(row: str):
    a = [s for s in re.split('[=|;|\-|\s+]+', row)]
    a.insert(1, a[0])
    print(a)
    return a

def division_common_parser(row: str):
    a = [s for s in re.split('[=|;|/|\s+]+', row)]
    # print(a)
    return a

def division_uncommon_parser(row: str):
    a = [s for s in re.split('[=|;|/|\s+]+', row)]
    a.insert(1, a[0])
    # print(a)
    return a

def modulo_common_parser(row: str):
    a = [s for s in re.split('[=|;|%|\s+]+', row)]
    return a

def modulo_uncommon_parser(row: str):
    a = [s for s in re.split('[=|;|%|\s+]+', row)]
    a.insert(1, a[0])
    return a


def main():
    file_path = '/home/bendamvn/zpd_bruh_XXX/test.txt'
    with open(file_path, 'r') as f:
        code = [line.strip() for line in f]
        result = []
        data = []
        for code_line in code:
            initialization = re.search("^\s*int\s[A-Za-z_]\w*\s*=\s*\d+\s*;$", code_line)
            if initialization:
                parser_result = initialization_parser(initialization.group(0))
                data.append({'data_type': parser_result[0], 'variable': parser_result[1], 'value': parser_result[2]})
                continue

            assignment = re.search("^\s*(?!int$)[A-Za-z_]\w*\s*=\s*\w+\s*;$", code_line)
            if assignment:
                parser_result = assignment_parser(assignment.group(0))
                result.append({'operation_type': 'ass', 'content': {'variable': parser_result[0],
                                                                    'value': parser_result[1]}})
                continue

            addition_common = re.search("^\s*[A-Za-z_]\w*\s*=\s*\w+\s\+?\s\w*\s*;$", code_line)
            addition_uncommon = re.search("^\s*[A-Za-z_]\w*\s\+*=\s*\w+\s*;$", code_line)
            if addition_common:
                parser_result = addition_common_parser(addition_common.group(0))
                result.append({'operation_type': 'add', 'content': {'variable': parser_result[0],
                                                                    'term1': parser_result[1],
                                                                    'term2': parser_result[2]}})
                continue
            elif addition_uncommon:
                parser_result = addition_uncommon_parser(addition_uncommon.group(0))
                result.append({'operation_type': 'add', 'content': {'variable': parser_result[0],
                                                                    'term1': parser_result[1],
                                                                    'term2': parser_result[2]}})
                continue

            multiplication_common = re.search("^\s*[A-Za-z_]\w*\s*=\s*[A-Za-z_]?\w*\s*\*\s*[A-Za-z_]?\w*\s*;$", code_line)
            multiplication_uncommon = re.search("^\s*[A-Za-z_]\w*\s*\*=\s*[A-Za-z_]?\w*\s*;$", code_line)
            if multiplication_common:
                parser_result = multiplication_common_parser(multiplication_common.group(0))
                result.append({'operation_type': 'mult', 'content': {'variable': parser_result[0],
                                                                    'factor1': parser_result[1],
                                                                    'factor2': parser_result[2]}})
                continue
            elif multiplication_uncommon:
                parser_result = multiplication_uncommon_parser(multiplication_uncommon.group(0))
                result.append({'operation_type': 'mult', 'content': {'variable': parser_result[0],
                                                                    'factor1': parser_result[1],
                                                                    'factor2': parser_result[2]}})
                continue

            decrease_common = re.search("^\s*[A-Za-z_]\w*\s*=\s*[A-Za-z_]?\w*\s*-\s*[A-Za-z_]?\w*\s*;$", code_line)
            decrease_uncommon = re.search("^\s*[A-Za-z_]\w*\s*-=\s*[A-Za-z_]?\w*\s*;$", code_line)
            if decrease_common:
                parser_result = decrease_common_parser(decrease_common.group(0))
                result.append({'operation_type': 'dec', 'content': {'variable': parser_result[0],
                                                                     'term1': parser_result[1],
                                                                     'term2': parser_result[2]}})
                continue
            elif decrease_uncommon:
                parser_result = decrease_uncommon_parser(decrease_uncommon.group(0))
                result.append({'operation_type': 'dec', 'content': {'variable': parser_result[0],
                                                                    'term1': parser_result[1],
                                                                    'term2': parser_result[2]}})
                continue

            division_common = re.search("^\s*[A-Za-z_]\w*\s*=\s*[A-Za-z_]?\w*\s*\/\s*[A-Za-z_]?\w*\s*;$", code_line)
            division_uncommon = re.search("^\s*[A-Za-z_]\w*\s*\/=\s*[A-Za-z_]\w*\s*;$", code_line)
            if division_common:
                parser_result = division_common_parser(division_common.group(0))
                result.append({'operation_type': 'div', 'content': {'variable': parser_result[0],
                                                                    'term1': parser_result[1],
                                                                    'term2': parser_result[2]}})
                continue
            elif division_uncommon:
                parser_result = division_uncommon_parser(division_uncommon.group(0))
                result.append({'operation_type': 'div', 'content': {'variable': parser_result[0],
                                                                    'term1': parser_result[1],
                                                                    'term2': parser_result[2]}})
                continue

            modulo_common = re.search("^\s*[A-Za-z_]\w*\s*=\s*[A-Za-z_]?\w*\s*\%\s*[A-Za-z_]?\w*\s*;$", code_line)
            modulo_uncommon = re.search("^\s*[A-Za-z_]\w*\s*%=\s*[A-Za-z_]\w*\s*;$", code_line)
            if modulo_common:
                parser_result = modulo_common_parser(modulo_common.group(0))
                result.append({'operation_type': 'mod', 'content': {'variable': parser_result[0],
                                                                    'term1': parser_result[1],
                                                                    'term2': parser_result[2]}})
                continue
            elif modulo_uncommon:
                parser_result = modulo_uncommon_parser(modulo_common.group(0))
                result.append({'operation_type': 'mod', 'content': {'variable': parser_result[0],
                                                                    'term1': parser_result[1],
                                                                    'term2': parser_result[2]}})
                continue
    translation_to_asm_code(result, data)


def translation_to_asm_code(translation_code: list, data: list):
    with open('asmr.asm', 'w') as asmr:
        asmr.write('SECTION .data\n')
        for d in data:
            if d['data_type'] == 'int':
                asmr.write(f'{d["variable"]}: dd {d["value"]}')
        asmr.write('\n\nSECTION .text\norg 0x100\n\n')
        for dic in translation_code:
            match dic['operation_type']:
                case 'ass':
                    if str(dic['content']['value']).isdigit():
                        asmr.write(f'mov dword [ds:{dic["content"]["variable"]}], {dic["content"]["value"]}\n')
                    else:
                        asmr.write(f'mov eax, dword [ds:{dic["content"]["value"]}]\n')
                        asmr.write(f'mov dword [ds:{dic["content"]["variable"]}], eax\n')
                case 'add':
                    if str(dic['content']['term2']).isdigit():
                        asmr.write(f'mov eax, dword [ds:{dic["content"]["term1"]}]\n')
                        asmr.write(f'mov ebx, {dic["content"]["term2"]}\n')
                        asmr.write(f'mov ecx, eax\n')
                        asmr.write(f'add ecx, ebx\n')
                        asmr.write(f'mov dword [ds:{dic["content"]["variable"]}], ecx\n')
                        asmr.write('\n')
                    else:
                        asmr.write(f'mov eax, dword [ds:{dic["content"]["term2"]}]\n')
                        asmr.write(f'mov ebx, eax\n')
                        asmr.write(f'mov eax, dword [ds:{dic["content"]["term1"]}]\n')
                        asmr.write(f'mov ecx, eax\n')
                        asmr.write(f'add ecx, ebx\n')
                        asmr.write(f'mov dword [ds:{dic["content"]["variable"]}], ecx\n')
                        asmr.write('\n')
                case 'mult':
                    if str(dic['content']['factor2']).isdigit():
                        asmr.write(f'mov eax, dword [ds: {dic["content"]["factor1"]}]\n')
                        asmr.write(f'mov ebx, {dic["content"]["factor2"]}\n')
                        asmr.write(f'imul ebx\n')
                        asmr.write(f'mov ecx, eax\n')
                        asmr.write(f'mov dword [ds:{dic["content"]["variable"]}], ecx\n')
                        asmr.write('\n')
                    else:
                        asmr.write(f'mov eax, dword [ds:{dic["content"]["factor2"]}]\n')
                        asmr.write(f'mov ebx, eax\n')
                        asmr.write(f'mov eax, dword [ds:{dic["content"]["factor1"]}]\n')
                        asmr.write(f'imul ebx\n')
                        asmr.write(f'mov ecx, eax\n')
                        asmr.write(f'mov dword [ds:{dic["content"]["variable"]}], ecx\n')
                        asmr.write('\n')
                case 'dec':
                    if str(dic['content']['term2']).isdigit():
                        asmr.write(f'mov eax, dword [ds:{dic["content"]["term1"]}]\n')
                        asmr.write(f'mov ebx, {dic["content"]["term2"]}\n')
                        asmr.write(f'mov ecx, eax\n')
                        asmr.write(f'sub ecx, ebx\n')
                        asmr.write(f'mov dword [ds:{dic["content"]["variable"]}], ecx\n')
                        asmr.write('\n')
                    else:
                        asmr.write(f'mov eax, dword [ds:{dic["content"]["term2"]}]\n')
                        asmr.write(f'mov ebx, eax\n')
                        asmr.write(f'mov eax, dword [ds:{dic["content"]["term1"]}]\n')
                        asmr.write(f'mov ecx, eax\n')
                        asmr.write(f'sub ecx, ebx\n')
                        asmr.write(f'mov dword [ds:{dic["content"]["variable"]}], ecx\n')
                        asmr.write('\n')
                case 'div':
                    if str(dic['content']['term2']).isdigit():
                        asmr.write(f'mov eax, dword [ds:{dic["content"]["term1"]}]\n')
                        asmr.write(f'mov ebx, {dic["content"]["term2"]}\n')
                        asmr.write(f'idiv ebx\n')
                        asmr.write(f'mov ecx, eax\n')
                        asmr.write(f'mov dword [ds: {dic["content"]["variable"]}], ecx\n')
                        asmr.write('\n')
                    else:
                        asmr.write(f'mov eax, dword [ds:{dic["content"]["term2"]}]\n')
                        asmr.write(f'mov ebx, eax\n')
                        asmr.write(f'mov eax, dword [ds:{dic["content"]["term1"]}]\n')
                        asmr.write(f'idiv ebx\n')
                        asmr.write(f'mov ecx, eax\n')
                        asmr.write(f'mov dword [ds:{dic["content"]["variable"]}], ecx\n')
                        asmr.write('\n')
                case 'mod':
                    if str(dic['content']['term2']).isdigit():
                        asmr.write(f'mov eax, dword [ds:{dic["content"]["term1"]}]\n')
                        asmr.write(f'mov ebx, {dic["content"]["term2"]}\n')
                        asmr.write(f'xor edx, edx\n')
                        asmr.write(f'idiv ebx\n')
                        asmr.write(f'mov ecx, edx\n')
                        asmr.write(f'mov dword [ds:{dic["content"]["variable"]}], ecx\n')
                        asmr.write('\n')
                    else:
                        asmr.write(f'mov eax, dword [ds:{dic["content"]["term2"]}]\n')
                        asmr.write(f'mov ebx, eax\n')
                        asmr.write(f'mov eax, dword [ds:{dic["content"]["term1"]}]\n')
                        asmr.write(f'xor edx, edx\n')
                        asmr.write(f'idiv ebx\n')
                        asmr.write(f'mov ecx, edx\n')
                        asmr.write(f'mov dword [ds:{dic["content"]["variable"]}], ecx\n')
                        asmr.write('\n')


if __name__ == '__main__':
    main()
