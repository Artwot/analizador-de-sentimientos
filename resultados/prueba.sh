#!/bin/bash

t=$(wc -l palabras_etiquetadas_100)

for i in {1..100}
do
    head -$i palabras_etiquetadas_100 | wc -L 
done 