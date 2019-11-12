#!/bin/bash

#searchTerms = ()

#while [[ $# -gt 0 ]] ; do
#  case "$1" in
#    --genSearch)
#      shift
#
#      echo "genSearch"
#      ;;
#    --directory)
#      echo "directory"
#      ;;
#    --authors)
#      echo "authors"
#      ;;
#    --datasetType)
#      echo "datasetType"
#      ;;
#    --searchDesc)
#      echo "searchDesc"
#      ;;
#    --numOfProbes)
#      echo "searchDesc"
#      ;;
#    --numOfSamps)
#      echo "numOfSamps"
#      ;;
#    --org)
#      echo "org"
#      ;;
#    --accessionID)
#      echo "accessionID"
#      ;;
#    --MeSH)
#      echo "MeSH"
#      ;;
#    --platformTech)
#      echo "platformTech"
#      ;;
#    --project)
#      echo "project"
#      ;;
#    --pubDate)
#      echo "pubDate"
#      ;;
#    --relSeries)
#      echo "relSeries"
#      ;;
#    --relPlat)
#      echo "relPlat"
#      ;;
#    --reporterID)
#      echo "reporterID"
#      ;;
#    --sampleSrc)
#      echo "sampleSrc"
#      ;;
#    --sampleType)
#      echo "sampleType"
#      ;;
#    --sampleValType)
#      echo "sampleValType"
#      ;;
#    --subInst)
#      echo "subInst"
#      ;;
#    --subsetDesc)
#      echo "subsetDesc"
#      ;;
#    --subsetVarType)
#      echo "subsetVartype"
#      ;;
#    --suppFiles)
#      echo "suppFiles"
#      ;;
#    --tagLen)
#      echo "tagLen"
#      ;;
#    --title)
#      echo "title"
#      ;;
#    --updateDate)
#      echo "updateDate"
#      ;;
#    *)
#      break
#      ;;
#  esac
#done

#echo "step 1 done"

#terms=()
#for search in "${searchTerms[@]}" ; do
#  echo $search
#  terms+=( $search )
#done
#
#if [ -n "${SEARCHDESC}" ]
#then
#  echo $SEARCHDESC
#fi
#if [[ -n "${}"]]; then
#
#if [[ -n "${}"]]; then
#
#if [[ -n "${}"]]; then
#
#if [[ -n "${}"]]; then
#
#if [[ -n "${}"]]; then
#
#if [[ -n "${}"]]; then

echo "--------------"
#echo ${terms[1]}
echo "done"
#echo "$@"

python /root/Program/search_geo.py "$@"