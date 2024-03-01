echo "==================== PYJQ MIGRATOR START ==================="

input_args=$@
echo "input_args: '${input_args}'"

CUR_DIR=${PWD}
#SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

sudo docker run --rm --name pyjq_run -v $CUR_DIR:/home/myadmin -e asdasdasd?? pyjqm



#cd "${SCRIPT_DIR}" || exit 1

#if [ input_args ] ; then
	#pipenv run python "${SCRIPT_DIR}/migr_maxi_v1.py" --path=${CUR_DIR} --keys="$input_args"
#else
	#sudo docker run --rm --name pyjq_run -v $CUR_DIR:/home/myadmin pyjqm 
	#pipenv run python "${SCRIPT_DIR}/migr_maxi_v1.py" --path=${CUR_DIR}
fi

#cd "${CUR_DIR}" || exit 1
sleep 1

echo "==================== PYJQ MIGRATOR FINISH =================="
