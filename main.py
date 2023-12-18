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

def function_start_parser(row: str):
    a = [s for s in re.split('[{|\s*]', row)]
    if a[1][-1] == ')':
        b = a.pop(1)
        a.insert(1, b[:-2])
        a.insert(2, '()')
    # print(a)
    return a

def procedure_call_parser(row: str):
    a = [s for s in re.split('[;|()|\s+]+', row)]
    a.append('proc')
    return a

def function_call_parser(row: str):
    a = [s for s in re.split('[=|;|()|\s+]+', row)]
    a.append('func')
    return a

def return_call_parser(row: str):
    a = [s for s in re.split('[;|\s+]+', row)]
    return a

def main():
    file_path = './test.txt'
    with open(file_path, 'r') as f:
        code = [line.strip() for line in f]
        result = []
        data = []
        offset = 0
        for code_line in code:
            function_start = re.search("^[A-Za-z]\w*\s+[A-Za-z]\w*\(\)\s*\{\s*$", code_line)
            if function_start:
                parser_result = function_start_parser(function_start.group())
                offset, function_data, function_result = parse_function_code(code, offset)
                data.append({'function_name': parser_result[1], 'data': function_data})
                result.append({'function_name': parser_result[1], 'result': function_result})
                # print(parser_result)
                # print(f'{data} \n {result}')

    translation_to_asm_code(result, data)


