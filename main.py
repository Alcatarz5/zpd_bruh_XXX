import os
import re


def initialization_parser(row: str):
    a = [s for s in re.split('[=|;|\s+]+', row)]
    print(a)
    return a


def assignment_parser(row: str):
    a = [s for s in re.split('[=|;|\s+]+', row)]
    print(a)


def addition_common_parser(row: str):
    a = [s for s in re.split('[=|;|+|\s+]+', row)]
    print(a)


def addition_uncommon_parser(row: str):
    a = [s for s in re.split('[=|;|+|\s+]+', row)]
    print(a)


def main():
    file_path = '/home/bendamvn/zpd_bruh_XXX/test.txt'
    with open(file_path, 'r') as f:
        code = [line.strip() for line in f]
        result = []
        for code_line in code:
            initialization = re.search("^\s*int\s[A-Za-z_]\w*\s*=\s*\d+\s*;$", code_line)
            if initialization:
                parser_result = initialization_parser(initialization.group(0))
                result.append({'operation_type': 'init', 'content': {'data_type': parser_result[0],
                                                                     'variable': parser_result[1],
                                                                     'value': parser_result[2]}})
                continue

            assignment = re.search("^\s*(?!int$)[A-Za-z_]\w*\s*=\s*\d+\s*;$", code_line)
            if assignment:
                assignment_parser(assignment.group(0))
                result.append({'operation_type': 'ass', 'content': {'variable': parser_result[0],
                                                                    'value': parser_result[1]}})
                continue

            addition_common = re.search("^\s*[A-Za-z_]\w*\s*=\s*\w+\s\+?\s\w*\s*;$", code_line)
            addition_uncommon = re.search("^\s*[A-Za-z_]\w*\s\+*=\s*\w+\s*;$", code_line)
            if addition_common:
                addition_common_parser(addition_common.group(0))
                # result.append({'operation_type': 'add', 'content': addition_common.group(0)})
                continue
            elif addition_uncommon:
                addition_uncommon_parser(addition_uncommon.group(0))
                # result.append({'operation_type': 'add', 'content': addition_uncommon.group(0)})
                continue

            multiplication_common = re.search("^\s*[A-Za-z_]\w+\s*=\s*[A-Za-z_]\w+\s*\*\s*[A-Za-z_]\w+\s*;$", code_line)
            multiplication_uncommon = re.search("^\s*[A-Za-z_]\w+\s*\*=\s*[A-Za-z_]\w+\s*;$", code_line)
            if multiplication_common:
                # result.append({'operation_type': 'mult', 'content': multiplication_common.group(0)})
                continue
            elif multiplication_uncommon:
                # result.append({'operation_type': 'mult', 'content': multiplication_uncommon.group(0)})
                continue

            decrease_common = re.search("^\s*[A-Za-z_]\w+\s*=\s*[A-Za-z_]\w+\s*-\s*[A-Za-z_]\w+\s*;$", code_line)
            decrease_uncommon = re.search("^\s*[A-Za-z_]\w+\s*-=\s*[A-Za-z_]\w+\s*;$", code_line)
            if decrease_common:
                # result.append({'operation_type': 'dec', 'content': decrease_common.group(0)})
                continue
            elif decrease_uncommon:
                # result.append({'operation_type': 'dec', 'content': decrease_uncommon.group(0)})
                continue

            division_common = re.search("^\s*[A-Za-z_]\w*\s*=\s*[A-Za-z_]\w*\s*\/\s*[A-Za-z_]\w*\s*;$", code_line)
            division_uncommon = re.search("^\s*[A-Za-z_]\w*\s*\/=\s*[A-Za-z_]\w*\s*;$", code_line)
            if division_common:
                # result.append({'operation_type': 'div', 'content': division_common.group(0)})
                continue
            elif division_uncommon:
                # result.append({'operation_type': 'div', 'content': division_uncommon.group(0)})
                continue

            modulo_common = re.search("^\s*[A-Za-z_]\w*\s*=\s*[A-Za-z_]\w*\s*\%\s*[A-Za-z_]\w*\s*;$", code_line)
            modulo_uncommon = re.search("^\s*[A-Za-z_]\w*\s*%=\s*[A-Za-z_]\w*\s*;$", code_line)
            if modulo_common:
                # result.append({'operation_type': 'mod', 'content': modulo_common.group(0)})
                continue
            elif modulo_uncommon:
                # result.append({'operation_type': 'mod', 'content': modulo_uncommon.group(0)})
                continue


def translation_to_asm_code(translation_code):
    with open('asmr.asm', 'w') as asmr:
        asmr.write()
        for dic in translation_code:
            match dic['operation_type']:
                case 'init':
                    pass
                case 'ass':
                    asmr.write(f'mov dword [ds: {dic["content"]["varibale"]}], ')

#             # {команда} {регистр}, {значение}




if __name__ == '__main__':
    # a = 5
    # if a > 1:
    #     print('a>1')
    # if a > 3:
    #     print('a>3')
    main()


# /home/bendamvn/zpd_bruh_XXX/test.txt