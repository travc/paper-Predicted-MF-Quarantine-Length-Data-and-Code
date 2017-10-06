#!/bin/sh

MAILTO='FILL-IN-YOUR-EMAIL-ADDRESS'

# Provide runset diectory as first argument
RUNSET=${1%/}  # first argument sans trailing slash (if there is one)
RUNSET_LABEL="${RUNSET/\// }"
echo $RUNSET

cmd="cd $RUNSET; qsub -N \"MedFoesP-long $RUNSET_LABEL\" \"$PWD/$RUNSET/mfp_longrun_array.sge\""

# make sure the RUNSET argument was actually passed
if [ "$#" -ne 1 ] || ! [ -d "$1" ]; then
  echo "Usage: $0 RUNSET" >&2
  exit 1
fi

START_DATE=`date -Ins`
echo "######## STARTED ########"
echo "## $START_DATE "

sh -c "$cmd"
rval=$?

END_DATE=`date -Ins`
echo '######## FISNISHED ########'
echo "## $END_DATE "
echo $cmd
echo '###########################'
echo "Job Finished:
####
# $cmd
####
rval  : $rval
start : $START_DATE
end   : $END_DATE" | \
mail -s "Job Finsihed: $cmd" $MAILTO