def parse_function_code(funtion_code: list, offset: int):
    func_data = []
    func_result = []
    for i, line in enumerate(funtion_code):
        if i <= offset:
            continue
        initialization = re.search("^\s*int\s[A-Za-z_]\w*\s*=\s*\d+\s*;$", line)
        if initialization:
            parser_result = initialization_parser(initialization.group(0))
            func_data.append({'data_type': parser_result[0], 'variable': parser_result[1], 'value': parser_result[2]})
            continue

        assignment = re.search("^\s*(?!int$)[A-Za-z_]\w*\s*=\s*\w+\s*;$", line)
        if assignment:
            parser_result = assignment_parser(assignment.group(0))
            func_result.append({'operation_type': 'ass', 'content': {'variable': parser_result[0],
                                                                'value': parser_result[1]}})
            continue

        addition_common = re.search("^\s*[A-Za-z_]\w*\s*=\s*\w+\s\+?\s\w*\s*;$", line)
        addition_uncommon = re.search("^\s*[A-Za-z_]\w*\s\+*=\s*\w+\s*;$", line)
        if addition_common:
            parser_result = addition_common_parser(addition_common.group(0))
            func_result.append({'operation_type': 'add', 'content': {'variable': parser_result[0],
                                                                'term1': parser_result[1],
                                                                'term2': parser_result[2]}})
            continue
        elif addition_uncommon:
            parser_result = addition_uncommon_parser(addition_uncommon.group(0))
            func_result.append({'operation_type': 'add', 'content': {'variable': parser_result[0],
                                                                'term1': parser_result[1],
                                                                'term2': parser_result[2]}})
            continue

        multiplication_common = re.search("^\s*[A-Za-z_]\w*\s*=\s*[A-Za-z_]?\w*\s*\*\s*[A-Za-z_]?\w*\s*;$", line)
        multiplication_uncommon = re.search("^\s*[A-Za-z_]\w*\s*\*=\s*[A-Za-z_]?\w*\s*;$", line)
        if multiplication_common:
            parser_result = multiplication_common_parser(multiplication_common.group(0))
            func_result.append({'operation_type': 'mult', 'content': {'variable': parser_result[0],
                                                                 'term1': parser_result[1],
                                                                 'term2': parser_result[2]}})
            continue
        elif multiplication_uncommon:
            parser_result = multiplication_uncommon_parser(multiplication_uncommon.group(0))
            func_result.append({'operation_type': 'mult', 'content': {'variable': parser_result[0],
                                                                 'term1': parser_result[1],
                                                                 'term2': parser_result[2]}})
            continue

        decrease_common = re.search("^\s*[A-Za-z_]\w*\s*=\s*[A-Za-z_]?\w*\s*-\s*[A-Za-z_]?\w*\s*;$", line)
        decrease_uncommon = re.search("^\s*[A-Za-z_]\w*\s*-=\s*[A-Za-z_]?\w*\s*;$", line)
        if decrease_common:
            parser_result = decrease_common_parser(decrease_common.group(0))
            func_result.append({'operation_type': 'dec', 'content': {'variable': parser_result[0],
                                                                'term1': parser_result[1],
                                                                'term2': parser_result[2]}})
            continue
        elif decrease_uncommon:
            parser_result = decrease_uncommon_parser(decrease_uncommon.group(0))
            func_result.append({'operation_type': 'dec', 'content': {'variable': parser_result[0],
                                                                'term1': parser_result[1],
                                                                'term2': parser_result[2]}})
            continue

        division_common = re.search("^\s*[A-Za-z_]\w*\s*=\s*[A-Za-z_]?\w*\s*\/\s*[A-Za-z_]?\w*\s*;$", line)
        division_uncommon = re.search("^\s*[A-Za-z_]\w*\s*\/=\s*[A-Za-z_]\w*\s*;$", line)
        if division_common:
            parser_result = division_common_parser(division_common.group(0))
            func_result.append({'operation_type': 'div', 'content': {'variable': parser_result[0],
                                                                'term1': parser_result[1],
                                                                'term2': parser_result[2]}})
            continue
        elif division_uncommon:
            parser_result = division_uncommon_parser(division_uncommon.group(0))
            func_result.append({'operation_type': 'div', 'content': {'variable': parser_result[0],
                                                                'term1': parser_result[1],
                                                                'term2': parser_result[2]}})
            continue

        modulo_common = re.search("^\s*[A-Za-z_]\w*\s*=\s*[A-Za-z_]?\w*\s*\%\s*[A-Za-z_]?\w*\s*;$", line)
        modulo_uncommon = re.search("^\s*[A-Za-z_]\w*\s*%=\s*[A-Za-z_]\w*\s*;$", line)
        if modulo_common:
            parser_result = modulo_common_parser(modulo_common.group(0))
            func_result.append({'operation_type': 'mod', 'content': {'variable': parser_result[0],
                                                                'term1': parser_result[1],
                                                                'term2': parser_result[2]}})
            continue
        elif modulo_uncommon:
            parser_result = modulo_uncommon_parser(modulo_common.group(0))
            func_result.append({'operation_type': 'mod', 'content': {'variable': parser_result[0],
                                                                'term1': parser_result[1],
                                                                'term2': parser_result[2]}})
            continue

        procedure_call = re.search("^\s*[A-Za-z_]+\w*\(\)\s*\;\s*$", line)
        function_call = re.search("^\s*[A-Za-z_]+\w*\s*\=\s*[A-Za-z_]+\w*\(\)\s*\;\s*$", line)
        if procedure_call:
            parser_result = procedure_call_parser(procedure_call.group(0))
            func_result.append({'operation_type': 'proc', 'content': {'variable': parser_result[0]}})
            continue
        elif function_call:
            parser_result = function_call_parser(function_call.group(0))
            func_result.append({'operation_type': 'func', 'content': {'variable': parser_result[0],
                                                                'term1': parser_result[1],
                                                                'term2': ''}})
            continue

        return_call = re.search("^\s*return\s+[A-Za-z_]+\w*\s*\;\s*$", line)
        if return_call:
            parser_result = return_call_parser(return_call.group(0))
            func_result.append({'operation_type': 'ret', 'content': {'variable': parser_result[1]}})
            continue

        function_end = re.search("^\s*\}\s*$", line)
        if function_end:
            func_result.append({'operation_type': 'end', 'content': {'variable': ''}})
            # print(result)
            return i, func_data, func_result

