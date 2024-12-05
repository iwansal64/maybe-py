printf "\33[1;35mWELCOME TO MAYBE.PY INSTALLATION!!\r"

sleep 2

printf "Creating the environment for you......\t :)\r"

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

if ! printf "python $SCRIPT_DIR/maybe.py \$1 \$2 \$3 \$4" > /usr/bin/maybe; then
    printf "There's something wrong.. Did you run this with 'sudo'? If not please use it :)\n"
else
    sleep 1
    printf "DONE! Yeahh, Just it! Easy right?....\t :)\n"
fi

