#!/bin/bash

for i in $(ls rules/*.yml); do cmd="./gen_rules.py $i"; echo $cmd; $cmd; done