def translation_main_body(translation_code: list, data: list):
    with open('asmr.asm', 'w') as asmr:
        asmr.write('SECTION .data\n')
        for d in data:
            if d['data_type'] == 'int':
                asmr.write(f'\t{d["variable"]}: dd {d["value"]}')
        asmr.write('\n\tint 20h \n\nSECTION .text\n\torg 0x100\n\n')
        asmr.write('global _start:\n_start:\n')
        for dic in translation_code:
            match dic['operation_type']:
                case 'ass':
                    if str(dic['content']['value']).isdigit():
                        asmr.write(f'\tmov dword [ds:{dic["content"]["variable"]}], {dic["content"]["value"]}\n')
                    else:
                        asmr.write(f'\tmov eax, dword [ds:{dic["content"]["value"]}]\n')
                        asmr.write(f'\tmov dword [ds:{dic["content"]["variable"]}], eax\n')
                case 'add':
                    if str(dic['content']['term2']).isdigit():
                        asmr.write(f'\tmov eax, dword [ds:{dic["content"]["term1"]}]\n')
                        asmr.write(f'\tmov ebx, {dic["content"]["term2"]}\n')
                        asmr.write(f'\tmov ecx, eax\n')
                        asmr.write(f'\tadd ecx, ebx\n')
                        asmr.write(f'\tmov dword [ds:{dic["content"]["variable"]}], ecx\n')
                        asmr.write('\n')
                    else:
                        asmr.write(f'\tmov eax, dword [ds:{dic["content"]["term2"]}]\n')
                        asmr.write(f'\tmov ebx, eax\n')
                        asmr.write(f'\tmov eax, dword [ds:{dic["content"]["term1"]}]\n')
                        asmr.write(f'\tmov ecx, eax\n')
                        asmr.write(f'\tadd ecx, ebx\n')
                        asmr.write(f'\tmov dword [ds:{dic["content"]["variable"]}], ecx\n')
                        asmr.write('\n')
                case 'mult':
                    if str(dic['content']['term2']).isdigit():
                        asmr.write(f'\tmov eax, dword [ds: {dic["content"]["term1"]}]\n')
                        asmr.write(f'\tmov ebx, {dic["content"]["term2"]}\n')
                        asmr.write(f'\timul ebx\n')
                        asmr.write(f'\tmov ecx, eax\n')
                        asmr.write(f'\tmov dword [ds:{dic["content"]["variable"]}], ecx\n')
                        asmr.write('\n')
                    else:
                        asmr.write(f'\tmov eax, dword [ds:{dic["content"]["term2"]}]\n')
                        asmr.write(f'\tmov ebx, eax\n')
                        asmr.write(f'\tmov eax, dword [ds:{dic["content"]["term1"]}]\n')
                        asmr.write(f'\timul ebx\n')
                        asmr.write(f'\tmov ecx, eax\n')
                        asmr.write(f'\tmov dword [ds:{dic["content"]["variable"]}], ecx\n')
                        asmr.write('\n')
                case 'dec':
                    if str(dic['content']['term2']).isdigit():
                        asmr.write(f'\tmov eax, dword [ds:{dic["content"]["term1"]}]\n')
                        asmr.write(f'\tmov ebx, {dic["content"]["term2"]}\n')
                        asmr.write(f'\tmov ecx, eax\n')
                        asmr.write(f'\tsub ecx, ebx\n')
                        asmr.write(f'\tmov dword [ds:{dic["content"]["variable"]}], ecx\n')
                        asmr.write('\n')
                    else:
                        asmr.write(f'\tmov eax, dword [ds:{dic["content"]["term2"]}]\n')
                        asmr.write(f'\tmov ebx, eax\n')
                        asmr.write(f'\tmov eax, dword [ds:{dic["content"]["term1"]}]\n')
                        asmr.write(f'\tmov ecx, eax\n')
                        asmr.write(f'\tsub ecx, ebx\n')
                        asmr.write(f'\tmov dword [ds:{dic["content"]["variable"]}], ecx\n')
                        asmr.write('\n')
                case 'div':
                    if str(dic['content']['term2']).isdigit():
                        asmr.write(f'\tmov eax, dword [ds:{dic["content"]["term1"]}]\n')
                        asmr.write(f'\tmov ebx, {dic["content"]["term2"]}\n')
                        asmr.write(f'\tidiv ebx\n')
                        asmr.write(f'\tmov ecx, eax\n')
                        asmr.write(f'\tmov dword [ds: {dic["content"]["variable"]}], ecx\n')
                        asmr.write('\n')
                    else:
                        asmr.write(f'\tmov eax, dword [ds:{dic["content"]["term2"]}]\n')
                        asmr.write(f'\tmov ebx, eax\n')
                        asmr.write(f'\tmov eax, dword [ds:{dic["content"]["term1"]}]\n')
                        asmr.write(f'\tidiv ebx\n')
                        asmr.write(f'\tmov ecx, eax\n')
                        asmr.write(f'\tmov dword [ds:{dic["content"]["variable"]}], ecx\n')
                        asmr.write('\n')
                case 'mod':
                    if str(dic['content']['term2']).isdigit():
                        asmr.write(f'\tmov eax, dword [ds:{dic["content"]["term1"]}]\n')
                        asmr.write(f'\tmov ebx, {dic["content"]["term2"]}\n')
                        asmr.write(f'\txor edx, edx\n')
                        asmr.write(f'\tidiv ebx\n')
                        asmr.write(f'\tmov ecx, edx\n')
                        asmr.write(f'\tmov dword [ds:{dic["content"]["variable"]}], ecx\n')
                        asmr.write('\n')
                    else:
                        asmr.write(f'\tmov eax, dword [ds:{dic["content"]["term2"]}]\n')
                        asmr.write(f'\tmov ebx, eax\n')
                        asmr.write(f'\tmov eax, dword [ds:{dic["content"]["term1"]}]\n')
                        asmr.write(f'\txor edx, edx\n')
                        asmr.write(f'\tidiv ebx\n')
                        asmr.write(f'\tmov ecx, edx\n')
                        asmr.write(f'\tmov dword [ds:{dic["content"]["variable"]}], ecx\n')
                        asmr.write('\n')
                case 'proc':
                    asmr.write(f'\tcall {dic["content"]["variable"]}\n')
                    asmr.write('\n')
                case 'func':
                    asmr.write(f'\tcall {dic["content"]["term1"]}\n')
                    asmr.write(f'\tmov dword [ds:{dic["content"]["variable"]}], ecx\n')
                    asmr.write('\n')
                case 'end':
                    asmr.write(f'\tint 20h\n')
                    asmr.write('\n')

