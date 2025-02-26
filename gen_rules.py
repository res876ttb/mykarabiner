#!/usr/bin/env python3

import argparse
import yaml
import sys
import json
import os

args = None
rules = None
macros = None

def parseArgs():
  global args
  parser = argparse.ArgumentParser()
  parser.add_argument('rule_file', help='Path to the rule YAML file')
  parser.add_argument('-o', '--output_name', help='Name to the output file name. If not set, will be the same as the rule_file', default='')
  args = parser.parse_args()

def parseRules():
  global rules
  with open(args.rule_file) as fp:
    try:
      rules = yaml.safe_load(fp)
    except yaml.YAMLError as exc:
      print(exc)
      print('Aborted.')
      sys.exit(1)

def getTitle():
  if 'title' not in rules:
    print('`title` is not set')
    sys.exit(1)
  return rules['title']

def getMacros():
  if 'macros' in rules:
    return rules['macros']
  return {}

def parseOptions(options):
  options = options.strip()
  if options == '':
    return {}

  new_rule = {}
  splitted_options = options.split(',')
  for option in splitted_options:
    if option in macros:
      for key, value in macros[option].items():
        new_rule[key] = value
    else:
      print('Unknown option:', option)
      sys.exit(1)
  return new_rule

def parseFrom(rule_from):
  rule = {}
  rule_from = rule_from.strip().split(',')
  rule['key_code'] = rule_from[0]

  if len(rule_from) == 1:
    return rule

  modifiers = {}
  for modifier in rule_from[1:]:
    if modifier == 'any':
      modifiers['optional'] = ['any']
    else:
      if 'mandatory' not in modifiers:
        modifiers['mandatory'] = []
      modifiers['mandatory'].append(modifier)

  rule['modifiers'] = modifiers
  return rule

def parseToGroup(to_rule):
  rule = {}
  to_rule = to_rule.strip().split(',')

  rule['key_code'] = to_rule[0]

  if len(to_rule) > 1:
    for modifier in to_rule[1:]:
      modifier = modifier.strip()
      if modifier == 'lazy':
        rule['lazy'] = True
      else:
        if 'modifiers' not in rule:
          rule['modifiers'] = []
        rule['modifiers'].append(modifier)

  return rule

def parseTo(rule_to):
  return [parseToGroup(to_group) for to_group in rule_to.split('|')]

def genRuleItem(rule_item):
  splitted_rule = rule_item.split('/')
  rule_from = splitted_rule[0]
  rule_to   = splitted_rule[1].strip()
  options   = splitted_rule[2] if len(splitted_rule) == 3 else ''

  new_rule = parseOptions(options)
  if rule_from != '':
    new_rule['from'] = parseFrom(rule_from)
  if rule_to != '':
    new_rule['to'] = parseTo(rule_to)
  new_rule['type'] = 'basic'
  return new_rule

def genRuleGroup(desc, rule_group_items):
  manipulators = []
  for rule_item in rule_group_items:
    manipulators.append(genRuleItem(rule_item))
  return {
    'description': desc,
    'manipulators': manipulators
  }

def genRules():
  global macros

  if 'rules' not in rules:
    print('`rules` is not set')
    sys.exit(1)

  title = getTitle()
  macros = getMacros()
  new_rule = {
    'title': title,
    'rules': []
  }

  for desc, rule_group in rules['rules'].items():
    new_rule['rules'].append(genRuleGroup(desc, rule_group))

  return new_rule

def writeRules(rules):
  out_name = args.output_name if args.output_name != '' else os.path.basename(args.rule_file.replace('yml', 'json'))
  with open(out_name, 'w') as fp:
    json.dump(rules, fp, indent=4)

def main():
  parseArgs()
  parseRules()
  rules = genRules()
  writeRules(rules)

if __name__ == '__main__':
  main()