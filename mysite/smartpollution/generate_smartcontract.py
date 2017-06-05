import os


def create_new_smart_contract1(template_name='PollutionTracker', metric_name='DefaultMetricName', lower_trigger=-6666,
                               upper_trigger=6666):
    with open(os.path.join(os.getcwd(), template_name + '.sol'), 'w', encoding='utf-8') as out_file, open(
            os.path.join(os.getcwd(), 'smartpollution', 'static', 'smartcontracts', 'template_smartcontract.sol'), 'r',
            encoding='utf-8') as template_f:
        for lin in template_f:
            if not "@" in lin:
                out_file.write(lin)
            else:
                if "@ContractName@" in lin:
                    out_file.write(lin.replace('@ContractName@', str(template_name).replace('-', '')))
                if "@MetricName@" in lin:
                    out_file.write(lin.replace('@MetricName@', str(r'"' + metric_name + r'"').replace('-', '')))
                if "@LowerTrigger@" in lin:
                    out_file.write(lin.replace('@LowerTrigger@', str(int(lower_trigger))))
                if "@UpperTrigger@" in lin:
                    out_file.write(lin.replace('@UpperTrigger@', str(int(upper_trigger))))
    return os.path.join(os.getcwd(), template_name + '.sol')


def create_new_smart_contract(template_name='PollutionTracker', metrics=[]):
    with open(os.path.join(os.getcwd(), template_name + '.sol'), 'w', encoding='utf-8') as out_file, open(
            os.path.join(os.getcwd(), 'smartpollution', 'static', 'smartcontracts',
                         'simple_template_smartcontract.sol'), 'r', encoding='utf-8') as template_f:
        for lin in template_f:
            if not "@" in lin:
                out_file.write(lin)
            else:
                if "@contractName@" in lin:
                    out_file.write(lin.replace('@contractName@', str(template_name).replace('-', '')))
                if "@singleEvents@" in lin:
                    for met in metrics:
                        out_file.write('\t\tevent ' + str(met) + '(' + 'int16 _val' + str(met) + ',' + 'string _id);\n')
                if "@singleUpdate@" in lin:
                    for met in metrics:
                        out_file.write('\t\tfunction alarm' + str(met) + '(' + 'int16 _val' + str(
                            met) + ',' + 'string _id) onlyOwner{' + str(met) + '(' + '_val' + str(
                            met) + ', ' + '_id);}\n')
                if "@paramsAlarmAll@" in lin:
                    out_file.write('\t\t\t')
                    for met in metrics:
                        out_file.write(' int16 _val' + str(met) + ',')
                    out_file.write(' string _id\n')

                if "@paramsUpdateAll@" in lin:
                    for met in metrics:
                        out_file.write('\t\t\t\tint16 _val' + str(met) + ',')
                    out_file.write(' string _id\n')
                if "@codeUpdateAll@" in lin:
                    out_file.write('\t\t\t\tAlarmAll(')
                    for met in metrics:
                        out_file.write(' _val' + str(met) + ',')
                    out_file.write(' _id);\n')

    return os.path.join(os.getcwd(), template_name + '.sol')