def translation_function(translation_code: list, data: list, function_name:str, function_number: int):
    local_variables = []
    with open('asmr.asm', 'a') as asmr:
        asmr.write(f'{function_name}:\n')
        asmr.write('\t%push mycontext\n')
        asmr.write('\t%stacksize large\n')
        asmr.write('\t%assign %$localsize 0\n')
        asmr.write('\t%local ')
        for d in data:
            if d['data_type'] == 'int' and d != data[-1]:
                asmr.write(f'{function_name}_{d["variable"]}:word, ')
                local_variables.append(f'{function_name}_{d["variable"]}')
            else:
                asmr.write(f'{function_name}_{d["variable"]}:word')
                local_variables.append(f'{function_name}_{d["variable"]}')

        asmr.write('\n\n')
        asmr.write(f'\tenter %$localsize, {function_number}\n')
        for d in data:
            if d['data_type'] == 'int':
                asmr.write(f'\tmov dword [ds:{function_name}_{d["variable"]}], {d["value"]}\n')
        asmr.write('\n')
        for dic in translation_code:
            variable = ''
            term1 = ''
            term2 = ''
            if 'variable' in dic['content'].keys():
                if f'{function_name}_{dic["content"]["variable"]}' in local_variables:
                    variable = f'{function_name}_{dic["content"]["variable"]}'
                else:
                    variable = f'{dic["content"]["variable"]}'
            if 'term1' in dic['content'].keys():
                if f'{function_name}_{dic["content"]["term1"]}' in local_variables:
                    term1 = f'{function_name}_{dic["content"]["term1"]}'
                else:
                    term1 = f'{dic["content"]["term1"]}'
                if f'{function_name}_{dic["content"]["term2"]}' in local_variables:
                    term2 = f'{function_name}_{dic["content"]["term2"]}'
                else:
                    term2 = f'{dic["content"]["term2"]}'
            match dic['operation_type']:
                case 'ass':
                    if str(dic['content']['value']).isdigit():
                        asmr.write(f'\tmov dword [ds:{variable}], {dic["content"]["value"]}\n')
                    else:
                        asmr.write(f'\tmov eax, dword [ds:{function_name}_{dic["content"]["value"]}]\n')
                        asmr.write(f'\tmov dword [ds:{variable}], eax\n')
                case 'add':
                    if str(dic['content']['term2']).isdigit():
                        asmr.write(f'\tmov eax, dword [ds:{term1}]\n')
                        asmr.write(f'\tmov ebx, {dic["content"]["term2"]}\n')
                        asmr.write(f'\tmov ecx, eax\n')
                        asmr.write(f'\tadd ecx, ebx\n')
                        asmr.write(f'\tmov dword [ds:{variable}], ecx\n')
                        asmr.write('\n')
                    else:
                        asmr.write(f'\tmov eax, dword [ds:{term2}]\n')
                        asmr.write(f'\tmov ebx, eax\n')
                        asmr.write(f'\tmov eax, dword [ds:{term1}]\n')
                        asmr.write(f'\tmov ecx, eax\n')
                        asmr.write(f'\tadd ecx, ebx\n')
                        asmr.write(f'\tmov dword [ds:{variable}], ecx\n')
                        asmr.write('\n')
                case 'mult':
                    if str(dic['content']['term2']).isdigit():
                        asmr.write(f'\tmov eax, dword [ds:{term1}]\n')
                        asmr.write(f'\tmov ebx, {dic["content"]["term2"]}\n')
                        asmr.write(f'\timul ebx\n')
                        asmr.write(f'\tmov ecx, eax\n')
                        asmr.write(f'\tmov dword [ds:{variable}], ecx\n')
                        asmr.write('\n')
                    else:
                        asmr.write(f'\tmov eax, dword [ds:{term2}]\n')
                        asmr.write(f'\tmov ebx, eax\n')
                        asmr.write(f'\tmov eax, dword [ds:{term1}]\n')
                        asmr.write(f'\timul ebx\n')
                        asmr.write(f'\tmov ecx, eax\n')
                        asmr.write(f'\tmov dword [ds:{variable}], ecx\n')
                        asmr.write('\n')
                case 'dec':
                    if str(dic['content']['term2']).isdigit():
                        asmr.write(f'\tmov eax, dword [ds:{term1}]\n')
                        asmr.write(f'\tmov ebx, {dic["content"]["term2"]}\n')
                        asmr.write(f'\tmov ecx, eax\n')
                        asmr.write(f'\tsub ecx, ebx\n')
                        asmr.write(f'\tmov dword [ds:{variable}], ecx\n')
                        asmr.write('\n')
                    else:
                        asmr.write(f'\tmov eax, dword [ds:{term2}]\n')
                        asmr.write(f'\tmov ebx, eax\n')
                        asmr.write(f'\tmov eax, dword [ds:{term1}]\n')
                        asmr.write(f'\tmov ecx, eax\n')
                        asmr.write(f'\tsub ecx, ebx\n')
                        asmr.write(f'\tmov dword [ds:{variable}], ecx\n')
                        asmr.write('\n')
                case 'div':
                    if str(dic['content']['term2']).isdigit():
                        asmr.write(f'\tmov eax, dword [ds:{term1}]\n')
                        asmr.write(f'\tmov ebx, {dic["content"]["term2"]}\n')
                        asmr.write(f'\tidiv ebx\n')
                        asmr.write(f'\tmov ecx, eax\n')
                        asmr.write(f'\tmov dword [ds:{variable}], ecx\n')
                        asmr.write('\n')
                    else:
                        asmr.write(f'\tmov eax, dword [ds:{term2}]\n')
                        asmr.write(f'\tmov ebx, eax\n')
                        asmr.write(f'\tmov eax, dword [ds:{term1}]\n')
                        asmr.write(f'\tidiv ebx\n')
                        asmr.write(f'\tmov ecx, eax\n')
                        asmr.write(f'\tmov dword [ds:{variable}], ecx\n')
                        asmr.write('\n')
                case 'mod':
                    if str(dic['content']['term2']).isdigit():
                        asmr.write(f'\tmov eax, dword [ds:{term1}]\n')
                        asmr.write(f'\tmov ebx, {dic["content"]["term2"]}\n')
                        asmr.write(f'\txor edx, edx\n')
                        asmr.write(f'\tidiv ebx\n')
                        asmr.write(f'\tmov ecx, edx\n')
                        asmr.write(f'\tmov dword [ds:{variable}], ecx\n')
                        asmr.write('\n')
                    else:
                        asmr.write(f'\tmov eax, dword [ds:{term2}]\n')
                        asmr.write(f'\tmov ebx, eax\n')
                        asmr.write(f'\tmov eax, dword [ds:{term1}]\n')
                        asmr.write(f'\txor edx, edx\n')
                        asmr.write(f'\tidiv ebx\n')
                        asmr.write(f'\tmov ecx, edx\n')
                        asmr.write(f'\tmov dword [ds:{variable}], ecx\n')
                        asmr.write('\n')
                case 'ret':
                    asmr.write(f'\tmov ecx, [ds:{variable}]\n')
                    asmr.write('\n')
                case 'end':
                    asmr.write(f'\tleave\n')
                    asmr.write(f'\tret\n')
                    asmr.write('\n')
                    asmr.write('\t%pop\n\n')

def translation_to_asm_code(translation_code: list, data: list):
    function_number = 0
    for i, code in enumerate(translation_code):
        if code['function_name'] == 'main':
            translation_main_body(code['result'], data[i]['data'])
            break
    for i, code in enumerate(translation_code):
        if code['function_name'] != 'main':
            translation_function(code['result'], data[i]['data'], code['function_name'], function_number)
            function_number += 1
        else:
            continue


if __name__ == '__main__':
    main()

# Maksim
# ochen`
# nam
# pomog
