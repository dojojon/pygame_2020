#!/bin/bash

echo 'Copy common files to game dirs'

function copy_common(){
    echo 'Creating Common: '$1
    mkdir -p ./$1/common/
    cp -v ./particles/particle_engine.py ./$1/common/.
    echo ''
}


copy_common lemon_leak
copy_common galga
